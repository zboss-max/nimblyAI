"""
校验层
职责：校验接收到的请求数据，合规返回值，不合规返回报错，不处理业务
"""
from dataclasses import dataclass

from app.models.user import USERNAME_PATTERN, PHONE_PATTERN, EMAIL_PATTERN


@dataclass
class SignInSchema:
    """登录请求参数校验：identifier 可以是用户名/手机号/邮箱"""

    identifier: str
    password: str

    @classmethod
    def from_json(cls, payload: dict) -> 'SignInSchema':
        """json数据校验"""

        # 类型校验
        if not isinstance(payload, dict):
            raise TypeError("请求体不是 JSON 对象")

        schema = cls(
            identifier=(
                    payload.get('identifier') or
                    payload.get('username') or
                    ''
            ).strip(),  # .strip()：自动去掉首尾空格
            password=payload.get('password') or ''
        )

        # 空值校验
        if not schema.identifier:
            raise ValueError('账号不能为空')
        if not schema.password:
            raise ValueError('密码不能为空')

        return schema


@dataclass
class SignUpSchema:
    """注册请求参数校验：用户名 手机号 邮箱 三选一必填"""

    username: str = ''
    phone: str = ''
    email: str = ''
    password: str = ''

    @classmethod
    def from_json(cls, payload: dict) -> 'SignUpSchema':
        """json数据校验"""

        # 类型校验
        if not isinstance(payload, dict):
            raise TypeError("请求体不是 JSON 对象")

        schema = cls(
            username=(payload.get('username') or '').strip(),
            phone=(payload.get('phone') or '').strip(),
            email=(payload.get('email') or '').strip(),
            password=payload.get('password') or '',
        )

        # 空值校验
        if not (schema.username or schema.phone or schema.email):
            raise ValueError('用户名、手机号、邮箱至少填一个')
        if not schema.password:
            raise ValueError('密码不能为空')

        # 格式校验
        if schema.username and not USERNAME_PATTERN.match(schema.username):
            raise ValueError('用户名需为 8-16 位字母或数字')
        if schema.phone and not PHONE_PATTERN.match(schema.phone):
            raise ValueError('手机号格式不正确')
        if schema.email and not EMAIL_PATTERN.match(schema.email):
            raise ValueError('邮箱格式不正确')
        if len(schema.password) < 8:
            raise ValueError('密码至少 8 位')

        return schema
