from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField

from wtforms.validators import DataRequired

class FormLoginPasien(FlaskForm):
  usrname = StringField('Username', validators=[DataRequired("Data belum di isi.")])
  pswd = PasswordField('Password', validators=[DataRequired("Data belum di isi.")])
  