import os
import secrets
from flask import Flask, jsonify
from flask_smorest import Api
from flask_jwt_extended import JWTManager, get_jwt
from flask_migrate import Migrate
from dotenv import load_dotenv

from datetime import datetime, timedelta, timezone
from apscheduler.schedulers.background import BackgroundScheduler
import atexit

from db import db
from models import BlockListModel
from resources import users_blp, posts_blp, category_blp, comment_blp


def create_app(db_url=None):
    app = Flask(__name__)
    
    load_dotenv()

    app.config["PROPAGATE_EXCEPTIONS"] = True
    app.config["API_TITLE"] = "Blog Api"
    app.config["API_VERSION"] = "v1"
    app.config["OPENAPI_VERSION"] = "3.0.3"
    app.config["OPENAPI_URL_PREFIX"] = "/"
    app.config["OPENAPI_SWAGGER_UI_PATH"] = "/swagger-ui"
    app.config["OPENAPI_SWAGGER_UI_URL"] = "https://cdn.jsdelivr.net/npm/swagger-ui-dist/"
    
    app.config["SQLALCHEMY_DATABASE_URI"] = db_url or os.getenv("DATABASE_URI", "sqlite:///data.db")
    print(app.config["SQLALCHEMY_DATABASE_URI"])
    
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    
    db.init_app(app)
    
    migrate = Migrate(app, db)
    
    # since we are using flask migrate we no longer need to db.create_all()
    # with app.app_context():
    #     db.create_all()

    # app.config["JWT_SECRET_KEY"] = secrets.SystemRandom().getrandbits(128)
    app.config["JWT_SECRET_KEY"] = os.getenv("JWT_SECRET_KEY")
    app.config['JWT_ACCESS_TOKEN_EXPIRES'] = timedelta(hours=24)
    
    jwt = JWTManager(app)
    
    @jwt.token_in_blocklist_loader
    def check_if_token_is_revoked(jwt_header, jwt_payload):
        jti = jwt_payload["jti"]
        return BlockListModel.query.filter(BlockListModel.token == jti).first() is not None
    
    @jwt.revoked_token_loader
    def revoked_token_callback(jwt_header, jwt_payload):
        return (
            jsonify({"description": "The token has been revoked.", "error": "token_revoked"}), 
            401
        )
    
    @jwt.needs_fresh_token_loader
    def token_not_fresh_callback(jwt_header, jwt_payload):
        return (
            jsonify(
                {
                    "description": "The token is not fresh.",
                    "error": "fresh_token_required",
                }
            ),
            401,
        )
    
    @jwt.expired_token_loader
    def expired_token_callback(jwt_header, jwt_payload):
        return (
            jsonify({"message": "The token has expired.", "error": "token_expired"}),
            401,
        )
    
    @jwt.invalid_token_loader
    def invalid_token_callback(error):
        return (
            jsonify(
                {"message": "Signature verification failed.", "error": "invalid_token"}
            ),
            401,
        )
    
    @jwt.unauthorized_loader
    def missing_token_callback(error):
        return (
            jsonify(
                {
                    "description": "Request does not contain an access token.",
                    "error":"authorization_required"
                }
            ), 
            401
        )
    
    api = Api(app)

    api.register_blueprint(users_blp)
    api.register_blueprint(posts_blp)
    api.register_blueprint(category_blp)
    api.register_blueprint(comment_blp)
    
    
    # Initialize APScheduler
    scheduler = BackgroundScheduler()
    
    # Wrap the cleanup function
    def cleanup_blocklisted_tokens():
        with app.app_context():  
            cutoff_date = datetime.now(timezone.utc) - timedelta(days=2)
            BlockListModel.query.filter(BlockListModel.created_at < cutoff_date).delete()
            db.session.commit()

    # Schedule the job
    scheduler.add_job(cleanup_blocklisted_tokens, 'interval', hours=24)
    scheduler.start()
    
    # Shutdown Scheduler on Exit
    @atexit.register
    def shutdown_scheduler():
        scheduler.shutdown()
    
    return app