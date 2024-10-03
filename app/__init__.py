from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from app.models import db 
import os

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
    app.config['SECRET_KEY'] = os.environ.get('FLASK_SECRET_KEY', 'default_secret_key')  # Fallback to 'default_secret_key'

    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    
    # Initialize the database with the app
    db.init_app(app)
    
    # Import and register Blueprints (routes)
    from app.routes import main as main_blueprint
    app.register_blueprint(main_blueprint)

    return app



