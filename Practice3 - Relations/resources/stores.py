from flask.views import MethodView
from flask_smorest import Blueprint, abort
from sqlalchemy.exc import SQLAlchemyError, IntegrityError
from models.stores import StoreModel


from db import db
from schema.storesproducts import StoreSchema


store_blueprint = Blueprint(
    "Stores", __name__, description="Operations on Stores")


@store_blueprint.route("/addstore")
class Addstore(MethodView):
    @store_blueprint.arguments(StoreSchema)
    @store_blueprint.response(201, StoreSchema)
    def post(self, store_data):
        try:
            store = StoreModel(**store_data)
            db.session.add(store)
            db.session.commit()
            return store
        except IntegrityError:
            abort(400, message="Store already exists")
        except SQLAlchemyError:
            abort(500, message="Error occured while storing")


@store_blueprint.route("/storeslist")
class GetStores(MethodView):
    @store_blueprint.response(200, StoreSchema(many=True))
    def get(self):
        stores = StoreModel.query.all()
        return stores
