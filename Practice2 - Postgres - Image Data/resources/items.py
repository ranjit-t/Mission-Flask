

from flask import jsonify, request
from flask_smorest import Blueprint
from flask.views import MethodView
import json
from sqlalchemy.orm import defer

from db import db
from Models import ProductModel
from schemas import PlainProductSchema

productsBlueprint = Blueprint("Products", __name__)


@productsBlueprint.route("/addProduct")
class AddProduct(MethodView):
    @productsBlueprint.response(201, PlainProductSchema)
    def post(self):
        data = request.form.get("data")
        if data:
            try:
                data = json.loads(data)
            except json.JSONDecodeError:
                return jsonify({"error": "Invalid JSON data"}), 400
        name = data["name"]
        price = data["price"]
        description = data["description"]
        image_binary = request.files.get('image')
        image_data = None
        image_name = None
        if image_binary:
            image_name = image_binary.filename
            image_data = image_binary.read()  # Read the file as binary data

        product_data = {
            'name': name,
            'price': float(price),
            'description': description,
            "image_name": image_name,
            'image_data': image_data
        }

        product = ProductModel(**product_data)
        db.session.add(product)
        db.session.commit()
        return product_data, 201


@productsBlueprint.route("/getProducts")
class GetProducts(MethodView):
    @productsBlueprint.response(200, PlainProductSchema(many=True))
    def get(self):
        # return ProductModel.query.all()
        return ProductModel.query.options(defer(ProductModel.image_data)).all()
