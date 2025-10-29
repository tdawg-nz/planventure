# models/base.py
from extensions import db
from datetime import datetime, timezone

class BaseModel(db.Model):
    __abstract__ = True
    
    created_at = db.Column(db.DateTime, nullable=False, default=lambda: datetime.now(timezone.utc))
    updated_at = db.Column(db.DateTime, nullable=False, default=lambda: datetime.now(timezone.utc), onupdate=lambda: datetime.now(timezone.utc))