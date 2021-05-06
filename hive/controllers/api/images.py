from flask import Blueprint, jsonify

route = Blueprint("images", __name__, url_prefix='/api')