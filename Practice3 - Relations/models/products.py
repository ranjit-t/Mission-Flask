from db import db


class ProductModel(db.Model):
    __tablename__ = "products"
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), unique=True, nullable=False)
    price = db.Column(db.Float, nullable=False)
    store_id = db.Column(db.Integer, db.ForeignKey(
        "stores.id"), nullable=False)
    store = db.relationship("StoreModel", back_populates="products")
    tags = db.relationship(
        "TagModel", back_populates="products", secondary="tags_products")
