from datetime import datetime, timezone
from enum import Enum

from db import db

class Role(Enum):
    Admin = "Admin"
    Author = "Author"
    Reader = "Reader"


class UsersModel(db.Model):
    __tablename__ = "users"
    
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(255), nullable= False, unique =True)
    email = db.Column(db.String(255), nullable= False)
    password = db.Column(db.String(), nullable= False)
    role = db.Column(db.Enum(Role), nullable= False)
    created_at = db.Column(db.DateTime, default=datetime.now(timezone.utc), nullable= False)
    
    posts = db.relationship("PostModel", back_populates="user", lazy="dynamic", cascade="all, delete")