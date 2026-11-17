"""
HTTP 适配层
职责：只做 HTTP 与 Python 之间的翻译——校验 → 调业务 → 组装响应，不写任何业务规则。
"""
from flask.views import MethodView


class SignIn(MethodView):
    """登录"""

    def post(self):
        # 校验
        pass


class SignUp(MethodView):
    """注册"""

    def post(self):
        pass
