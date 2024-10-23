from flask import request
from flask.views import MethodView
from flask_smorest import abort, Blueprint
from sqlalchemy.exc import SQLAlchemyError
from flask_jwt_extended import jwt_required, get_jwt_identity

from db import db
from models import PostModel
from schemas.post_schemas import PlainPostSchema


posts_blp = Blueprint("posts", __name__, description="Operations on posts")

@posts_blp.route("/posts/<int:id>")
@jwt_required()
class Post_by_id(MethodView):
    @posts_blp.response(200, PlainPostSchema)
    def get(self,id):
        post = PostModel.query.get_or_404(id)
        return post


    @posts_blp.arguments(PlainPostSchema)
    @posts_blp.response(200, PlainPostSchema)
    def put(self,id, request_data):
        # request_data = request.get_json()
    
        # timestamp = datetime.now()
        
        # try:
        #     post = posts[id]
        #     post.update({
        #         **request_data,
        #         "updated_at": timestamp,
        #     })
        #     return post
        # except KeyError:
        #     abort(404, message="post not found")
        post = PostModel.query.get(id)
        
        if not post:
            abort(404, message="post not found")
        
        current_user = get_jwt_identity()
        user_id = current_user['id']
        
        if post.user_id != user_id:
            abort(403, message="You do not have permission to update this post.")
        
        post.title = request_data["title"]
        post.content = request_data["content"]
        post.status = request_data["status"]
        
        try:
            db.session.add(post)
            db.session.commit()
            return post
        except SQLAlchemyError as e:
            print(e)
            abort(500, message=f"An error occurred while inserting the post. {e}")



    def delete(self,id):
        # try:
        #     del posts[id]
        #     return {"message": "post deleted sucessfully"}, 202
        # except:
        #     abort(404, message="post not found")
        post = PostModel.query.get_or_404(id)
        
        current_user = get_jwt_identity()
        user_id = current_user['id']
        
        if post.user_id != user_id:
            abort(403, message="You do not have permission to delete this post.")
            
        db.session.delete(post)
        db.session.commit()
        return {"message": "Post Deleted Sucessfully"}, 202


@posts_blp.route("/posts")
class Post(MethodView):
    @posts_blp.response(200, PlainPostSchema(many=True))
    def get(self):
        # return {"posts": list(posts.values())}
        posts = PostModel.query.all()
        return posts
    
    @jwt_required()
    @posts_blp.arguments(PlainPostSchema)
    @posts_blp.response(201, PlainPostSchema)
    def post(self,request_data):
        # request_data = request.get_json()
    
        # if (request_data["user_id"] in users) and (request_data["category_id"] in category):
            
        #     id = generate_id("post", request_data["title"])
        #     timestamp = datetime.now()
        #     # new_post = {
        #     #     "id": id,
        #     #     "title" : request_data["title"],
        #     #     "content": request_data["content"],
        #     #     "category_id": request_data["category_id"],
        #     #     "user_id": request_data["user_id"],
        #     #     "created_at": timestamp,
        #     #     "updated_at": timestamp
        #     # }
        #     new_post = {
        #         **request_data,
        #         "id" : id,
        #         "created_at": timestamp,
        #         "updated_at": timestamp
        #     }
        #     posts[id] = new_post
        #     return new_post , 201
        
        new_post = PostModel(**request_data)
        try:
            db.session.add(new_post)
            db.session.commit()
        except SQLAlchemyError as e:
            print(e)
            abort(500, message=f"An error occurred while inserting the post. {e}")
        
        return new_post