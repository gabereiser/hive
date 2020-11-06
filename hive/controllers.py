from flask import Blueprint, render_template, jsonify, flash, request, abort, redirect # noqa
from flask import url_for, send_from_directory
from flask_login import login_user, logout_user, login_required, current_user
import logging
import hashlib
import os
from datetime import datetime
from .models import User
from .docker import Docker

logger = logging.getLogger("controllers")
route = Blueprint("home", __name__)


@route.route("/status")
def status():
    return jsonify({"status": "ok"})


@route.route("/")
@login_required
def home():
    return render_template("index.html")


@route.route("/profile", methods=['GET', 'POST'])
@login_required
def profile():
    if request.method == 'POST' and current_user.is_active():
        user = current_user
        user.password_hash = hashlib.sha256(str(request.form['password']).encode('utf8')).hexdigest()
        user.save()
    return render_template("profile.html")


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


@route.route("/nodes/list")
@login_required
def docker_nodes_list():
    return Docker.node_list()


@route.route("/nodes/<str:id>")
@login_required
def docker_nodes_get(id):
    return Docker.node_get(id)
