from app import db
from flask import Blueprint, render_template, request, flash, url_for, redirect
from app.admin.form.form_pasien import FormPasien
from app.admin.model.model_pasien import Gender, Pasien
from app.user.form.form_login_pasien import FormLoginPasien
from flask_login import login_required, login_user, logout_user, current_user

user = Blueprint('user', __name__, template_folder='../templates/user')


choice_jk = []
for g in Gender.query.all():
	choice_jk.append((g.id, g.jk))

@user.route('/')
def indexUser():
  # if current_user.is_authenticated:
  #   return redirect(url_for('user.antrianUser'))
  return render_template('index.html')

@user.route('/pendaftaran', methods=['POST','GET'])

def registerPasien():
  form = FormPasien(request.form)
  form.jk.choices= choice_jk
  if request.method == 'POST' and form.validate_on_submit():
      no_id = form.noid.data
      nama = form.nama.data
      jk = form.jk.data 
      tgl_lahir = form.tgl_lahir.data
      alamat = form.alamat.data 
      telp = form.telp.data
      username = form.username.data
      password = form.password.data
      flash(message=f"Data { form.nama.data } berhasil di tambahkan", category="success")
      simpan = Pasien(no_identitas_p= no_id, nama_p= nama, id_jk_p= jk, tgl_lahir_p= tgl_lahir, alamat_p=alamat, telp_p= telp, username=username, password=password)
      simpan.createSlug(nama_p=nama)
      simpan.generatePassword(password=password)
      db.session.add(simpan)
      db.session.commit()
      return redirect(url_for('user.indexUser'))

  return render_template('registrasi.html', form=form)

@user.route('/masuk', methods=['POST','GET'])
def loginUser():
  # if current_user.is_authenticated:
  #   return redirect(url_for('user.antrianUser'))
  form = FormLoginPasien(request.form)
  if request.method == 'POST' and form.validate_on_submit:
    pasien = Pasien.query.filter_by(username=form.usrname.data).first()  
    if not pasien:
      flash(message="pasien name belum terdaftar", category="danger")
    elif pasien  and pasien.cekPassword(form.pswd.data):
      login_user(pasien)
      flash(message="Login Sukses", category='success')
      # next = request.args.get('next')
      return redirect(url_for('user.antrianUser'))
    else:
      flash(message="Login Gagal", category='danger')
  return render_template('login.html', form=form)

@user.route('/keluar')
@login_required
def Keluar():
  logout_user()
  flash("Anda telah keluar.", "info")
  return redirect(url_for('user.indexUser'))

@user.route('/halaman-index-user')
@login_required
def antrianUser():
  
  return render_template('antrian-user.html')

@user.route('/poli-umum', methods=['GET','POST'])
@login_required
def poliUmum ():
  return render_template('poli-umum.html')
