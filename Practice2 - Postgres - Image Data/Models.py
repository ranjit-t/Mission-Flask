from db import db


class ProductModel(db.Model):
    __tablename__ = "products"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    price = db.Column(db.Float, nullable=False)
    description = db.Column(db.String, nullable=False)
    image_name = db.Column(db.String, nullable=True)
    image_data = db.Column(db.LargeBinary, nullable=True)
