from flask import g
from app.controllers.DatabaseController import DatabaseController

#
def init_db_controller(app):
  app.teardown_appcontext(clear_db_controller)
  get_db_controller()

#
def get_db_controller():
  if 'db' not in g:
    g.db = DatabaseController()

  return g.db

#
def clear_db_controller(e=None):
  g.pop('db', None)
