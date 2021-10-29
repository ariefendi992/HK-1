from datetime import datetime
from flask import Blueprint, request, render_template, redirect, url_for, flash, jsonify
from sqlalchemy.sql.elements import AnnotatedColumnElement
from sqlalchemy.sql.sqltypes import ARRAY
from app import db
from ..model.model_antrianp import AntrianPoli, TAntrian
from ..model.model_pasien import Pasien
from ..model.model_poli import Poli
from ..form.form_antrianp import FormAntrianPoli, FormCetakAntrian
from sqlalchemy import desc, func, select, cast, Date, asc, or_, DateTime
from flask_login import login_required
from datetime import date, datetime
import json

antrianp = Blueprint('antrianp', __name__,
                    template_folder='../templates/admin/antrianpoli')


def choicePasien():
    choice = [("", "..:: Pilih ::..")]
    for pas in Pasien.query.filter(or_(cast(Pasien.created_at, Date) == date.today(), func.Date(Pasien.updated_at)==date.today())):
    # for pas in Pasien.query.filter(func.Date(Pasien.updated_at)==date.today()):
        choice.append((pas.id, pas.nama_p))
    return choice


def choicePoli():
    choice = [("", "..:: Pilih ::..")]
    for pol in Poli.query.filter(Poli.id_poli):
        choice.append((pol.id_poli, pol.nama_poli))
    return choice

# histori antrian


@antrianp.route('/data-antrian')
@login_required
def DataAntrian():
    dataAntrian = db.session.query(
        AntrianPoli, Pasien, Poli).join(Pasien, Poli).all()
    
    query = db.session.query(func.sum(AntrianPoli.id).label("jumlah")).filter(AntrianPoli.id_poli == 1, cast(AntrianPoli.tgl_daftar, Date)==date.today(), AntrianPoli.status == 0)
    
    return render_template('data-antrian.html', dataAntrian=dataAntrian, query=query)


# Data Antrian Harian
@antrianp.route('/antrian-harian')
@login_required
def AntrianHarian():

  # Antrian Sekarang Poli Umum
  query = db.session.query(AntrianPoli.no_antrianp).filter(AntrianPoli.id_poli == 1, cast(
        AntrianPoli.tgl_daftar, Date) == date.today(), AntrianPoli.status == '1').order_by(desc(AntrianPoli.tgl_update)).limit(1)
  rows1 = db.session.query(func.count()).select_from(query).scalar()

  # Antrian Selanjutnya Poli Umum
  query11 = db.session.query(AntrianPoli.no_antrianp).filter(AntrianPoli.id_poli == 1, cast(
        AntrianPoli.tgl_daftar, Date) == date.today(), AntrianPoli.status == '0').order_by(asc(AntrianPoli.no_antrianp)).limit(1)
  rows11 = db.session.query(func.count()).select_from(query11).scalar()
  return render_template('antrian-harian.html', rows1=rows1, rows11=rows11)


@antrianp.route('/json1', methods=['GET', 'POST'])
@login_required
def jsonUmumHarian():
    query = db.session.query(AntrianPoli, Pasien, Poli).join(Poli, Pasien).filter(
        AntrianPoli.id_poli == 1, cast(AntrianPoli.tgl_daftar, Date) == date.today())
    rows = db.session.query(func.count()).select_from(query)

    if rows:
        response = {}
        response['data'] = []

        for row, row2, row3 in query:
            data = {}
            data['id'] = row.id
            data['nama_p'] = row2.nama_p
            data['nama_poli'] = row3.nama_poli
            data['no_antrianp'] = row.no_antrianp
            data['tgl_daftar'] = row.tgl_daftar
            data['status'] = row.status
            data['id_poli'] = row.id_poli

            response['data'].append(data)

        return jsonify(response)
    else:
        response = {}
        response['data'] = []
        data = {}
        data['id'] = ''
        data['nama_p'] = ''
        data['nama_poli'] = ''
        data['no_antrianp'] = ''
        data['tgl_daftar'] = ''
        data['status'] = ''
        response['data'].append(data)
        return jsonify(response)


