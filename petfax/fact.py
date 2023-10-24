from flask import Blueprint,render_template

bp = Blueprint('fact',__name__, url_prefix='/facts')


@bp.route('/')
def index():
    return 'WELCOME TO /FACT PAGE!!!'

@bp.route('/new')
def form():
    return render_template('form.html' )