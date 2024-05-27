from flask import request
from flask.views import MethodView
from flask_smorest import Blueprint
from schemas_test.store import AddProductSchema, ItemSchema, UserDetailsSchema

blp = Blueprint("Stores", __name__, description="Operations on stores")


products = [{"name": "T-Shirt", "price": "10 euros"},
            {"name": "Dhoti", "price": "15 euros"},
            {"name": "Shaluwa", "price": "5 euros"}]


@blp.route("/store")
class Store(MethodView):
    def get(self):
        return {"message": f"Hello", "products": products}, 200


@blp.route("/store/addproduct")  # request body
class Product(MethodView):
    @blp.arguments(AddProductSchema)
    def post(self, payload):
        payload = request.get_json()
        user = payload["user"]
        name = payload["name"]
        price = payload["price"]
        print(name, price)
        products.append({"name": name, "price": price})
        return products, 201


# request body and url params
@blp.route("/greet/<string:name>")
class Greet(MethodView):
    @blp.arguments(UserDetailsSchema)
    def post(self, user_data, name):
        user_data = request.get_json()
        user = user_data["user"]
        resp = {"greetings": f"Hey {name}!!",
                "user": user,
                }
        return resp, 200

# request body and url params and query params


@blp.route("/product/<string:name>")
class Greet(MethodView):
    @blp.arguments(UserDetailsSchema)
    @blp.arguments(ItemSchema, location="query")
    def get(self, user_data, query_search, name):
        user_data = request.get_json()
        user = user_data["user"]
        item = query_search["item"]
        prod = list(filter(
            lambda prod: prod["name"].lower() == item.lower(), products))
        resp = {"greetings": f"Hey {name}!!",
                "search": item,
                "user": user,
                "data": prod[0] if len(prod) else f"not found"}
        return resp, 200
