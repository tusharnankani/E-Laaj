import os 
from flask import Flask

def create_app():
  app = Flask(__name__, instance_relative_config=True)
  app.jinja_env.add_extension("jinja2.ext.loopcontrols")

  app.config.from_pyfile("config.py", silent=True)

  try:
      os.makedirs(app.instance_path)
  except OSError:
      pass

  with app.app_context():
    from elaaj.models import db
    db.db.init_app(app)

    from elaaj.views import index, api
    app.register_blueprint(index.bp)
    app.register_blueprint(api.bp)

  return app