from marshmallow import Schema, fields

class UserSchema(Schema):
    id = fields.Str(dump_only=True)
    username = fields.Str(required=True)
    password = fields.Str(required=True)
    email = fields.Email(required=True)
    role = fields.Str(required=True)
    created_at = fields.DateTime(dump_only=True)