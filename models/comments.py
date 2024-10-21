from datetime import datetime, timezone
from db import db


class CommentsModel(db.Model):
    __tablename__ = "comments"
    
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.Text, nullable=False)
    
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    post_id = db.Column(db.Integer, db.ForeignKey("posts.id"), nullable=False)
    
    created_at = db.Column(db.DateTime, default=datetime.now(timezone.utc),nullable=False)
    parent_comment_id = db.Column(db.Integer, db.ForeignKey("comments.id"), nullable=True)