from app.admin.model.model_pasien import Pasien
from flask_wtf import FlaskForm
from wtforms import SelectField, StringField, SubmitField
from wtforms.validators import DataRequired, ValidationError
from app.admin.model.model_antrianp import AntrianPoli
from app.admin.model.model_pasien import Pasien
from app import db
from sqlalchemy import cast, Date, or_
from datetime import datetime, date

class FormAntrianPoli(FlaskForm):
  nama_pasien = SelectField('Nama Pasien ', choices=[()])
  id_poli = SelectField('Pilih Poli', choices=[])
  no_antrianp = StringField('No. Antrian Poli', validators=[DataRequired()])
  no_antrian_poli2 = StringField('No. Antrian Poli')
  no_antrian_poli = StringField('No. Antrian Poli')
  # status = SelectField('Pilih ', choices=[])
  simpan = SubmitField('Simpan')

  # def validate_no_antrianp(self, no_antrianp):
    
  #   query = db.session.query(AntrianPoli.id).filter(or_(AntrianPoli.id_poli == 1, AntrianPoli.id_poli == 2, AntrianPoli.id_poli == 3, AntrianPoli.id_poli == 4), AntrianPoli.no_antrianp == no_antrianp.data, cast(AntrianPoli.tgl_daftar, Date)==date.today()).all()
  #   if query:
  #     raise ValidationError(
  #               "No Antrian untuk hari sudah ada, silahkan di refresh halaman ini")
                
    # query2 = db.session.query(AntrianPoli.no_antrianp).filter(AntrianPoli.id_poli ==2, AntrianPoli.no_antrianp == no_antrianp.data, cast(AntrianPoli.tgl_daftar, Date)==date.today()).first()
    # if query2:
    #   raise ValidationError(
    #             "No Antrian untuk hari sudah ada, silahkan di refresh halaman ini")
  
  # def validate_nama_pasien(self, nama_pasien):
  #   # query = db.session.query(AntrianPoli.id_pasien).filter(AntrianPoli.id_pasien, AntrianPoli.no_antrianp == no_antrianp.data, cast(AntrianPoli.tgl_daftar, Date)==date.today()).first()
  #   query = db.session.query(AntrianPoli, Pasien).join(Pasien.nama_p).filter(AntrianPoli.id_poli == 3, Pasien.nama_p == nama_pasien.data, cast(AntrianPoli.tgl_daftar, Date)==date.today())
  #   if query:
  #     raise ValidationError(
  #               "No Antrian untuk hari sudah ada, silahkan di refresh halaman ini")

class FormCetakAntrian(FlaskForm):
  nama_pasien = SelectField('Nama Pasien ', choices=[()])
  id_poli = SelectField('Pilih Poli', choices=[])
  no_antrianp = StringField('No. Antrian Poli')
  no_antrian_poli2 = StringField('No. Antrian Poli')
  no_antrian_poli = StringField('No. Antrian Poli')
  cetak = SubmitField('Cetak')