@antrianp.route('/json2', methods=['GET', 'POST'])
@login_required
def jsonGigiHarian():
    query = db.session.query(AntrianPoli, Pasien, Poli).join(Poli, Pasien).filter(
        AntrianPoli.id_poli == 2, cast(AntrianPoli.tgl_daftar, Date) == date.today())
    rows = db.session.query(func.count()).select_from(query)

    if rows:
        response = {}
        response['data'] = []

        for row, row2, row3 in query:
            data = {}
            data['id'] = row.id
            data['nama_p'] = row2.nama_p
            data['nama_poli'] = row3.nama_poli
            data['no_antrianp'] = row.no_antrianp
            data['tgl_daftar'] = row.tgl_daftar
            data['status'] = row.status
            data['id_poli'] = row.id_poli

            response['data'].append(data)

        return jsonify(response)
    else:
        response = {}
        response['data'] = []
        data = {}
        data['id'] = ''
        data['nama_p'] = ''
        data['nama_poli'] = ''
        data['no_antrianp'] = ''
        data['tgl_daftar'] = ''
        data['status'] = ''
        response['data'].append(data)
        return jsonify(response)


@antrianp.route('/json3', methods=['GET', 'POST'])
@login_required
def jsonSpesialisHarian():
    query = db.session.query(AntrianPoli, Pasien, Poli).join(Poli, Pasien).filter(
        AntrianPoli.id_poli == 3, cast(AntrianPoli.tgl_daftar, Date) == date.today())
    rows = db.session.query(func.count()).select_from(query)

    if rows:
        response = {}
        response['data'] = []

        for row, row2, row3 in query:
            data = {}
            data['id'] = row.id
            data['nama_p'] = row2.nama_p
            data['nama_poli'] = row3.nama_poli
            data['no_antrianp'] = row.no_antrianp
            data['tgl_daftar'] = row.tgl_daftar
            data['status'] = row.status
            data['id_poli'] = row.id_poli

            response['data'].append(data)

        return jsonify(response)
    else:
        response = {}
        response['data'] = []
        data = {}
        data['id'] = ''
        data['nama_p'] = ''
        data['nama_poli'] = ''
        data['no_antrianp'] = ''
        data['tgl_daftar'] = ''
        data['status'] = ''
        response['data'].append(data)
        return jsonify(response)


@antrianp.route('/json4', methods=['GET', 'POST'])
@login_required
def jsonKiaHarian():
    query = db.session.query(AntrianPoli, Pasien, Poli).join(Poli, Pasien).filter(
        AntrianPoli.id_poli == 4, cast(AntrianPoli.tgl_daftar, Date) == date.today())
    rows = db.session.query(func.count()).select_from(query)

    if rows:
        response = {}
        response['data'] = []

        for row, row2, row3 in query:
            data = {}
            data['id'] = row.id
            data['nama_p'] = row2.nama_p
            data['nama_poli'] = row3.nama_poli
            data['no_antrianp'] = row.no_antrianp
            data['tgl_daftar'] = row.tgl_daftar
            data['status'] = row.status
            data['id_poli'] = row.id_poli

            response['data'].append(data)

        return jsonify(response)
    else:
        response = {}
        response['data'] = []
        data = {}
        data['id'] = ''
        data['nama_p'] = ''
        data['nama_poli'] = ''
        data['no_antrianp'] = ''
        data['tgl_daftar'] = ''
        data['status'] = ''
        response['data'].append(data)
        return jsonify(response)


@antrianp.route('/json-umum/<id>', methods=['GET', 'POST', 'PUT', 'PATCH'])
def jsonUmumUp(id):
    # id = request.args.get('id')
    query = AntrianPoli.query.filter_by(id=id).first()
    if request.method == 'PUT':
        query.status = '1'
        query.tgl_update = datetime.now()
        db.session.commit()

    # return jsonify(query)


