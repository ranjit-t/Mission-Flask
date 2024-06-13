from db import db


class TagModel(db.Model):
    __tablename__ = "tags"
    id = db.Column(db.Integer, primary_key=True)
    tag = db.Column(db.String(20), unique=True, nullable=False)
    products = db.relationship(
        "ProductModel", back_populates="tags", secondary="tags_products")
