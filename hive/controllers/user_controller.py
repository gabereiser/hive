import hashlib

from flask import Blueprint, render_template, jsonify, flash, request, abort, redirect  # noqa
from flask_login import login_required, current_user

from hive.models import User

route = Blueprint("profile", __name__)


@route.route("/me/profile", methods=['GET', 'POST'])
@login_required
def profile():
    if request.method == 'POST' and current_user.is_active():
        user = current_user
        user.password_hash = hashlib.sha256(str(request.form['password']).encode('utf8')).hexdigest()
        user.save()
    return render_template("profile.html")


@route.route("/users/list")
@route.route("/users/list/<page>")
@login_required
def user_list(page: int = 0):
    users = User.query.order_by(User.id).slice(page, page+50)
    return render_template("user_list.html", users=users)
