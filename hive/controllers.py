from flask import Blueprint, render_template, jsonify, flash, request, abort, redirect # noqa
from flask import url_for
from flask_login import login_user, logout_user, login_required, current_user
import logging
import hashlib
from datetime import datetime
from models import User

logger = logging.getLogger("controllers")
route = Blueprint("home", __name__)


@route.route("/heartbeat")
def heartbeat():
    return jsonify({"status": "ok"})


@route.route("/")
@route.route("/index")
@login_required
def home():
    return render_template("index.html")


@route.route("/profile", methods=['GET', 'POST'])
@login_required
def profile():
    if request.method == 'POST' and current_user.is_active():
        user = current_user
        user.password_hash = hashlib.sha256(request.form['password'])
        user.save()
    return render_template("profile.html")


@route.route('/login', methods=['GET', 'POST'])
def login():

    if current_user.is_authenticated:
        return redirect(url_for('index'))
    if request.method == 'POST':
        # Login and validate the user.
        username = str(request.form['username'])
        hashword = hashlib.sha256(str(request.form['password']).encode('utf8')).hexdigest()
        remember = bool(request.form.get("remember", default=False))
        user = User.query.filter_by(username=username, password_hash=hashword).first()
        print("{} {} {}".format(username, request.form['password'], remember))
        if user is None:
            flash('Invalid username and or password.')
            return redirect(url_for('home.login'))
        if user:
            user.save()
            login_user(user, remember=remember)

        flash('Logged in successfully.')

        next = request.args.get('next')

        return redirect(next or url_for('home.home'))
    return render_template('login.html')


@route.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for("index"))


@route.route("/forgot-password")
def forgot_password():
    return render_template('forgot-password.html')