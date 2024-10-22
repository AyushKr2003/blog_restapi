import os
import secrets
from flask import Flask
from flask_smorest import Api
from flask_jwt_extended import JWTManager

from db import db
from resources import users_blp, posts_blp, category_blp, comment_blp


def create_app(db_url=None):
    app = Flask(__name__)

    app.config["PROPAGATE_EXCEPTIONS"] = True
    app.config["API_TITLE"] = "Blog Api"
    app.config["API_VERSION"] = "v1"
    app.config["OPENAPI_VERSION"] = "3.0.3"
    app.config["OPENAPI_URL_PREFIX"] = "/"
    app.config["OPENAPI_SWAGGER_UI_PATH"] = "/swagger-ui"
    app.config["OPENAPI_SWAGGER_UI_URL"] = "https://cdn.jsdelivr.net/npm/swagger-ui-dist/"
    
    app.config["SQLALCHEMY_DATABASE_URI"] = db_url or os.getenv("DATABASE_URI")
    print(app.config["SQLALCHEMY_DATABASE_URI"])
    
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    
    db.init_app(app)
    
    with app.app_context():
        db.create_all()

    # app.config["JWT_SECRET_KEY"] = secrets.SystemRandom().getrandbits(128)
    app.config["JWT_SECRET_KEY"] = os.getenv("JWT_SECRET_KEY")
    print(app.config["JWT_SECRET_KEY"])
    jwt = JWTManager(app)
    api = Api(app)

    api.register_blueprint(users_blp)
    api.register_blueprint(posts_blp)
    api.register_blueprint(category_blp)
    api.register_blueprint(comment_blp)
    
    return app