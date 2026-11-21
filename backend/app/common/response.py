"""
响应体

HTTP 状态码 / code 业务码 约定

http约定
    200  查询 / 更新成功
    201  创建成功（注册）
    204  删除成功（本项目包信封，通常改用 200 + data=null）
    400  参数缺失 / 参数错误 / 类型错 / JSON 解析失败
    401  未认证：token 缺失、无效、过期，或登录凭证错误，未经授权
    403  已认证但无权限（与 401 严格区分，混用会让前端跳错登录页）
    404  资源 / 接口 不存在
    405  请求方法不允许
    409  唯一约束冲突（用户名 / 手机号已存在）
    415  格式不支持
    422  语义校验失败（格式对但不符合业务规则）
    429  限流（登录失败次数过多）
    500  未捕获异常 —— 只应该是代码错误
分界线只有一条：4xx = 用户传错，5xx = 我们写错。

业务码分段约定（子段留给各模块，不要越界乱加）
    0        成功
    1        错误
    1xxx     认证 / 账号      auth
    2xxx     用户             user
    3xxx     项目 / 业务主体
    4xxx     文件 / 上传
    9xxx     框架级（参数、限流、服务端异常）
"""
from werkzeug.exceptions import HTTPException

from app.extensions import db


def ok(data: dict = None, status=200, msg='ok'):
    """成功响应"""
    if data is None:
        data = {}
    return {'code': 0, 'msg': msg, 'data': data}, status


def fail(msg: str, status=400, code=1, data: dict = None):
    """失败响应"""
    return {'code': code, 'msg': msg, 'data': data}, status


"""
JWT 错误回调：把扩展的默认响应统一成项目格式
"""


def register_jwt_callbacks(jwt):
    """JWT 错误回调：把扩展的默认响应统一成项目格式"""

    @jwt.unauthorized_loader
    def missing_token(reason):
        """没带 Authorization 头，没有token"""
        return fail('请先登录', 401)

    @jwt.invalid_token_loader
    def invalid_token(reason):
        """格式错 / 签名被改过，无效token"""
        return fail('登录凭证无效', 401)

    @jwt.expired_token_loader
    def expired_token(jwt_header, jwt_payload):
        """过期token"""
        return fail('登录已过期', 401)

    @jwt.user_identity_loader
    def _identity_to_str(user_id):
        """统一把 identity 规定为字符串"""
        return str(user_id)


"""
接管系统报错的404和500统一成项目格式
"""

_HTTP_MSG = {
    400: '请求参数错误',
    401: '未登录或登录已过期',
    403: '没有操作权限',
    404: '请求的接口不存在',
    405: '请求方法不允许',
    413: '请求内容过大',
    415: '不支持的请求格式',
    422: '参数不符合业务规则',
    429: '请求过于频繁，请稍后再试',
    500: '服务异常，请稍后重试',
}


def register_error_handlers(app):
    """接管 Flask 层错误,把默认响应统一成项目格式"""

    @app.errorhandler(HTTPException)
    def _http_error(e: HTTPException):
        """预期内的 HTTP 错误：原状态码返回，只换中文文案"""
        status = e.code or 500  # 理论e.code可能为空
        return fail(_HTTP_MSG.get(status, e.name), status)

    @app.errorhandler(Exception)
    def _uncaught_error(e: Exception):
        """未捕获异常：只对 4xx 转交，其余一律当 5xx 处理并留堆栈"""
        # 兜底，正常不会走到
        if isinstance(e, HTTPException) and (e.code or 500) < 500:
            return _http_error(e)

        db.session.rollback()  # 关键：异常后不清 session，后续请求会连环报错
        app.logger.exception(e)  # 5xx 必须留 traceback
        return fail(_HTTP_MSG[500], 500, 9999)
