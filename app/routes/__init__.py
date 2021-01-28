import functools

from flask import redirect, session, url_for, g


def login_required(view):
  @functools.wraps(view)
  def wrapped_view(**kwargs):
    if session.get('user_id') is None:
      return redirect(url_for('auth.login'))

    return view(**kwargs)

  return wrapped_view
