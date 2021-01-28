from psycopg2 import connect, Error
from flask import current_app

#
class DatabaseController(object):

  #
  def __init__(self):
    try:
      self._db_connection = connect(
        database=current_app.config['DATABASE'], 
        user=current_app.config['USER'], 
        password=current_app.config['PASSWORD'], 
        host=current_app.config['HOST'], 
        port=current_app.config['PORT']
      )
      self._db_cursor = self._db_connection.cursor()

    except (Exception, Error) as e:
      current_app.logger.error('Failed Database Connection: %s', str(e))

  #
  def _call_procedure(self, procedure_query, procedure_params) -> bool:
    """
      --- Python Documentation ---
    """

    try:
      self._db_cursor.execute(procedure_query, procedure_params)
      self._db_connection.commit()

      return True

    except (Exception, Error) as e:
      current_app.logger.error('Failed Procedure: %s', str(e))

      return False

  #
  def get_db_cursor(self):
    return self._db_cursor if hasattr(self, '_db_cursor') else None

  #
  def get_db_connection(self):
    return self._db_connection if hasattr(self, '_db_connection') else None

  # Query Methods

  #
  def create_user(self, username, email, password):
    """
      Attempts to create a new user in the DB; will fail if the username
      already exists and is associated with a different account.
    """

    try:
      self._db_cursor.execute(
        'CALL public.udp_add_user(%s, %s, %s, %s, %s);',
        (username, email, password, False, self._generate_user_id())
      )
      self._db_connection.commit()

      return True

    except (Exception, Error) as e:
      current_app.logger.error('Failed Procedure: %s', str(e))

      return False
  
  #
  def is_unique_username(self, username):
    self._db_cursor.callproc('public.fn_get_account_from_username', [username]) # returns whether username exists

    return not bool(self._db_cursor.fetchone()[0])

  #
  def is_unique_email(self, email):
    self._db_cursor.callproc('public.fn_get_account_from_email', [email]) # returns whether email exists

    return not bool(self._db_cursor.fetchone()[0])

  #
  def _generate_user_id(self):
    self._db_cursor.callproc('public.fn_get_number_of_accounts')
    
    return int(self._db_cursor.fetchone()[0]) + 1

  #
  def validate_returning_user(self, username, password):

    pass
