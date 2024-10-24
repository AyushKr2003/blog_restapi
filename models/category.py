from db import db


class CategoryModel(db.Model):
    __tablename__ = "category"
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False, unique = True)
    
    posts = db.relationship("PostModel", back_populates="category", lazy="dynamic")