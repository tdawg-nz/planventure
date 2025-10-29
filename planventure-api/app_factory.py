# app_factory.py
import os
from flask import Flask
from dotenv import load_dotenv
from extensions import db

load_dotenv()

def _register_models():
    # Import models here (after db is bound). No wildcard import.
    from models.user import User       # noqa: F401
    from models.base import BaseModel  # noqa: F401
    # add other models...

def create_app():
    app = Flask(__name__, instance_relative_config=True)
    os.makedirs(app.instance_path, exist_ok=True)

    app.config["SQLALCHEMY_DATABASE_URI"] = (
        os.getenv("SQLALCHEMY_DATABASE_URI")
        or "sqlite:///" + os.path.join(app.instance_path, "dev.db")
    )
    app.config.setdefault("SQLALCHEMY_TRACK_MODIFICATIONS", False)

    # Bind the single db instance to this app
    db.init_app(app)

    # Import models AFTER binding, so metadata binds to this app’s engine
    with app.app_context():
        _register_models()

    return app