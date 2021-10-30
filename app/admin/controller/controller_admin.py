from app import db
from flask import Blueprint, render_template, request, redirect, url_for, flash, jsonify, session, abort
from ..form.form_user import UserAdd, UserEdit
from ..model.model_admin import Role, User
from ..model.model_pasien import Pasien
from ..model.model_antrianp import AntrianPoli
from sqlalchemy import func, Date, cast
from flask_login import login_required, login_user, logout_user, current_user
from datetime import date
import json
admin = Blueprint('admin', __name__, template_folder='../templates/admin')


choice_role = [("", "..:: Pilih ::..")]
for s in Role.query.all():
	choice_role.append((str(s.id), s.tipe_akun))
	# choice_role.append((s.id ,s.tipe_akun))

@admin.route('/')
@login_required
def indexAdmin():
    if current_user.is_authenticated:
        return redirect(url_for('admin.Index'))
    return redirect(url_for('auth.Login'))


@admin.route('/dashboard')
@login_required
def Index():
	if current_user.role_id == 1:
		if current_user.is_authenticated:
				listData = db.session.query(User, Role).join(Role).all()
				# data card
				dataPoliUmum = db.session.query(func.count(AntrianPoli.id)).filter(
						AntrianPoli.id_poli == 1, cast(AntrianPoli.tgl_daftar, Date) == date.today()).scalar()
				dataPoliGigi = db.session.query(func.count(AntrianPoli.id)).filter(
						AntrianPoli.id_poli == 2, cast(AntrianPoli.tgl_daftar, Date) == date.today()).scalar()
				dataPoliSpesialis = db.session.query(func.count(AntrianPoli.id)).filter(
						AntrianPoli.id_poli == 3, cast(AntrianPoli.tgl_daftar, Date) == date.today()).scalar()
				dataPoliKia = db.session.query(func.count(AntrianPoli.id)).filter(
						AntrianPoli.id_poli == 4, cast(AntrianPoli.tgl_daftar, Date) == date.today()).scalar()

				# data chart
				dataPasien = Pasien.query.count()
				totalPoli = db.session.query(func.count(AntrianPoli.id)).group_by(
						AntrianPoli.id_poli).order_by(AntrianPoli.id_poli).all()
				totalHarian = db.session.query(func.count(AntrianPoli.id)).group_by(AntrianPoli.id_poli).filter(
						cast(AntrianPoli.tgl_daftar, Date) == date.today()).order_by(AntrianPoli.id_poli).all()
				tot = []
				for total, in totalPoli:
						tot.append(total)

				toth = []
				for totalh, in totalHarian:
						toth.append(totalh)
				return render_template('user/index.html', totalHarian=json.dumps(toth), totalPoli=json.dumps(tot), listData=listData, dataPasien=dataPasien, dataPoliUmum=dataPoliUmum, dataPoliGigi=dataPoliGigi, dataPoliSpesialis=dataPoliSpesialis, dataPoliKia=dataPoliKia)
	else:
		abort(404)

# json chart data


@admin.route('/json-chart', methods=['GET', 'POST'])
def jsonChart():
    query = db.session.query(func.count(AntrianPoli.id)).group_by(AntrianPoli.id_poli).filter(
        cast(AntrianPoli.tgl_daftar, Date) == date.today()).order_by(AntrianPoli.id_poli).all()

    data = []
    for nilai, in query:
        data.append(nilai)

    return jsonify(data)


@admin.route('/data-tabel-pengguna')
@login_required
def DataPengguna():
    # listData = db.session.query(User, Role).join(Role).all()
    listData = User.query.join(Role).all()
    return render_template('user/data-pengguna.html', listData=listData)


@admin.route('/tambah-data', methods=['POST', 'GET'])
@login_required
def TambahData():
    form = UserAdd(request.form)
    form.tipe_akun.choices = choice_role
    if request.method == 'POST' and form.validate():
        nama = form.name.data
        username = form.username.data
        telp = form.telp.data
        role_id = form.tipe_akun.data
        password = form.password.data
        flash(
            message=f"Data {form.name.data} berhsil ditambahkan.", category="success")
        tambah = User(nama=nama, username=username, telp=telp,
                      role_id=role_id, password=password)
        db.session.add(tambah)
        db.session.commit()
        return redirect(url_for('admin.DataPengguna'))
    else:
        return render_template('user/tambah-data.html', form=form)


@admin.route('/ubah-data', methods=['GET', 'POST'])
@login_required
def UbahData():
	slug = request.args.get('slug')
	user_data = User.query.filter_by(slug=slug).first()
	form = UserEdit(obj=user_data)
	form.role_id.choices = choice_role
	if request.method == 'POST' and form.validate_on_submit():
			user_data.nama = form.nama.data
			user_data.username = form.username.data
			user_data.telp = form.telp.data
			user_data.role_id = form.role_id.data
			db.session.commit()
			return redirect(url_for('admin.DataPengguna'))
	else:
			return render_template('user/edit-data.html', form=form)


@admin.route('/delete-data', methods=['GET', 'POST'])
@login_required
def DeleteData():
	slug = request.args.get('slug')
	user_data = User.query.filter_by(slug=slug).first()
	flash(message=f"data berhsil di hapus", category="success")
	db.session.delete(user_data)
	db.session.commit()
	return redirect(url_for('admin.DataPengguna'))
