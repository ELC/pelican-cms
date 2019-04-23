import os
from flask import Flask
import pelican_cms.config as config

__version__ = "0.0.2"

def create_app():
    app = Flask(__name__)

    app.config.from_object(config)

    from pelican_cms.models import db, ma
    db.init_app(app)
    ma.init_app(app)

    from pelican_cms.views import home
    app.register_blueprint(home)

    return app