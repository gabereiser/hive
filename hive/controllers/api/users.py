from flask import Blueprint, jsonify

route = Blueprint("users", __name__, url_prefix='/api')