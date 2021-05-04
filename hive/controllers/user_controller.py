import hashlib
from uuid import UUID

from flask import Blueprint, render_template, jsonify, flash, request, abort, redirect  # noqa
from flask_login import login_required, current_user

from hive.models import User

route = Blueprint("profile", __name__)


@route.route("/me", methods=['GET', 'POST'])
@login_required
def profile():
    if request.method == 'POST' and current_user.is_active():
        user = current_user
        (error, success) = user.update_profile(request.form)
        if success is True:
            user.save()
            flash("Success!", "success")
        else:
            flash(error, "error")
    return render_template("profile.html", user=current_user)


@route.route("/users/list", defaults={'page': 1})
@route.route("/users/list/<int:page>")
@login_required
def user_list(page: int = 0):
    limit = request.args.get("limit", 50)
    offset = limit*(page-1)
    users = User.query.order_by(User.id).slice(offset, offset+limit)
    return render_template("user_list.html", users=users)


@route.route("/users/<uuid:user_id>")
@login_required
def user_view(user_id: UUID):
    user = User.query.filter_by(user_id=user_id).first()
    if user is not None:
        return render_template("user_details.html", user=user)
    else:
        abort(404)
