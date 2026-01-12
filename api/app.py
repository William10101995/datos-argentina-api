from flask import Flask
from api.config import get_config
from api.extensions import cors, limiter
from api.routes import register_routes


def create_app():
    app = Flask(__name__)
    app.config.from_object(get_config())

    cors.init_app(app, resources={r"/api/*": {"origins": app.config["CORS_ORIGINS"]}})
    limiter.init_app(app)

    register_routes(app)

    @app.route("/", methods=["GET"])
    def health():
        return {"status": "ok"}

    return app
