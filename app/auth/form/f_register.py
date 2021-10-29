from flask_wtf import FlaskForm
from flask_wtf.recaptcha import validators
from wtforms import TextField, PasswordField, SelectField, BooleanField
from wtforms.validators import DataRequired, Length
from app.admin.model.model_admin import *

class RegisTerForm(FlaskForm):
  nama = TextField('nama', validators=[DataRequired("Nama harus di isi.")])
  telp = TextField('No. Telp', validators=[DataRequired("No. Telp harus di isi.")])
  username = TextField('username :', validators=[DataRequired("username masih kosong.")])
  password = PasswordField('Kata Sandi :', validators=[DataRequired(), Length(min=6, message="Kata sandi tidak sesuai. Periksa kembali!")])
  role = SelectField('Tipe User :', choices=[('','.:: Pilih ::.'),('2','Dokter'),('3','Pasien')], validators=[DataRequired()])
  remember = BooleanField('Remember me')