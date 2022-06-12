"""Initialize Flask app."""
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


db = SQLAlchemy()
migrate = Migrate()


def create_app():
    """Create Flask application."""
    app = Flask(__name__, instance_relative_config=False)
    app.config.from_object('config.Config')

    db.init_app(app)
    migrate.init_app(app, db)

    with app.app_context():
        # Import parts of our application
        from .home import routes as home_routes
        from .posts import routes as posts_routes
        from . import models

        # Register Blueprints
        app.register_blueprint(home_routes.home_bp)
        app.register_blueprint(posts_routes.posts_bp)

        db.create_all()

        return app