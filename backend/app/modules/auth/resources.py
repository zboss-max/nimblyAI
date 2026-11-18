"""
HTTP 适配层
职责：只做 HTTP 与 Python 之间的翻译——校验 → 调业务 → 组装响应，不写任何业务规则。
"""
from flask.views import MethodView
from flask_jwt_extended import create_access_token

from app.modules.auth.schemas import SignInSchema, SignUpSchema
from app.modules.auth.services import AuthService
from app.common.response import ok, fail


class SignIn(MethodView):
    """登录"""

    def post(self):
        # 校验
        schema, err = SignInSchema.parse_body()
        if err:
            return fail(err, 400)

        # 处理
        user, err = AuthService.sign_in(
            identifier=schema.identifier,
            password=schema.password
        )
        if err:
            return fail(err, 401)

        # 响应
        token = create_access_token(identity=user.id)  # 创建token，访问令牌
        return ok(
            {
                'token': token,
                'user': user.to_dict()
            }
        )


class SignUp(MethodView):
    """注册"""

    def post(self):
        # 校验
        schema, err = SignUpSchema.parse_body()
        if err:
            return fail(err, 400)

        # 处理
        user, err = AuthService.sign_up(
            username=schema.username,
            phone=schema.phone,
            email=schema.email,
            password=schema.password
        )
        if err:
            return fail(err, 409)

        # 响应
        token = create_access_token(identity=user.id)  # 创建token，访问令牌
        return ok(
            {
                'token': token,
                'user': user.to_dict()
            },
            201
        )