@antrianp.route('/tambah-antrian-poli', methods=['GET', 'POST'])
@login_required
def TambahAntrianPoli():
    form = FormAntrianPoli(request.form)
    form.nama_pasien.choices = choicePasien()
    form.id_poli.choices = choicePoli()

    id_poli = request.args.get('id_poli')
    sql1 = db.session.query(func.count(AntrianPoli.id)).filter(AntrianPoli.id_poli == 1, cast(
        AntrianPoli.tgl_daftar, Date) == date.today()).order_by(desc(AntrianPoli.no_antrianp)).scalar()
    sql2 = db.session.query(func.count(AntrianPoli.id)).filter(AntrianPoli.id_poli == 2, cast(
        AntrianPoli.tgl_daftar, Date) == date.today()).order_by(desc(AntrianPoli.no_antrianp)).scalar()
    sql3 = db.session.query(func.count(AntrianPoli.id)).filter(AntrianPoli.id_poli == 3, cast(
        AntrianPoli.tgl_daftar, Date) == date.today()).order_by(desc(AntrianPoli.no_antrianp)).scalar()
    sql4 = db.session.query(func.count(AntrianPoli.id)).filter(AntrianPoli.id_poli == 4, cast(
        AntrianPoli.tgl_daftar, Date) == date.today()).order_by(desc(AntrianPoli.no_antrianp)).scalar()

    if sql1 == 0:
        sql1 = 1
    else:
        sql1 += 1

    if sql2 == 0:
        sql2 += 1
    else:
        sql2 += 1

    if sql3 == 0:
        sql3 = 1
    else:
        sql3 += 1

    if sql4 == 0:
        sql4 = 1
    else:
        sql4 += 1

    if request.method == 'POST' and form.validate_on_submit():
        nama_pasien = form.nama_pasien.data
        id_poli = form.id_poli.data
        no_antrianp = form.no_antrianp.data
        flash(message=f"Data Antrian telah dibuat", category="success")
        tambah = AntrianPoli(id_pasien=nama_pasien,
                             id_poli=id_poli, no_antrianp=no_antrianp)
        db.session.add(tambah)
        db.session.commit()
        return redirect(url_for('antrianp.AntrianHarian'))
    else:
        return render_template('tambah-antrianp.html', form=form, sql1=sql1, sql2=sql2, sql3=sql3, sql4=sql4)


@antrianp.route('/cetak')
@login_required
def Cetak():
    id = request.args.get('id')
    cetakAntrian = AntrianPoli.query.filter_by(id=id).first()
    namap = []
    for i in Poli.query:
        namap.append((i.id_poli, i.nama_poli))
    # nama_poli = request.args.get('nama_poli')
    # poli = Poli.query.filter_by(nama_poli=nama_poli).first()
    # cetakAntrian = db.session.query(AntrianPoli, Poli).join(Poli).filter_by(id=id).all()

    return render_template('./helper/_cetak-antrian.html', cetakAntrian=cetakAntrian, namap=namap)

@antrianp.route('/hapus-antrian', methods=['GET', 'POST'])
def HapusAntrian():
    dataFound = AntrianPoli.query.filter(AntrianPoli.id).first()
    flash("Data berhasil di hapus", "success")
    db.session.delete(dataFound)
    db.session.commit()
    return redirect(url_for('antrianp.DataAntrian'))

## Antrian Sekarang
# poli umum
@antrianp.route('/antrian-sekarang')
def jsonUmumSekarang():
  query = db.session.query(AntrianPoli.no_antrianp).filter(AntrianPoli.id_poli == '1', cast(AntrianPoli.tgl_daftar, Date) == date.today(), AntrianPoli.status == '1').order_by(desc(AntrianPoli.tgl_update)).limit(1)
  rows = db.session.query(func.count()).select_from(query).scalar()

  if rows :
    response = []
    for row1 in query:
      response = row1.no_antrianp
    return jsonify(response)
  else:
    response = 0
    return jsonify(response)

