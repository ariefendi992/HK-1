from app import app
from datetime import datetime, date

@app.template_filter('dateformat')
def dateformat(value, format="%d-%m-%Y"):
  return value.strftime(format)