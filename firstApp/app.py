import os
from flask import Flask
from flask_smorest import Api

from db import db
# import models

from resources.store import blp as StoreBluePrint
from resources.item import blp as ItemBluePrint


from flask_cors import CORS


def create_app(db_uri=None):
    app = Flask(__name__)
    cors = CORS(app)
    app.config['CORS_HEADERS'] = 'Content-Type'

    app.config["API_TITLE"] = "My API"
    app.config["API_VERSION"] = "v1"
    app.config["OPENAPI_VERSION"] = "3.0.2"
    app.config["OPENAPI_URL_PREFIX"] = "/"
    app.config["OPENAPI_SWAGGER_UI_PATH"] = "/doc"
    app.config["OPENAPI_SWAGGER_UI_URL"] = "https://cdn.jsdelivr.net/npm/swagger-ui-dist/"
    app.config["SQLALCHEMY_DATABASE_URI"] = db_uri or os.getenv(
        "DATABASE_URI", "sqlite:///data.db")  # conncting to database
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False  # audit trail
    db.init_app(app)

    api = Api(app)

    with app.app_context():
        db.create_all()

    api.register_blueprint(StoreBluePrint)
    api.register_blueprint(ItemBluePrint)

    return app
