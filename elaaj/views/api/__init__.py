from flask import Blueprint, jsonify, abort, request
from elaaj.models.db import db, PhoneCodes, Patients, Doctors
from datetime import datetime, timedelta
from random import randint

bp = Blueprint("api", __name__, url_prefix="/api")

@bp.route("/phoneCheck")
def phoneCheck():
  phone = request.args.get("phone")
  try:
    phone=int(phone)
  except:
    return jsonify(phoneExists=None)
  if(not PhoneCodes.query.filter_by(phone=phone).first()):
    return jsonify(phoneExists=False)
  return jsonify(phoneExists=True)

@bp.route("/otpCheck")
def otpCheck():
  phone = request.args.get("phone")
  otp = request.args.get("otp")
  try:
    phone=int(phone)
  except:
    return jsonify(isCorrect=False)

  if(not phone or not otp):
    return jsonify(isCorrect=False)
  phoneDb = PhoneCodes.query.filter_by(phone=phone).first()
  if(phoneDb and phoneDb.otp == otp and datetime.fromtimestamp(phoneDb.expire) > datetime.now()):
    return jsonify(isCorrect=True)
  return jsonify(isCorrect=False)

@bp.route("/createOtp", methods=["POST"])
def createOtp():
  phone = request.json.get("phone")
  if(not phone):
    return jsonify(error="Provide a phone number!")
  otp = int("".join([str(randint(0, 9)) for _ in range(0, 4)]))
  if(Patients.query.filter_by(phone=phone) is not None or Doctors.query.filter_by(phone=phone) is not None):
    return jsonify(error="This phone number is already registerd!")
  db.session.add(PhoneCodes(phone=phone, otp=otp, expire=datetime.timestamp(datetime.now()+timedelta(minutes=3))))
  db.session.commit()
  db.session.remove()
  return jsonify(otp=otp)
    
@bp.route("/<string:apiType>")
def apiDbGetter(apiType):
  if(not db.engine.dialect.has_table(db.engine, apiType)):
    abort(404)
  dbRes = db.session.execute("SELECT * FROM '" + apiType + "'");
  result = []
  for row in dbRes:
    result.append(dict(row.items()))
  return jsonify(result)