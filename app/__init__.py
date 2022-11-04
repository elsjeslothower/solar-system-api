from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from dotenv import load_dotenv
import os

db = SQLAlchemy()
migrate = Migrate(compare_type=True)

def create_app(test_config=None):
    app = Flask(__name__)

    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    if not test_config:
        app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get("SQLALCHEMY_DATABASE_URI")
    else:
        app.config["TESTING"] = True
        app.config['SQLALCHEMY_TEST_DATABASE_URI'] = os.environ.get("SQLALCHEMY_TEST_DATABASE_URI")
    
    db.init_app(app)
    migrate.init_app(app, db)

    from .routes.routes import solar_system_bp
    app.register_blueprint(solar_system_bp)

    from app.models.planet import Planet

    return app