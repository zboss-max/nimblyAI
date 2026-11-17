"""
响应体

HTTP 状态码 / code 业务码 约定

http约定
    200  查询 / 更新成功
    201  创建成功（注册）
    204  删除成功（本项目包信封，通常改用 200 + data=null）
    400  参数缺失 / 类型错 / JSON 解析失败
    401  未认证：token 缺失、无效、过期，或登录凭证错误
    403  已认证但无权限（与 401 严格区分，混用会让前端跳错登录页）
    404  资源不存在
    405  方法不允许
    409  唯一约束冲突（用户名 / 手机号已存在）
    422  语义校验失败（格式对但不符合业务规则）
    429  限流（登录失败次数过多）
    500  未捕获异常 —— 只应该是代码错误
分界线只有一条：4xx = 用户传错，5xx = 我们写错。

业务码分段约定（子段留给各模块，不要越界乱加）
    0        成功
    1xxx     认证 / 账号      auth
    2xxx     用户             user
    3xxx     项目 / 业务主体
    4xxx     文件 / 上传
    9xxx     框架级（参数、限流、服务端异常）
"""


def ok(data=None, msg='ok', status=200):
    """成功响应"""
    return {'code': 0, 'msg': msg, 'data': data}, status


def fail(msg, status=400, code=1, data=None):
    """失败响应"""
    return {'code': code, 'msg': msg, 'data': data}, status
