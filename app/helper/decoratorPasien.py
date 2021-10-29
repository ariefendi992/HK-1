from flask import abort
from flask_login import current_user
from functools import wraps

def pasienRequired(f):
  @wraps(f)
  def wrapper(*args, **kwargs):
    if not current_user.role_id == 3:
      abort(403)
    return f(*args, **kwargs)
  return wrapper