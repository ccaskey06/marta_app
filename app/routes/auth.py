from flask import Blueprint, current_app, escape, flash, g, redirect, render_template, request, session, url_for
from app.shared import db, hasher

from app.models.RegisterForm import RegisterForm

#
auth_bp = Blueprint('auth', __name__)
FILE_PATH = 'auth/login-and-registration.html'

#
@auth_bp.route('/', methods=['GET', 'POST'])
@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
  hasher.get_hash_controller()
  db.get_db_controller()

  if request.method == 'POST':
    username = escape(request.form['username'])
    password = escape(request.form['password'])
    
    # encrypted password is pulled from the database
    encrypted_password = ''

    is_correct_password = g.hasher.check_hash(encrypted_password, password)

  return render_template(FILE_PATH, is_registration=False, error=None)

#
@auth_bp.route('/register', methods=['GET', 'POST'])
def register():
  db.get_db_controller()
  hasher.get_hash_controller()

  register_form = RegisterForm()

  if request == 'POST' and register_form.validate():
    print('success')

  # if request.method == 'POST':
  #   username = escape(request.form['username'])
  #   email = escape(request.form['email'])
  #   password = escape(request.form['password'])
  #   confirm_password = escape(request.form['confirm_password'])
  #   encrypted_password = g.hasher.generate_hash(escape(request.form['password']))

  #   unique_username = g.db.is_unique_username(username)
  #   unique_email = g.db.is_unique_email(email)

  #   if unique_username and unique_email:
  #     if g.db.create_user(username, email, encrypted_password):
  #       return redirect(url_for('views.temp_dashboard'))

  #     else:
  #       return render_template(
  #         FILE_PATH,
  #         is_registration=True,
  #         error='Unable To Create Account. Contact Admin.',
  #         username=username,
  #         email='',
  #         password=password,
  #         confirm_password=confirm_password
  #       )

  #       # provide modal with error message and button to fill out admin form
        
  #   elif not unique_email:
  #     return render_template(
  #       FILE_PATH,
  #       is_registration=True,
  #       error='Email Already Associated With An Account',
  #       username=username,
  #       email='',
  #       password=password,
  #       confirm_password=confirm_password
  #     )

  #   else: # username error message
  #     return render_template(
  #       FILE_PATH,
  #       is_registration=True,
  #       error='Username Already Taken',
  #       username='',
  #       email=email,
  #       password=password,
  #       confirm_password=confirm_password
  #     )

  #   # # user is default a passenger - has an email
  #   # try:
  #   #   # check uniqueness of email - if works, passenger created
  #   #   dbCursor.execute("INSERT INTO `Passenger`(`Username`, `Email`) VALUES (%s, %s)", [username, email])

  #   # except: # query fails if email (unique) already exists
  #   #   error = 'Account already exists for this email. Incorrect credentials'
  #   #   return render_template('registration_page.html', error = error, reg_user_val = username, reg_pass_val = password, reg_confirm_val = password, reg_email_val = "")
  #   #   # reset value for email - save other inputs

  #   # # user selects "Doesn't Have Breezecard" - input is empty
  #   # if breezecard == "":
  #   #   # generate new breezecard, insert it into database
  #   #   generate_breezecard(dbCursor, username)

  #   # ## for using "Have Breezecard", check if Breezecard is already in the system
  #   # else:

  #   #   try:
  #   #     # try to insert breezecard into database
  #   #     dbCursor.execute("""INSERT INTO `Breezecard`(`BreezecardNum`, `Value`, `BelongsTo`) VALUES (%s, 0, %s)""", [breezecard, username])

  #   #   except: # breezecard already exists in database - query fails

  #   #     countNull = None

  #   #     try:
  #   #       # will either return 0 or 1 tuple(s)
  #   #       dbCursor.execute("""SELECT * FROM `Breezecard` WHERE `BreezecardNum` = %s AND `BelongsTo` IS NULL""", [breezecard])

  #   #       countNull = dbCursor.rowcount # number of tuples

  #   #     except: # query fails for some reason - generate random card and go to passenger dashboard

  #   #       generate_breezecard(dbCursor, username)
  #   #       return redirect(url_for('pass_dashboard', username=username))

  #   #     # only works if above query worked
  #   #     if countNull > 0: # this breezecard has a NULL owner
  #   #       try:
  #   #         # card exists but doesn't belong to anyone (i.e. BelongsTo = NULL)
  #   #         dbCursor.execute("""UPDATE `Breezecard` SET `BelongsTo` = %s WHERE `BreezecardNum` = %s""", [username, breezecard])

  #   #       except: # query fails for some reason - generate random card and go to passenger dashboard

  #   #         generate_breezecard(dbCursor, username)
  #   #         return redirect(url_for('pass_dashboard', username=username))

  #   #     else: # breezecard has an associated owner

  #   #       # get current timestamp
  #   #       dateTime = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

  #   #       # create Conflict (i.e. suspend card)
  #   #       try:

  #   #         dbCursor.execute("""INSERT INTO `Conflict`(`Username`, `BreezecardNum`, `DateTime`) VALUES (%s, %s, %s)""", [username, breezecard, dateTime])
  #   #         generate_breezecard(dbCursor, username) # generate new breezecard for username

  #   #       except: # query fails - there already exists a conflict for this username and breezecard; generate new breezecard and redirect to passenger dashboard

  #   #         generate_breezecard(dbCursor, username)
  #   #         return redirect(url_for('pass_dashboard', username=username))

  #   # db.commit()
  #   # dbCursor.close()
  #   # db.close()

  #   # # submit inputs and go right to passenger dashboard
  #   # return redirect(url_for('pass_dashboard', username=username))


  #   # transit_card = escape(request.form['transit_card']).replace(' ', '')
  
  print('error')
  return render_template(
    FILE_PATH,
    form=register_form,
    is_registration=True,
    username='',
    email='',
    password='',
    confirm_password=''
  )
