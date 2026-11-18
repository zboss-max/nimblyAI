from flask import Blueprint

from app.modules.auth.routes import create_auth_blueprint


def register_routes() -> Blueprint:
    api = Blueprint('api_v1', __name__, url_prefix='/api/v1')

    api.register_blueprint(create_auth_blueprint())

    return api
