from flask_bcrypt import generate_password_hash
from app import db
from flask import Blueprint, render_template, request, redirect, url_for, flash, abort
from ..model.model_pasien import Gender, Pasien
from ..model.model_antrianp import AntrianPoli
from ..model.model_poli import Poli
from ..form.form_pasien import FormPasien, FormEditPasien
from flask_login import current_user, login_required, fresh_login_required
from datetime import datetime, date
from sqlalchemy import desc, cast, Date, and_

pasien = Blueprint('pasien', __name__, template_folder="../templates/admin/pasien")


choice_jk = []
for g in Gender.query.all():
	choice_jk.append((g.id, g.jk))

@pasien.route('/')
@login_required
def DataPasien():
	if current_user.role_id == 1:
		dataPasien = db.session.query(Pasien, Gender).join(Gender).filter(cast(Pasien.created_at, Date)==date.today()).order_by(desc(Pasien.id)).all()
		return render_template('data-pasien.html', dataPasien=dataPasien)
	else:
		return '<h3>Modul tidak ditemukan</h3>'

@pasien.route('/riwayat')
@login_required
def riwayatPasien():
  # query = Pasien.query.join(Gender, AntrianPoli, Poli).all()
  query = AntrianPoli.query.join(Poli, Pasien, Gender).order_by(desc(Pasien.id)).all()
  return render_template('riwayat-pasien.html', query=query)

@pasien.route('/tambah-data', methods=['GET', 'POST'])
@login_required
def TambahPasien():
	form = FormPasien(request.form)
	form.jk.choices = choice_jk
	if request.method == 'POST' and form.validate_on_submit():
		no_id = form.noid.data
		nama = form.nama.data
		jk = form.jk.data 
		tgl_lahir = form.tgl_lahir.data
		alamat = form.alamat.data 
		telp = form.telp.data
		id_user = current_user.id
		flash(message=f"Data { form.nama.data } berhasil di tambahkan", category="success")
		simpan = Pasien(no_identitas_p= no_id, nama_p= nama, id_jk_p= jk, tgl_lahir_p= tgl_lahir, alamat_p=alamat, telp_p= telp, id_user=id_user)
		simpan.createSlug(nama_p=nama)
		db.session.add(simpan)
		db.session.commit()
		return redirect(url_for('pasien.DataPasien'))

	return render_template('tambah-pasien.html', form=form)

@pasien.route('/edit-data-pasien', methods=['POST','GET'])
@login_required
def EditPasien():
	slug = request.args.get('slug')
	pasienData = Pasien.query.filter_by(slug=slug).first()
	form = FormEditPasien(obj=pasienData)
	form.id_jk_p.choices = choice_jk
	if request.method == 'POST' and form.validate_on_submit():
		pasienData.no_identitas_p = form.no_identitas_p.data
		pasienData.nama_p = form.nama_p.data 
		pasienData.id_jk_p = form.id_jk_p.data
		pasienData.tgl_lahir_p = form.tgl_lahir_p.data
		pasienData.alamat_p = form.alamat_p.data
		pasienData.telp_p = form.telp_p.data
		pasienData.username = form.username.data
		# pasienData.password = form.password.data
		pasienData.password = generate_password_hash(form.password.data)
		pasienData.updated_at = datetime.now()
		flash(message=f"data { form.nama_p.data } berhasil di update.", category="warning")
		db.session.commit()
		return redirect(url_for('pasien.DataPasien'))
	else:
		return render_template('edit-pasien.html', form=form, pasienData=pasienData)

@pasien.route('/hapus-data-pasien')
@login_required
def HapusPasien():
	slug = request.args.get('slug')
	DataPasien = Pasien.query.filter_by(slug=slug).first()
	flash(message=f"Data pasien telah di hapus.", category="danger")
	db.session.delete(DataPasien)
	db.session.commit()
	return redirect(url_for('pasien.DataPasien'))
