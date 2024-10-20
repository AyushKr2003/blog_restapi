from marshmallow import Schema, fields

class CategorySchemas(Schema):
    id = fields.Str(dump_only=True)
    name = fields.Str(required=True)
