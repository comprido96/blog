"""Initialize Flask app."""
from flask import Flask


def create_app():
    """Create Flask application."""
    app = Flask(__name__, instance_relative_config=False)
    app.config.from_object('config.Config')

    with app.app_context():
        # Import parts of our application
        from .home import routes as home_routes
        from .posts import routes as posts_routes

        # Register Blueprints
        app.register_blueprint(home_routes.home_bp)
        app.register_blueprint(posts_routes.posts_bp)

        return app