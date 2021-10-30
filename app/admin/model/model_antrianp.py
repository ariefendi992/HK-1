from app import db
from datetime import date, datetime

class AntrianPoli(db.Model):
  __tablename__ = 'antrianp'
  id = db.Column(db.Integer(), primary_key=True)
  id_pasien = db.Column(db.BigInteger(), db.ForeignKey('pasien.id'))
  id_poli = db.Column(db.Integer(), db.ForeignKey('poli.id_poli'))
  no_antrianp = db.Column(db.Integer())
  tgl_daftar = db.Column(db.Date(), default=date.today())
  tgl_update = db.Column(db.DateTime())
  status = db.Column(db.Enum('1','0'), default='0')

  def __repr__(self):
    return '( id pasien {}, id Poli {}, noantrian {} )'.format(self.id_pasien, self.id_poli, self.no_antrianp)