## poli gigi
@antrianp.route('/json-gigi1')
def jsonGigiSekarang():
    query = db.session.query(AntrianPoli.no_antrianp).filter(AntrianPoli.id_poli == '2', cast(AntrianPoli.tgl_daftar, Date) == date.today(), AntrianPoli.status == '1').order_by(desc(AntrianPoli.tgl_update)).limit(1)
    rows = db.session.query(func.count()).select_from(query).scalar()

    if rows :
        response = []
        for row1 in query:
            response = row1.no_antrianp
        return jsonify(response)
    else:
        response = 0
        return jsonify(response)

### poli spesialis
@antrianp.route('/json-spesialis1')
def jsonSpesialisSekarang():
    query = db.session.query(AntrianPoli.no_antrianp).filter(AntrianPoli.id_poli == '3', cast(AntrianPoli.tgl_daftar, Date) == date.today(), AntrianPoli.status == '1').order_by(desc(AntrianPoli.tgl_update)).limit(1)
    rows = db.session.query(func.count()).select_from(query).scalar()

    if rows :
        response = []
        for row1 in query:
            response = row1.no_antrianp
        return jsonify(response)
    else:
        response = 0
        return jsonify(response) 

#### poli Kesehatan Ibu dan Anak
@antrianp.route('/json-kia1')
def jsonKiaSekarang():
    query = db.session.query(AntrianPoli.no_antrianp).filter(AntrianPoli.id_poli == '4', cast(AntrianPoli.tgl_daftar, Date) == date.today(), AntrianPoli.status == '1').order_by(desc(AntrianPoli.tgl_update)).limit(1)
    rows = db.session.query(func.count()).select_from(query).scalar()

    if rows :
        response = []
        for row1 in query:
            response = row1.no_antrianp
        return jsonify(response)
    else:
        response = 0
        return jsonify(response) 


# antrian selanjutnya
# Poli Umum
@antrianp.route('/antrian-selanjutnya')
def jsonUmumSelanjutnya():
  query = db.session.query(AntrianPoli.no_antrianp).filter(AntrianPoli.id_poli == '1', cast(
        AntrianPoli.tgl_daftar, Date) == date.today(), AntrianPoli.status == '0').order_by(asc(AntrianPoli.no_antrianp)).limit(1)
  rows = db.session.query(func.count()).select_from(query).scalar()

  if rows :
    response = []
    for row1 in query:
      response = row1.no_antrianp
    return jsonify(response)
  else:
    response = 0
    return jsonify(response)

## Poli Gigi
@antrianp.route('/json-gigi2')
def jsonGigiSelanjutnya():
  query = db.session.query(AntrianPoli.no_antrianp).filter(AntrianPoli.id_poli == '2', cast(
        AntrianPoli.tgl_daftar, Date) == date.today(), AntrianPoli.status == '0').order_by(asc(AntrianPoli.no_antrianp)).limit(1)
  rows = db.session.query(func.count()).select_from(query).scalar()

  if rows :
    response = []
    for row1 in query:
      response = row1.no_antrianp
    return jsonify(response)
  else:
    response = 0
    return jsonify(response)

# ## Poli Spesialis
@antrianp.route('/json-spesialis2')
def jsonSpesialisSelanjutnya():
  query = db.session.query(AntrianPoli.no_antrianp).filter(AntrianPoli.id_poli == '3', cast(
        AntrianPoli.tgl_daftar, Date) == date.today(), AntrianPoli.status == '0').order_by(asc(AntrianPoli.no_antrianp)).limit(1)
  rows = db.session.query(func.count()).select_from(query).scalar()

  if rows :
    response = []
    for row1 in query:
      response = row1.no_antrianp
    return jsonify(response)
  else:
    response = 0
    return jsonify(response)

