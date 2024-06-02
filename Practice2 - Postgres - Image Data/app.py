from flask import Flask
from flask_cors import CORS
from flask_smorest import Api
from db import db
from resources.items import productsBlueprint

app = Flask(__name__)
app.config['CORS_HEADERS'] = 'Content-Type'
app.config["API_TITLE"] = "Products API"
app.config["API_VERSION"] = "V1"
app.config["OPENAPI_VERSION"] = "3.0.2"
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://postgres:Postgres123@localhost/Test"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
cors = CORS(app)
api = Api(app)
db.init_app(app)

api.register_blueprint(productsBlueprint)

with app.app_context():
    db.create_all()
