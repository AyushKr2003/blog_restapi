from marshmallow import Schema, fields

class PlainCommentSchema(Schema):
    id = fields.Int(dump_only=True)
    content = fields.Str(required=True)
    user_id = fields.Int(required=True)
    post_id = fields.Int(required=True)
    
    parent_comment_id = fields.Int()
    
    created_at = fields.DateTime(dump_only=True)
    updated_at = fields.DateTime(dump_only=True)