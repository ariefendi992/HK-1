from ..model.model_poli import Poli
from flask import Blueprint, render_template, request, flash, redirect, url_for
from ..form.form_poli import FormPoli, FormUbahPoli
from app import db
from flask_login import login_required
from app.helper.decoratorAdmin import adminRequired

poli = Blueprint('poli', __name__, template_folder='../templates/admin/poli')

@poli.route('/Kategori-Poli')
@login_required
@adminRequired
def DataPoli():
  dataPoli = Poli.query.all()
  return render_template('data-poli.html', dataPoli=dataPoli)

@poli.route('/tambah-poli', methods=['GET','POST'])
@login_required
def TambahPoli():
  form = FormPoli(request.form)
  if request.method == 'POST' and form.validate_on_submit():
    kodeP = form.kodeP.data
    namaP = form.namaP.data
    simpan = Poli(kode_poli=kodeP, nama_poli= namaP)
    flash(message=f" Data { form.namaP.data } berhasil di tambahkan", category="success")
    db.session.add(simpan)
    db.session.commit()
    return redirect(url_for('poli.DataPoli'))
  else:
    return render_template('tambah-poli.html', form=form)

@poli.route('/ubah-poli', methods=['GET','POST'])
@login_required
def UbahPoli():
  slug = request.args.get('slug')
  poliData = Poli.query.filter_by(slug=slug).first()
  form = FormUbahPoli(obj=poliData)
  if request.method == 'POST' and form.validate_on_submit():
    poliData.kode_poli = form.kode_poli.data
    poliData.nama_poli = form.nama_poli.data
    flash(message=f"Data {form.nama_poli.data} berhasil di update", category='warning')
    db.session.commit()
    return redirect(url_for('poli.DataPoli'))
  else:
    return render_template('edit-poli.html', form=form, poliData=poliData)
