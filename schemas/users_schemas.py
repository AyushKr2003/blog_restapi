from marshmallow import Schema, fields
from schemas import PlainPostSchema

class UserLoginSchema(Schema):
    username = fields.Str(required=True)
    password = fields.Str(required=True, load_only=True)
    
class UserSchema(UserLoginSchema):
    id = fields.Int(dump_only=True)
    email = fields.Email(required=True)
    role = fields.Str(required=True)
    created_at = fields.DateTime(dump_only=True)



class UserPostSchema(UserSchema):
    post_id = fields.Int(required=True, load_only=True)
    posts = fields.Nested(PlainPostSchema(), dump_only=True)