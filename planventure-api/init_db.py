# init_db.py
from app_factory import create_app
from extensions import db

# Import model modules/classes explicitly so SQLAlchemy sees tables
from models.user import User    # noqa: F401
from models.trip import Trip    # noqa: F401

app = create_app()
with app.app_context():
    db.create_all()
    print("Database initialized.")