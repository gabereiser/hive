from flask import Blueprint, render_template, jsonify, flash, request, abort, redirect  # noqa
from flask_login import login_required

route = Blueprint("home", __name__)


@route.route("/api/status")
def status():
    return jsonify({"status": "ok"})


@route.route("/")
@login_required
def home():
    return render_template("views/index.html")
