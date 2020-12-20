from flask import Blueprint, jsonify, abort, request
from elaaj.models.db import db, PhoneCodes
from datetime import datetime, timedelta

bp = Blueprint("api", __name__, url_prefix="/api")

@bp.route("/phoneCheck")
def phoneCheck():
  phone = request.args.get("phone")
  otp = request.args.get("otp")
  try:
    phone=int(phone)
  except:
    return jsonify(isCorrect=False)

  if(not phone or not otp):
    return jsonify(isCorrect=False)
  phoneDb = PhoneCodes.query.filter_by(phone=phone).first()
  if(phoneDb and phoneDb.otp == otp and datetime.fromtimestamp(phoneDb.expire) > datetime.now() """not expired"""):
    return jsonify(isCorrect=True)
  return jsonify(isCorrect=False)
    

@bp.route("/<string:apiType>")
def apiDbGetter(apiType):
  if(not db.engine.dialect.has_table(db.engine, apiType)):
    abort(404)
  dbRes = db.session.execute("SELECT * FROM '" + apiType + "'");
  result = []
  for row in dbRes:
    result.append(dict(row.items()))
  return jsonify(result)