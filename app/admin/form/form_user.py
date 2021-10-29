from flask_wtf import FlaskForm
from wtforms import TextField, PasswordField, SelectField
from wtforms.fields.simple import SubmitField
from wtforms.validators import DataRequired, Email, Length, ValidationError, EqualTo
from ..model.model_admin import User, Role


class UserAdd(FlaskForm):
    name = TextField('Nama :', validators=[DataRequired("Nama belum diisi")])
    username = TextField('username :', validators=[DataRequired("Username belum disi")])
    telp = TextField('No. HP/WA :', validators=[DataRequired("No. Telp/Wa belum di isi"), Length(
        min=10, max=15, message="Minimal 10, dan maksismal 15 digit")])
    tipe_akun = SelectField('Tipe Akun :',  choices=[], validators=[DataRequired("Pilih Tipe Akun")])
    password = PasswordField('Password :', validators=[
        DataRequired("Minimal 6 Karakter")])
    simpan = SubmitField('Simpan')

    def validate_username(self, username):
        username_found = User.query.filter_by(username=username.data).first()
        if username_found:
            raise ValidationError(
                "Username sudah terdaftar. Silahkan gunakan username lain!")


    def validate_telp(self, telp):
        telp_found = User.query.filter_by(telp=telp.data).first()
        if telp_found:
            raise ValidationError(
                "No. Telp sudah digunakan, silahkan gunakan yang lain!")

class UserEdit(FlaskForm):
    nama = TextField('Nama :', validators=[DataRequired()])
    username = TextField('Username :', validators=[DataRequired()])
    telp = TextField('No. HP/WA :', validators=[DataRequired(), Length(
        min=10, max=15, message="Minimal 10, dan maksismal 15 digit")])
    role_id = SelectField('Tipe Akun :', choices=[])
    password = PasswordField('Password :', validators=[
        DataRequired("Minimal 6 Karakter")])
    konf_password = PasswordField('Ulangi Password :', validators=[EqualTo(
        'password', message='Password yang dimasukkan tidak sesuai.')])
