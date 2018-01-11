import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# Instantiate the db
db = SQLAlchemy()


def create_app():
    # Instantiate the app
    app = Flask(__name__)

    # Set config
    app_settings = os.getenv('APP_SETTINGS')
    app.config.from_object(app_settings)

    # set up extensions
    db.init_app(app)

    # register blueprints
    from project.api.users import users_blueprint
    app.register_blueprint(users_blueprint)

    return app
