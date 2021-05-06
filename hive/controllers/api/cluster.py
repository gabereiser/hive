from flask import Blueprint, jsonify

route = Blueprint("cluster", __name__, url_prefix='/api')