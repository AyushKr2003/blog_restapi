from flask import request
from flask.views import MethodView
from flask_smorest import abort, Blueprint
from datetime import datetime

from schemas.post_schemas import PostAddUpdateSchema
from demo_data import users, posts, category
from id_generater import generate_id


posts_blp = Blueprint("posts", __name__, description="Operations on posts")

@posts_blp.route("/posts/<string:id>")
class Post_by_id(MethodView):
    @posts_blp.response(200, PostAddUpdateSchema)
    def get(self,id):
        try:
            return posts[id]
        except:
            abort(404, message="Post not Found")
    

    @posts_blp.arguments(PostAddUpdateSchema)
    @posts_blp.response(200, PostAddUpdateSchema)
    def put(self,id, request_data):
        # request_data = request.get_json()
    
        timestamp = datetime.now()
        
        try:
            post = posts[id]
            post.update({
                **request_data,
                "updated_at": timestamp,
            })
            return post
            
        except KeyError:
            abort(404, message="post not found")
    
    def delete(self,id):
        try:
            del posts[id]
            return {"message": "post deleted sucessfully"}, 202
        except:
            abort(404, message="post not found")


@posts_blp.route("/posts")
class Post(MethodView):
    @posts_blp.response(200, PostAddUpdateSchema(many=True))
    def get(self):
        # return {"posts": list(posts.values())}
        return posts.values()
    
    @posts_blp.arguments(PostAddUpdateSchema)
    @posts_blp.response(201, PostAddUpdateSchema)
    def post(self,request_data):
        # request_data = request.get_json()
    
        if (request_data["user_id"] in users) and (request_data["category_id"] in category):
            
            id = generate_id("post", request_data["title"])
            timestamp = datetime.now()
            # new_post = {
            #     "id": id,
            #     "title" : request_data["title"],
            #     "content": request_data["content"],
            #     "category_id": request_data["category_id"],
            #     "user_id": request_data["user_id"],
            #     "created_at": timestamp,
            #     "updated_at": timestamp
            # }
            new_post = {
                **request_data,
                "id" : id,
                "created_at": timestamp,
                "updated_at": timestamp
            }
                
            posts[id] = new_post
            return new_post , 201
            
        abort(404, message="UserId not found")