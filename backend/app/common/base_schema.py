"""
基础校验层
所有校验层的类都必需继承此类
"""
from abc import ABC, abstractmethod
from typing import Self

from flask import request


class BaseSchema(ABC):
    """
    基础校验类
    继承此类报错均走raise
    调用parse_body()校验
    """

    @classmethod
    @abstractmethod
    def from_json(cls, payload: dict) -> Self:
        """从 JSON 构造实例，校验失败抛 ValueError"""

    @classmethod
    def parse_body(cls) -> tuple[Self | None, str | None, int | None]:
        """
        校验请求体，返回 (schema, 错误响应)
        调用方必须用两个变量接收
        :return:self, err, status
        """
        try:
            # 获取json数据并校验
            return cls.from_json(request.get_json(silent=True)), None, None
        except (TypeError, ValueError) as e:
            return None, str(e), 400
