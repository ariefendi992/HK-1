from flask_wtf import FlaskForm
from wtforms import TextField, PasswordField, SelectField, BooleanField
from wtforms.validators import DataRequired, Length
from app.admin.model.model_admin import *

class LoginForm(FlaskForm):
   username = TextField('username :', validators=[DataRequired("username masih kosong.")])
   password = PasswordField('Kata Sandi :', validators=[DataRequired(), Length(min=6, message="Kata sandi tidak sesuai. Periksa kembali!")])
   role = SelectField('Tipe User :', choices=[(r.id, r.tipe_akun) for r in Role.query], validators=[DataRequired()])
   remember = BooleanField('Remember me')

