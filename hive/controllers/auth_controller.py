import hashlib

from flask import Blueprint, render_template, jsonify, flash, request, abort, redirect, url_for  # noqa
from flask_login import current_user, login_user, login_required, logout_user

from hive.models import User

route = Blueprint("auth", __name__)


@route.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    if request.method == 'POST':
        # Login and validate the user.
        username = str(request.form['username'])  # encode username to str
        hashword = hashlib.sha256(str(request.form['password']).encode('utf8')).hexdigest()
        remember = bool(request.form.get("remember", default=False))
        user = User.query.filter_by(username=username, password_hash=hashword).first()  # user exist?
        if user is None:
            return {
                'status': 'error',
                'errors': [
                    "Invalid username/password."
                ]
            }
        else:
            login_user(user, remember=remember)

        next = request.args.get('next')
        return {
            'status': 'ok',
            'redirect': next or url_for('home.home')
        }
    return render_template('login.html')


@route.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for("home.home"))
