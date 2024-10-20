from datetime import datetime, timezone
from enum import Enum

from db import db


class PostStatus(Enum):
    DRAFT = "Draft"
    PUBLISHED = "Published"

class PostModel(db.Model):
    __tablename__ = "posts"
    
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable= False)
    content = db.Column(db.Text, nullable=False)
    status = db.Column(db.Enum(PostStatus), nullable=False)
    
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    category_id = db.Column(db.Integer, db.ForeignKey("category.id"), nullable=False)
    
    created_at = db.Column(db.DateTime, default=datetime.now(timezone.utc), nullable=False)
    updated_at = db.Column(db.DateTime, default=datetime.now(timezone.utc), onupdate=datetime.now(timezone.utc), nullable=False)
    
    user = db.relationship("UsersModel", back_populates="posts")
    category = db.relationship("CategoryModel", back_populates = "posts")