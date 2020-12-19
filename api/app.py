from flask import Flask, jsonify

app = Flask(__name__, instance_relative_config=True)
app.config.from_pyfile("settings.py")

from . import db
db.db.init_app(app)

@app.route("/api")
def index():
  return jsonify()

if(__name__ == "__main__"):
  app.run(debug=True)