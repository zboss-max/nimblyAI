from flask import request

from app.common.response import fail


def parse_body(schema_cls):
    """校验请求体，返回 (schema, 错误响应)"""
    try:
        return schema_cls.from_json(request.get_json(silent=True)), None
    except (TypeError, ValueError) as e:
        return None, fail(str(e), 400)
