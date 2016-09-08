# encoding='utf-8'

from flask import render_template
from flask import Blueprint
from flask import request
from flask import redirect
from flask import url_for

from models import User

from utils import log


main = Blueprint('user', __name__)


@main.route('/')
def index():
    return render_template('index.html')


@main.route('/user/login', methods=['POST'])
def login():
    form = request.form
    u = User(form)
    log('login u', u)
    if u.validate_login():
        return redirect(url_for('todo.index'))