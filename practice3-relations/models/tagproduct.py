from db import db


class TagProductModel(db.Model):
    __tablename__ = "tags_products"
    id = db.Column(db.Integer, primary_key=True)
    product_id = db.Column(db.Integer, db.ForeignKey("products.id"))
    tag_id = db.Column(db.Integer, db.ForeignKey("tags.id"))


# class TagProductModel(db.Model):
#     __tablename__ = "tags_products"
#     id = db.Column(db.Integer, primary_key=True)
#     product_id = db.Column(db.Integer, db.ForeignKey("products.id"))
#     tag_id = db.Column(db.Integer, db.ForeignKey("tags.id"))
