from flask.app import Flask
from sqlalchemy.sql.expression import true
from app import db
from slugify import slugify
from .model_antrianp import AntrianPoli

class Poli(db.Model):
  __tablename__ = 'poli'
  id_poli = db.Column(db.Integer, primary_key=True)
  kode_poli = db.Column(db.String(30), nullable=False, unique=True)
  nama_poli = db.Column(db.String(30), nullable=False, unique=True)
  slug = db.Column(db.String(30), nullable=False)
  jumlah_maks = db.Column(db.Integer())
  id_antrian = db.relationship('AntrianPoli', backref='poli', lazy=True)

  def __init__(self, kode_poli, nama_poli):
    self.kode_poli = kode_poli
    self.nama_poli = nama_poli
    self.slug = slugify(nama_poli, to_lower=True)
    # self.jumlah_maks = jumlah_maks
  
  def __repr__(self):
    return '< id_poli {} poli {} >'.format(self.kode_poli, self.nama_poli)

