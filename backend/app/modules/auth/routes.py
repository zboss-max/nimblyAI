"""
路由层
职责：只把 URL 映射到对应 Resource，不含任何业务逻辑。
"""
from flask import Blueprint

from app.modules.auth.resources import (
    SignIn,
    SignUp,
)


def create_auth_blueprint():
    blueprint = Blueprint('auth', __name__, url_prefix='/auth')

    blueprint.add_url_rule('/signin', view_func=SignIn.as_view('signin'))
    blueprint.add_url_rule('/signup', view_func=SignUp.as_view('signup'))

    return blueprint
