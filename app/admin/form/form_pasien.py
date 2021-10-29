from flask_wtf import FlaskForm
from flask_wtf.recaptcha import validators
from wtforms import TextField, RadioField, TextAreaField, DateField, SubmitField, SelectField
from wtforms.fields.html5 import DateField
from wtforms.fields.simple import PasswordField
from wtforms.validators import DataRequired, Length, InputRequired, Required, ValidationError
from ..model.model_pasien import Pasien

class FormPasien(FlaskForm):
    noid = TextField('No. Identitas', validators=[DataRequired("No. Identitas / KTP masih kosong")])
    nama = TextField('Nama Pasien :', validators=[DataRequired("Nama Pasien Masih Kosong")])
    jk = RadioField('Jenis Kelamin :', choices=[],validators=[Required("Pilih Jenis Kelamin")], default=1 )
    tgl_lahir = DateField("Tanggal Lahir :", validators=[InputRequired("Pilih Tanggal, Bulan & Tahun Lahir")])
    alamat = TextAreaField('Alamat :', validators=[InputRequired("Alamat Masih Kosong")])
    telp = TextField(
        'No. Telp/WA :', validators=[DataRequired("No. Telp/Whatsapp Masih Kosong"), Length(min=10, max=15, message="Masukan Telp/Hp yang sesuai")])
    simpan = SubmitField("Simpan")

    def validate_noid(self, noid):
        identitas = Pasien.query.filter_by(no_identitas_p=noid.data).first()
        if identitas:
            raise ValidationError("No. Identitas sudah terdaftar")
   

class FormEditPasien(FlaskForm):
    no_identitas_p = TextField('No. Identitas', validators=[DataRequired("No. Identitas / KTP masih kosong")])
    nama_p = TextField('Nama Pasien :', validators=[DataRequired("Nama Pasien Masih Kosong")])
    id_jk_p = RadioField('Jenis Kelamin :', choices=[],validators=[Required("Pilih Jenis Kelamin")], default=1 )
    tgl_lahir_p = DateField("Tanggal Lahir :", validators=[InputRequired("Pilih Tanggal, Bulan & Tahun Lahir")])
    alamat_p = TextAreaField('Alamat :', validators=[InputRequired("Alamat Masih Kosong")])
    telp_p = TextField(
        'No. Telp/WA :', validators=[DataRequired("No. Telp/Whatsapp Masih Kosong"), Length(min=10, max=15, message="Masukan Telp/Hp yang sesuai")])
    
    simpan = SubmitField("Update")

