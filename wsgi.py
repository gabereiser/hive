from flask import jsonify
from flask_swagger import swagger

from hive.application import Application

app = Application()
app.init()


@app.route("/api/spec")
def spec():
    return jsonify(swagger(app))


def main():
    app.run(host='0.0.0.0', port=8080)


def create_app():
    app.init()
    return app


if __name__ == "__main__":
    main()
