from flask import render_template, Blueprint

site = Blueprint('site', __name__, template_folder='../templates', static_folder='static')

@site.route('/')
def Index():
  return render_template('landing.html')

@site.route('/temp')
def Temp():
  return render_template('src/index.html')