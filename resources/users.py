from flask import  request
from flask.views import MethodView
from flask_smorest import abort,Blueprint
from sqlalchemy.exc import SQLAlchemyError
from passlib.hash import pbkdf2_sha256
from flask_jwt_extended import create_access_token, jwt_required

from db import db
from models import UsersModel
from schemas import UserSchema,UserLoginSchema


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


@users_blp.route("/user/login")
class LogIn(MethodView):
    @users_blp.arguments(UserLoginSchema)
    def post(self, request_data):
        user = UsersModel.query.filter(
            UsersModel.username == request_data["username"]
        ).first()
        if user and pbkdf2_sha256.verify(request_data["password"], user.password):
            access_token = create_access_token(identity=user.id)
            return {"access_token": access_token}
        
        abort(401, message="Invalid Credentials.")