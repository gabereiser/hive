from flask import Blueprint, render_template, jsonify, flash, request, abort, redirect, url_for  # noqa
from flask_login import current_user, login_user, login_required, logout_user

from hive.models import User

route = Blueprint("auth", __name__)


@route.route('/login', methods=['GET', 'POST'])
def login():
    error = ""
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
                error = "Invalid username or password."
                flash(error, category="error")
        else:
            error = "Invalid username or password."
            flash(error, category="error")
        if error == "":
            next = request.args.get('next')
            redirect(next or url_for('home.home'))
        else:
            return render_template('login.html', error=error), 403
    return render_template('login.html', error=error)


@route.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for("home.home"))
