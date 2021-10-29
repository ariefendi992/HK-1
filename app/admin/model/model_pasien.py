from app import db
from datetime import date, datetime
from slugify import slugify
from .model_antrianp import AntrianPoli


class Pasien(db.Model):
  __tablename__ = "pasien"
  id = db.Column(db.BigInteger(), primary_key=True)
  no_identitas_p = db.Column(db.BigInteger(), nullable=False)
  nama_p = db.Column(db.String(80), nullable=False)
  slug = db.Column(db.String(80), nullable=False)
  id_jk_p = db.Column(db.Integer(), db.ForeignKey('gender.id'))
  tgl_lahir_p = db.Column(db.Date(), nullable=False)
  alamat_p = db.Column(db.Text())
  telp_p = db.Column(db.String(20))
  created_at = db.Column(db.Date(), default=date.today())
  updated_at = db.Column(db.DateTime())
  id_user = db.Column(db.BigInteger(), db.ForeignKey('user.id'))
  id_antrian = db.relationship('AntrianPoli', backref='pasien', lazy=True)
  # users = db.relationship('User', backref='role', lazy=True)
  

  def createSlug(self, nama_p):
      self.slug = slugify(nama_p, to_lower=True, separator='-')

  def __repr__(self):
      return '<id : {} - nama : {} - id_jk : {} >'. format(self.id, self.nama_p, self.id_jk_p)


class Gender(db.Model):
  __tablename__ = "gender"
  id = db.Column(db.Integer(), primary_key=True)
  jk = db.Column(db.String(20), nullable=False, unique=True)
  pasiens = db.relationship('Pasien', backref='gender', lazy=True)

  def __repr__(self):
      return '<id {} jk {}>'. format(self.id, self.jk)
