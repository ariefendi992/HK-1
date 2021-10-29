from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

class FormPoli(FlaskForm):
  kodeP = StringField('Kode Poli')
  namaP = StringField('Nama Poli')
  simpan = SubmitField('Simpan')

class FormUbahPoli(FlaskForm):
  kode_poli = StringField('Kode Poli')
  nama_poli = StringField('Nama Poli')
  simpan = SubmitField('Simpan')