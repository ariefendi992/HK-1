from flask_migrate import current
from app import db
from flask import Blueprint, render_template
from flask_login import login_required, current_user
from app.admin.model.model_pasien import Pasien, Gender
from sqlalchemy import desc
from app.helper.decoratorPasien import pasienRequired

ps = Blueprint('pasiens', __name__, static_folder='static', template_folder='../templates/pasiens')

@ps.route('/')
@login_required
@pasienRequired
def dataPasien():
    # if not current_user.role.tipe_akun == 'pasien':
    #     return 'Modul halaman ini tidak ditemukan {}'.format(current_user.id)
    # else:
        query = Pasien.query.join(Gender).filter(Pasien.id_user == current_user.id).order_by(desc(Pasien.id)).all()
        return render_template('pasiens.html', query=query)
    
