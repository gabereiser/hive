from flask import Blueprint, render_template, jsonify, flash, request, abort, redirect, url_for  # noqa
from flask_login import current_user, login_user, login_required, logout_user

from hive.models import User

route = Blueprint("auth_controller", __name__)


@route.route('/login', methods=['GET', 'POST'])
def login():
    error = False
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    if request.method == 'POST':
        # Login and validate the user.
        username = str(request.form.get('username'))  # encode username to str
        password = str(request.form.get('password'))
        remember = bool(request.form.get("remember", default=False))
        user = User.query.filter_by(username=username).first()  # user exist?
        if user is not None:
            if user.verify_password(password):
                login_user(user, remember=remember)
                user.refresh()
            else:
                error = True
                flash("Invalid username and/or password.", category="error")
        else:
            error = True
            flash("Invalid username and/or password.", category="error")
        if not error:
            next = request.args.get('next')
            redirect(next or url_for('home.home'))

    return render_template('views/accounts/login.html')


@route.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for("home.home"))
