from flask import request
from flask.views import MethodView
from flask_smorest import Blueprint, abort
from models import ItemModel
from models.store import StoreModel
from schemas import ItemSchema
from db import db
from sqlalchemy.exc import SQLAlchemyError, IntegrityError

blp = Blueprint("Items", __name__, description="Operations on Items")


@blp.route("/additem")
class AddStore(MethodView):
    @blp.arguments(ItemSchema)
    @blp.response(201, ItemSchema)
    def post(self, item_data):
        item = ItemModel(**item_data)
        try:
            db.session.add(item)
            db.session.commit()
        except IntegrityError:
            abort(400, message="item already exists")
        except SQLAlchemyError:
            abort(500, message="Error occured while storing")
        return item


@blp.route("/itemslist")
class GetStores(MethodView):
    @blp.response(200, ItemSchema(many=True))
    def get(self):
        items = ItemModel.query.all()
        return items


# @blp.route("/store")
# class GetStores(MethodView):
#     @blp.arguments(GetStoreSchema)
#     @blp.response(200, ItemSchema)
#     def get(self, store):
#         store = StoreModel.query.get_or_404(store)
#         return store
