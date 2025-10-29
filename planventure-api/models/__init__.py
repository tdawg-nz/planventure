# models/__init__.py
# DO NOT create a new SQLAlchemy() here.
# Optionally re-export db if you like:
# from extensions import db

from .user import User       # noqa: F401
from .trip import Trip       # noqa: F401
from .base import BaseModel   # noqa: F401

__all__ = ['db', 'User', 'Trip']