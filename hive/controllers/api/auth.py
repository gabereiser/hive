from logging import getLogger

from flask import Blueprint, jsonify, request, url_for, redirect
from flask_login import login_user

from hive.models import User

route = Blueprint("auth", __name__, url_prefix='/api/auth')

log = getLogger(__name__)


@route.route("/authorize", methods=["POST", "PUT"])
def authorize():
    pass


@route.route("/token", methods=["POST", "PUT"])
def token():
    pass


@route.route("/refresh", methods=["GET", "POST", "PUT"])
def refresh():
    pass


@route.route("/login", methods=["POST"])
def login():
    log.info("Login API request made.")

    error: str = ""
    if request.method == 'POST':
        # Login and validate the user.
        username: str = str(request.form.get('username'))  # encode username to str
        password: str = str(request.form.get('password'))
        remember: bool = bool(request.form.get("remember", default=False))
        user = User.query.filter_by(username=username).first()  # user exist?
        if user is not None:
            if user.verify_password(password):
                login_user(user, remember=remember)
                user.refresh()
            else:
                error = "Invalid username or password."
        else:
            error = "Invalid username or password."
        if error == "":
            return jsonify({'status': 'ok', 'error': None}), 201
        else:
            return jsonify({'status': 'error', 'error': error})
    return redirect(url_for("auth_controller.login")), 302
