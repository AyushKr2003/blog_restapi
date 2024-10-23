from flask import request
from flask.views import MethodView
from flask_smorest import abort, Blueprint
from sqlalchemy.exc import SQLAlchemyError
from flask_jwt_extended import jwt_required, get_jwt_identity

from db import db
from models import CommentsModel
from schemas import PlainCommentSchema

comment_blp = Blueprint("comments", __name__, description="Operations on comments")

@comment_blp.route("/comments")
class Comments(MethodView):
    @comment_blp.response(200, PlainCommentSchema(many=True))
    def get(self):
        comments = CommentsModel.query.all()
        return comments
    
    @jwt_required()
    @comment_blp.arguments(PlainCommentSchema)
    @comment_blp.response(201, PlainCommentSchema)
    def post(self, requested_data):
        comments = CommentsModel(**requested_data)
        
        try:
            db.session.add(comments)
            db.session.commit()
            return comments
        except SQLAlchemyError as e:
            abort(500, message=f"An error occurred while inserting the comment. {e}")


@jwt_required()
@comment_blp.route("/comments/<int:id>")
class CommentsById(MethodView):
    @comment_blp.response(200, PlainCommentSchema)
    def get(self, id):
        comments = CommentsModel.query.get_or_404(id)
        return comments
    
    @comment_blp.arguments(PlainCommentSchema)
    @comment_blp.response(200, PlainCommentSchema)
    def put(self, requested_data, id):
        current_user = get_jwt_identity()
        user_id = current_user['id']
        
        comment = CommentsModel.query.get(id)
        
        if not comment:
            abort(404, message="Comment not found")
        
        if comment.user_id != user_id:
            abort(403, message="You do not have permission to delete this comment.")
        
        comment.content = requested_data["content"]
        try:
            db.session.add(comment)
            db.session.commit()
            return comment
        except SQLAlchemyError as e:
            abort(500, message=f"An error occurred while updating the comment. {e}")
    
    @comment_blp.response(204)
    def delete(self, id):
        
        current_user = get_jwt_identity()
        user_id = current_user['id']
        
        comments = CommentsModel.query.get_or_404(id)
        
        if comments.user_id != user_id:
            abort(403, message="You do not have permission to delete this comment.")
        db.session.delete(comments)
        db.session.commit()
        return {"message": "Comment Deleted"}, 204