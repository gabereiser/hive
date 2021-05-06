from flask import Blueprint, jsonify

route = Blueprint("dns", __name__, url_prefix='/api')