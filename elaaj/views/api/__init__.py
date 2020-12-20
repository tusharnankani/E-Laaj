from flask import Blueprint, jsonify, abort
from elaaj.models.db import db

bp = Blueprint("api", __name__, url_prefix="/api")

@bp.route("/<string:apiType>")
def apiDbGetter(apiType):
  if(not db.engine.dialect.has_table(db.engine, apiType)):
    abort(404)
  dbRes = db.session.execute("SELECT * FROM '" + apiType + "'");
  result = []
  for row in dbRes:
    result.append(dict(row.items()))
  return jsonify(result)