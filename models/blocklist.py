from datetime import datetime, timezone
from db import db

class BlockListModel(db.Model):
    __tablename__ = "blocklist"
    
    id = db.Column(db.Integer, primary_key=True)
    token = db.Column(db.String(255), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.now(timezone.utc), nullable=False) 