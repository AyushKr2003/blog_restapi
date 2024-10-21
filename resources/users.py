from flask import  request
from flask.views import MethodView
from flask_smorest import abort,Blueprint
from sqlalchemy.exc import SQLAlchemyError

from db import db
from models import UsersModel
from schemas.users_schemas import UserSchema
from id_generater import generate_id

users_blp = Blueprint("users", __name__, description="user operation")

@users_blp.route("/user")
class User(MethodView):
    @users_blp.response(200, UserSchema(many=True))
    def get(self):
        # return {"users": list(users.values())};
        users = UsersModel.query.all()
        return users
    
    @users_blp.arguments(UserSchema)
    @users_blp.response(201, UserSchema)
    def post(self,request_data):
        # request_data = request.get_json()
        
        # new_user = {
        #         "id": id, 
        #         **request_data, 
        #         "created_at": timestamp
        #     }
        # users[id] = new_user
        new_user = UsersModel(**request_data)
        try:
            db.session.add(new_user)
            db.session.commit()
        except SQLAlchemyError as e:
            print(e)
            abort(500, message=f"An error occurred while inserting the user. {e}")
        
        return new_user


# @app.get("/userslist")
# def get_all_users():
#     return {"users": list(users.values())};

# @app.post("/adduser")
# def add_user():
#     request_data = request.get_json()
    
#     id = generate_id("user", request_data["username"])
#     timestamp = datetime.now(timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')
    
#     new_user = {
#             "id": id, 
#             **request_data, 
#             "created_at": timestamp
#         }
#     users[id] = new_user
    
#     return new_user, 201
