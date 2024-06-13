from marshmallow import Schema, fields


class PlainProductSchema(Schema):
    id = fields.Int(dump_only=True)
    title = fields.Str(required=True)
    price = fields.Float(required=True)
    tag = fields.Str(read_only=True)


class PlainStoreSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str(required=True)


class TagSchema(Schema):
    id = fields.Int(dump_only=True)
    tag = fields.Str(required=True)


class StoreSchema(PlainStoreSchema):
    products = fields.List(fields.Nested(PlainProductSchema()), dump_only=True)


class ProductSchema(PlainProductSchema):
    store_id = fields.Int(required=True, load_only=True)
    store = fields.Nested(PlainStoreSchema(),  dump_only=True)
    tags = fields.List(fields.Nested(TagSchema()), dump_only=True)
