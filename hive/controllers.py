from flask import Blueprint, render_template
import logging

logger = logging.getLogger("controllers")
app = Blueprint("home", __name__)


@app.route("/")
def home():
    logger.info("/ called")
    return render_template("index.html")
