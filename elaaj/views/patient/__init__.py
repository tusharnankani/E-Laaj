from flask import Blueprint, render_template, g, redirect, url_for, flash, request
import elaaj.models.db as db
from werkzeug.security import check_password_hash

bp = Blueprint("patient", __name__, url_prefix="/patient")

@bp.route("/")
def patient():
  if(g.get("user") is None):
    return redirect(url_for("patient.login"))
  return render_template("patient/patient.html")

@bp.route("/login", methods=["GET", "POST"])
def login():
  if(request.method == "POST"):
    phone = request.form["phone"]
    password = request.form["password"]
    if(not phone or not password):
      flash("Please, provide phone and password", "error")
    else:
      user = db.Patients.query.filter_by(phone=phone).first()
      if(not check_password_hash(user.password, password)):
        flash("Incorrect phone number or password", "error")
      else:
        g.user = user
        return redirect(url_for("patient.patient"))
  return render_template("patient/login.html")
  