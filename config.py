from os import path, environ
from dotenv import load_dotenv
from datetime import timedelta

base_dir = path.abspath(path.dirname(__file__))
load_dotenv(path.join(base_dir,'.env'))

class Konfigurasi(object):
  USERNAME = environ.get('DB_USERNAME')
  PASSWORD = environ.get('DB_PASSWORD')
  HOST = environ.get('DB_HOST')
  DATABASE = environ.get('DB_NAME')

  SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://'+ USERNAME + ':'+ PASSWORD +'@'+ HOST + '/'+ DATABASE
  SQLALCHEMY_TRACK_MODIFICATIONS= False
  SQLALCHEMY_RECORD_QUERIES = True

  SECRET_KEY = environ.get('SECRET_KEY')
  REMEMBER_COOKIE_DURATION = timedelta(seconds=10)
