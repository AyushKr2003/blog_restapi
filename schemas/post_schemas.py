from marshmallow import Schema, fields

class PlainPostSchema(Schema):
    id = fields.Int(dump_only=True)
    title = fields.Str(required=True)
    content = fields.Str(required=True) 
    status = fields.Str(required=True)
    
    category_id = fields.Int(required=True)
    user_id = fields.Int(required=True)
    
    created_at = fields.DateTime(dump_only=True)
    updated_at = fields.DateTime(dump_only=True)


class PostCategorySchema(PlainPostSchema):
    category_id = fields.Int(required=True)
    categories = fields.Nested(PlainPostSchema(), dump_only=True)


# class PostSchema(PlainPostSchema):
#     user_id = fields.Int(required=True)