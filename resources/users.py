from flask import  request
from flask.views import MethodView
from flask_smorest import abort,Blueprint
from sqlalchemy.exc import SQLAlchemyError
from passlib.hash import pbkdf2_sha256

from db import db
from models import UsersModel
from schemas.users_schemas import UserSchema


users_blp = Blueprint("users", __name__, description="user operation")

@users_blp.route("/user")
class User(MethodView):
    @users_blp.response(200, UserSchema(many=True))
    def get(self):
        # return {"users": list(users.values())};
        users = UsersModel.query.all()
        return users

@users_blp.route("/user/<int:id>")
class UserById(MethodView):
    def get(self,id):
        user = UsersModel.query.get_or_404(id)
        return user
    
    def put(self,id):
        user = UsersModel.query.get(id)
        if not user:
            abort(404, message="User not found")
        
        user.username = request.json["username"]
        user.email = request.json["email"]
        user.password = pbkdf2_sha256.hash(request.json["password"])
        user.role = request.json["role"]
        try:
            db.session.add(user)
            db.session.commit()
        except SQLAlchemyError as e:
            abort(500, message=f"An error occurred while updating the user. {e}")
        return user
    
    def delete(self,id):
        user = UsersModel.query.get_or_404(id)
        db.session.delete(user)
        db.session.commit()
        return {"message": "User Deleted"}

@users_blp.route("/user/signup")
class UserSignup(MethodView):
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
        new_user.password = pbkdf2_sha256.hash(request_data["password"])
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
