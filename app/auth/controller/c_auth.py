from flask_login.utils import login_required
from app import db
from app.auth.form.f_login import LoginForm
from app.auth.form.f_register import RegisTerForm
from app.admin.model.model_admin import *
from flask import Blueprint, render_template, redirect, request, url_for, flash, session, abort
from flask_login import login_user, logout_user, current_user
from urllib.parse import urlparse, urljoin

auth = Blueprint('auth', __name__, static_folder='static',
                template_folder='../templates/auth')

#variabel global
def is_safe_url(target):
    ref_url = urlparse(request.host_url)
    test_url = urlparse(urljoin(request.host_url, target))

    return test_url.scheme in ('http', 'https') and ref_url.netloc == test_url.netloc
  

@auth.route('/register', methods=['GET', 'POST'])
def Register():
    form = RegisTerForm()
    if request.method == 'POST' and form.validate:
        nama = form.nama.data
        username = form.username.data
        telp = form.telp.data
        password = form.password.data
        role_id = form.role.data
        flash('Akun berhasil dibuat. Silahkan Login.', 'info')
        query = User(nama=nama, username=username, telp=telp,
                    password=password, role_id=role_id)
        db.session.add(query)
        db.session.commit()

    return render_template('register.html', form=form)

@auth.route('/', methods=['GET', 'POST'])
def Login():
    form = LoginForm(request.form)
    # session.permanent = None
    if request.method == 'POST' and form.validate_on_submit:
        user = User.query.filter_by(username=form.username.data).first()
        if not user:
            flash(message='Username Salah.!', category='danger')
        
        if user and user.checkPassword(form.password.data):
            login_user(user, remember=form.remember.data)
            if 'next' in session and session['next']:
                if is_safe_url(session['next']):
                  return redirect(session['next'])
            if current_user.role_id == 1:
              flash(message='Login Sukses, Selamat datang {}'.format(current_user.nama), category='success')
              return redirect(url_for('admin.Index'))
            elif current_user.role_id == 3:
              flash(message='Login Sukses, Selamat datang {}'.format(current_user.nama), category='success')
              return redirect(url_for('pasiens.pasienDashboard'))
        else:
            flash(message='Password Salah.!', category='danger')
        
    session['next'] = request.args.get('next')
    return render_template('login.html', form=form)


@auth.get('/logout')
@login_required
def Logout():
  # logout_user()
  logout_user()  
  wait_time = 1000
  redirect_url = (url_for('auth.Login'))

    
  seconds = 3000
    # flash("Logout Sukses", "")

# if the validation is successful, forward to redirect page, wait 3 seconds, redirect to specified url
  return f'''
  <html>
  <head>
    <link href="https://fonts.googleapis.com/css2?family=Nunito:wght@300;400;600;700;800&display=swap" rel="stylesheet">
    <style>
    body {{
      font-family: 'Nunito Sans', sans-serif;
      font-size : 16px;
      font-weight : 600;
    }}
    #timer {{
      border: none;
      border-radius: 10px 0 10px 0;
    }}
    </style>
  </head>
  <body>
  <div style="margin: 20px auto;  width: 35%;">
      <p id="timer" style="margin: auto; width: 100%; background: #57CAEB; color:white; padding: 12px; text-align: center">
        Logout Sukses... (3) 
      </p>
  </div>
    <script>
    </script>
    <script>
      var timerElement = document.getElementById('timer');
      
    
      var timerCounter = {seconds} / 1000
        
      var timer = setInterval(function() {{
        if (timerCounter <= 1) {{
          window.location='{ redirect_url }'
          clearInterval(timer)          
        }}
        timerCounter = timerCounter - 1;
        timerElement.innerHTML = 'Logout Sukses... ' + '('+timerCounter+')';
        if (timerCounter === 0) {{
          timerElement.innerHTML = 'redirect to..'
        }}
        }}, { wait_time });
      </script>
  </body>
  </html>
  '''

  # flash("Anda telah keluar.", "info")

