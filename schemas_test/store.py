# Schemas
from marshmallow import Schema, fields


class AddProductSchema(Schema):
    user = fields.Str(required=True)
    name = fields.Str(required=True)
    price = fields.Float(required=True, strict=True)


class UserDetailsSchema(Schema):
    user = fields.Str(required=True)


class ItemSchema(Schema):
    item = fields.Str(required=True)
