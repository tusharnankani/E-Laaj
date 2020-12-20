from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Doctors(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.Text, nullable=False)
  surname = db.Column(db.Text, nullable=False)
  age = db.Column(db.Integer, nullable=False)
  speciality = db.Column(db.Text, nullable=False)
  phone = db.Column(db.Integer, nullable=False)
  licenseId = db.Column(db.Integer, nullable=False)
  yoe = db.Column(db.Integer, nullable=False)
  location = db.Column(db.Text, nullable=False)

class Patients(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.Text, nullable=False)
  surname = db.Column(db.Text, nullable=False)
  age = db.Column(db.Integer, nullable=False)
  phone = db.Column(db.Integer, nullable=False)

class PhoneCodes(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  phone = db.Column(db.Integer, nullable=False)
  otp = db.Column(db.Text, nullable=False)
  expire = db.Column(db.Integer, nullable=False)
  

def init_db():
  db.drop_all()
  db.create_all()