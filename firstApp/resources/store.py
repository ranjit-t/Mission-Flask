from flask import request
from flask.views import MethodView
from flask_smorest import Blueprint, abort
from models import StoreModel
from schemas import GetStoreSchema, StoreSchema
from db import db
from sqlalchemy.exc import SQLAlchemyError, IntegrityError
# from schemas_test.store import AddProductSchema, ItemSchema, UserDetailsSchema

blp = Blueprint("Stores", __name__, description="Operations on stores")


@blp.route("/addstore")
class AddStore(MethodView):
    @blp.arguments(StoreSchema)
    @blp.response(201, StoreSchema)
    def post(self, store_data):
        store = StoreModel(**store_data)
        try:
            db.session.add(store)
            db.session.commit()
        except IntegrityError:
            abort(400, message="Store already exists")
        except SQLAlchemyError:
            abort(500, message="Error occured while storing")
        return store


@blp.route("/storeslist")
class GetStores(MethodView):
    @blp.response(200, StoreSchema(many=True))
    def get(self):
        stores = StoreModel.query.all()
        return stores


@blp.route("/store")
class GetStores(MethodView):
    @blp.arguments(GetStoreSchema)
    @blp.response(200, StoreSchema)
    def get(self, store):
        store = StoreModel.query.get_or_404(store)
        return store
