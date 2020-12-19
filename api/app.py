import os
from flask import Flask, jsonify

app = Flask(__name__, instance_relative_config=True)

try:
  os.makedirs(app.instance_path)
  os.mknod(app.instance_path + "/settings.py")
except OSError:
  pass

app.config.from_pyfile("settings.py")


@app.route("/api")
def index():
  return jsonify()

if(__name__ == "__main__"):
  app.run(debug=True)