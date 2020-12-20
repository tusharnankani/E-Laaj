from flask import Blueprint

bp = Blueprint("index", __name__, url_prefix="/")

@bp.route("/")
def index():
  return "test"