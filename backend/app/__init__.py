"""
应用工厂，flask源代码：create_app
"""
from flask import Flask

from config import config
from app.extensions import db, jwt, migrate


def create_app(config_name):
    """初始化应用"""
    # 初始化flask对象
    app = Flask(__name__)
    # 添加配置
    app.config.from_object(config[config_name])
    # 初始化数据库
    db.init_app(app)
    # 初始化数据迁移，通过 Alembic 管理表结构变更
    migrate.init_app(app, db)
    # 初始化jwt
    jwt.init_app(app)

    # 导入模型，注册到 SQLAlchemy metadata
    import_models()

    # 注册 JWT 错误回调
    from app.common.response import register_jwt_callbacks
    register_jwt_callbacks(jwt)

    # 注册全局错误处理
    from app.common.response import register_error_handlers
    register_error_handlers(app)

    # 导入api并由配置控制
    from app.api import get_registry
    for version in app.config["API_VERSIONS"]:
        app.register_blueprint(get_registry()[version]())

    return app


def import_models():
    """显式导入全部模型，确保 SQLAlchemy 和 Alembic 能发现所有数据表"""
    import app.models
