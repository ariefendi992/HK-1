from flask import session, flash, url_for
from datetime import timedelta
from werkzeug.wrappers import request
from app import app, login_manager
from app.admin import admin, pasien, poli, antrianp
from app.user import user
from app.auth import auth
from app.pasien import ps
from app.site import site
from app.helper.format_date import dateformat
from app.admin.model.model_pasien import Pasien
from app.admin.model.model_admin import User

@login_manager.user_loader
def load_user(user_id):
  return User.query.get(int(user_id))

app.register_blueprint(admin, url_prefix='/admin')
app.register_blueprint(pasien, url_prefix='/admin/pasien')
app.register_blueprint(poli, url_prefix='/admin/kategori-poli')
app.register_blueprint(antrianp, url_prefix='/admin/antrian-poli')
app.register_blueprint(ps, url_prefix='/user-pasien')
# app.register_blueprint(user, url_prefix='/')
app.register_blueprint(site, url_prefix='/')
app.register_blueprint(auth, url_prefix='/auth')
# login_manager.login_view = 'auth.Login'
login_manager.blueprint_login_views = {'pasiens': 'auth.Login','admin': 'auth.Login', 'pasien' : 'auth.Login', 'poli' : 'auth.Login', 'antrianp' : 'auth.Login', 'front' : '/masuk'}

login_manager.login_message = u"login dulu untuk akses halaman ini."
login_manager.login_message_category = "info"

# login_manager.session_protection = 'strong'
login_manager.refresh_view = 'auth.Login'
login_manager.needs_refresh_message = 'silahkan login kembali'
login_manager.needs_refresh_message_category = 'info'

# @app.before_request
# def before_request():
#   # session.permanent = True
#   app.permanent_session_lifetime = True