# ## #Poli kesehatan ibu dan anak
@antrianp.route('/json-kia2')
def jsonKiaSelanjutnya():
  query = db.session.query(AntrianPoli.no_antrianp).filter(AntrianPoli.id_poli == '4', cast(
        AntrianPoli.tgl_daftar, Date) == date.today(), AntrianPoli.status == '0').order_by(asc(AntrianPoli.no_antrianp)).limit(1)
  rows = db.session.query(func.count()).select_from(query).scalar()

  if rows :
    response = []
    for row1 in query:
      response = row1.no_antrianp
    return jsonify(response)
  else:
    response = 0
    return jsonify(response)


# sis antrian
# Poli Umum
@antrianp.route('/sisa-antrian')
def jsonUmumSisa():
  query = db.session.query(func.count(AntrianPoli.id).label("jumlah")).filter(AntrianPoli.id_poli == '1', cast(AntrianPoli.tgl_daftar, Date)==date.today(), AntrianPoli.status =='0')

  response = []
  for row1 in query:
    response = row1['jumlah']
  return jsonify(response)

## Poli gigi
@antrianp.route('/json-gigi3')
def jsonGigiSisa():
  query = db.session.query(func.count(AntrianPoli.id).label("jumlah")).filter(AntrianPoli.id_poli == '2', cast(AntrianPoli.tgl_daftar, Date)==date.today(), AntrianPoli.status =='0')

  response = []
  for row1 in query:
    response = row1['jumlah']
  return jsonify(response)

# ## poli spesialis
@antrianp.route('/json-spesialis3')
def jsonSpesialisSisa():
  query = db.session.query(func.count(AntrianPoli.id).label("jumlah")).filter(AntrianPoli.id_poli == '3', cast(AntrianPoli.tgl_daftar, Date)==date.today(), AntrianPoli.status =='0')

  response = []
  for row1 in query:
    response = row1['jumlah']
  return jsonify(response)

# ### poli Kesehatan ibu & anak
@antrianp.route('/json-kia3')
def jsonKiaSisa():
  query = db.session.query(func.count(AntrianPoli.id).label("jumlah")).filter(AntrianPoli.id_poli == '4', cast(AntrianPoli.tgl_daftar, Date)==date.today(), AntrianPoli.status =='0')

  response = []
  for row1 in query:
    response = row1['jumlah']
  return jsonify(response)

# total antrian
#  poli umum
@antrianp.route('/jumlah-antrian')
def jsonUmumTotal():
  query = db.session.query(func.count(AntrianPoli.id).label("jumlah")).filter(AntrianPoli.id_poli == '1', cast(AntrianPoli.tgl_daftar, Date)==date.today())

  response = []
  for row1 in query:
    response = row1['jumlah']
  return jsonify(response)

# # Poli Gigi
@antrianp.route('/json-gigi4')
def jsonGigiTotal():
  query = db.session.query(func.count(AntrianPoli.id).label("jumlah")).filter(AntrianPoli.id_poli == '2', cast(AntrianPoli.tgl_daftar, Date)==date.today())

  response = []
  for row1 in query:
    response = row1['jumlah']
  return jsonify(response)

# ## Poli spesialis
@antrianp.route('/json-spesialis4')
def jsonSpesialisTotal():
  query = db.session.query(func.count(AntrianPoli.id).label("jumlah")).filter(AntrianPoli.id_poli == '3', cast(AntrianPoli.tgl_daftar, Date)==date.today())

  response = []
  for row1 in query:
    response = row1['jumlah']
  return jsonify(response)

# ### Poli Kesehatan Ibu dan Anak
@antrianp.route('/json-kia4')
def jsonKiaTotal():
  query = db.session.query(func.count(AntrianPoli.id).label("jumlah")).filter(AntrianPoli.id_poli == '4', cast(AntrianPoli.tgl_daftar, Date)==date.today())

  response = []
  for row1 in query:
    response = row1['jumlah']
  return jsonify(response)