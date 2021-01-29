from flask import Blueprint, render_template

from . import login_required


views_bp = Blueprint('views', __name__)

@views_bp.route('/temp-dashboard', methods=['GET', 'POST'])
@login_required
def temp_dashboard():

  return render_template('views.temp-dashboard.html')
