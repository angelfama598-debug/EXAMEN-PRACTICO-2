from flask import Blueprint, render_template

bp_core = Blueprint('core', __name__, template_folder='templates')

@bp_core.route('/')
def index():
    return render_template('core/index.html')