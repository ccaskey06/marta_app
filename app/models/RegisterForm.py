from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, SubmitField, TextField
from wtforms.validators import DataRequired, Email, EqualTo, InputRequired, Length

#
class RegisterForm(FlaskForm):
  """
    Register Form
  """

  username = StringField(
    'Username',
    [
      DataRequired()
    ]
  )

  email = StringField(
    'Email', 
    [
      DataRequired(),
      Email()
    ]
  )

  password = PasswordField(
    'Password',
    [
      DataRequired(),
      Length(min=8)
    ]
  )

  confirm_password  = PasswordField(
    'Confirm Password',
    [
      DataRequired(),
      EqualTo('password')
    ]
  )

  submit = SubmitField('Register')
