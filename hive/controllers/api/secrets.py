from flask import Blueprint, jsonify

route = Blueprint("secrets", __name__, url_prefix='/api')