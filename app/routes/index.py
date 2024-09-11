from flask import Blueprint, render_template

bp = Blueprint('index', __name__, url_prefix='/')

@bp.route('/', methods=['GET'])
def index():
    return render_template('index.html')


@bp.route("/contacts",  methods=['GET'])
def contacts():
    return render_template('contacts.html')