from flask.views import MethodView
from flask_smorest import Blueprint, abort
from sqlalchemy.exc import SQLAlchemyError, IntegrityError
from models.products import ProductModel
from models.tag import TagModel
from schema.storesproducts import ProductSchema
from sqlalchemy.orm import defer

from db import db


product_blueprint = Blueprint(
    "Products", __name__, description="Operations on Products")


@product_blueprint.route("/additem")
class AddProduct(MethodView):
    @product_blueprint.arguments(ProductSchema)
    @product_blueprint.response(201, ProductSchema)
    def post(self, product_data):
        try:
            tag_name = product_data.get("tag")
            if tag_name:
                del product_data["tag"]
            product = ProductModel(**product_data)
            db.session.add(product)
            if tag_name:
                tag = db.session.query(TagModel).filter_by(
                    tag=tag_name).first()
                if not tag:
                    tag = TagModel(tag=tag_name)
                    db.session.add(tag)
                product.tags.append(tag)
            db.session.commit()
            return product
        except IntegrityError:
            abort(400, message="Product already exists")
        except SQLAlchemyError:
            abort(500, message="Error occured while storing")


@product_blueprint.route("/itemslist")
class GetStores(MethodView):
    @product_blueprint.response(200, ProductSchema(many=True))
    def get(self):
        stores = ProductModel.query.all()
        return stores
