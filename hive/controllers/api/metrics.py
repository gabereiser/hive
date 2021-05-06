from flask import Blueprint, jsonify

route = Blueprint("metrics", __name__, url_prefix='/api')


@route.route('/status')
def status():
    return jsonify({'status': 'ok'})
