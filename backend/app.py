from flask import Flask
from extensions import jwt, config

from user.users import users
from user.auth import auth

from polls.polls import polls

from health.health import health
from handler.handlers import handlers


def create_app():
    """App Factory.

    Returns:
        App: Flask app object.

    """
    app = Flask(__name__)
    jwt.init_app(app)

    app.config["JWT_SECRET_KEY"] = config.JWT_SECRET_KEY
    app.config["JWT_ACCESS_TOKEN_EXPIRES"] = config.JWT_ACCESS_TOKEN_EXPIRES

    app.register_blueprint(auth)
    app.register_blueprint(users)

    app.register_blueprint(polls)
    
    app.register_blueprint(health)
    app.register_blueprint(handlers)

    return app
