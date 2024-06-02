# schemas.py
from marshmallow import Schema, fields, post_load
import base64

from Models import ProductModel


class PlainProductSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str(required=True)
    price = fields.Float(required=True)
    description = fields.Str(required=True)
    image_name = fields.Str(required=True, dump_only=True)


# class ProductSchema(Schema):
#     data = fields.Nested(PlainProductSchema)
#     image = fields.Method(serialize='serialize_image',
#                           deserialize='deserialize_image',)

#     def serialize_image(self, product):
#         if product.image:
#             return base64.b64encode(product.image).decode('utf-8')
#         return None

#     def deserialize_image(self, value):
#         if value:
#             return base64.b64decode(value)
#         return None
