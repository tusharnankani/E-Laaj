from flask import Blueprint, render_template

bp = Blueprint("patient", __name__, url_prefix="/patient")

@bp.route("/")
def patient():
  return render_template("patient/patient.html")