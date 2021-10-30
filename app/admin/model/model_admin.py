from flask.helpers import flash
from app import db, bcrypt, login_manager
from datetime import datetime, date
from slugify import slugify
from flask_login import UserMixin


# @login_manager.user_loader
# def load_user(id):
#   user = User.query.get(id)
#   if user is None:
#     flash('Anda telah keluar')
#   return user
  # return User.query.get(id)

class User(db.Model, UserMixin):
  __tablename__ = 'user'
  id = db.Column(db.BigInteger(), primary_key=True)
  nama = db.Column(db.String(80), nullable=False)
  slug = db.Column(db.String(80), nullable=False)
  username = db.Column(db.String(80), nullable=False, unique=True)
  telp = db.Column(db.String(15), nullable=False)
  password = db.Column(db.Text(), nullable=False)
  created_at = db.Column(db.Date(), default=date.today())
  updated_at = db.Column(db.DateTime(), default=datetime.today())
  role_id = db.Column(db.BigInteger(), db.ForeignKey('role.id'))
  status = db.Column(db.Enum('1','0'), default='1')

  def __init__(self, nama, username, telp, password, role_id):
    self.nama = nama
    self.slug = slugify(nama, to_lower=True, separator='-')
    self.username = username
    self.telp = telp
    if password != '':
      self.password = bcrypt.generate_password_hash(password).decode('utf8')
    self.role_id = role_id


  def __repr__(self):
    return '<User nama : {} - username : {} - role id : {} >'.format(self.nama, self.username, self.role_id)

  def checkPassword(self, password):
    return bcrypt.check_password_hash(self.password, password)

class Role(db.Model):
  id = db.Column(db.BigInteger(), primary_key=True)
  tipe_akun = db.Column(db.String(20), nullable=False, unique=True)
  users = db.relationship('User', backref='role', lazy=True)
  
  
  def __repr__(self):
    return '{} {} '.format(self.id, self.tipe_akun)