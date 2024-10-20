from marshmallow import Schema, fields

class PostAddUpdateSchema(Schema):
    id = fields.Str(dump_only=True)
    title = fields.Str(required=True)
    content = fields.Str(required=True) 
    status = fields.Str(required=True)
    category_id = fields.Str(required=True)
    user_id = fields.Str(required=True)
    created_at = fields.DateTime(dump_only=True)
    updated_at = fields.DateTime(dump_only=True)

