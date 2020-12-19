import os
from flask import Flask, jsonify, abort
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__, instance_relative_config=True)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///../database.db" 

try:
  os.makedirs(app.instance_path)
  os.mknod(app.instance_path + "/settings.py")
except OSError:
  pass

db = SQLAlchemy(app)
app.config.from_pyfile("settings.py")


@app.route("/api/<string:apiType>")
def patients(apiType):
  print(app.config["TEST"])
  if(not db.engine.dialect.has_table(db.engine, apiType)):
    abort(404)
  dbRes = db.session.execute("SELECT * FROM '" + apiType + "'");
  result = []
  for row in dbRes:
    result.append(dict(row.items()))
  return jsonify(result)

if(__name__ == "__main__"):
  app.run(debug=True)