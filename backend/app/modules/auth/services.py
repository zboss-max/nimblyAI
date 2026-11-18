"""
业务层
职责：只处理业务，数据库交互
"""
from sqlalchemy.exc import IntegrityError

from app.extensions import db
from app.models import User, PHONE_PATTERN, EMAIL_PATTERN


class AuthService:
    """auth 业务处理"""

    @staticmethod
    def sign_in(
            identifier: str,
            password: str
    ) -> tuple[User | None, str | None]:
        """
        登录：按任意标识查用户 → 验密（不区分“用户不存在”和“密码错误”）
        :return: user, err
        """
        # 确定账号类型
        if PHONE_PATTERN.match(identifier):
            column = User.phone
        elif EMAIL_PATTERN.match(identifier):
            column = User.email
        else:
            column = User.username

        # 查找并验证密码
        user = db.session.scalars(
            db.select(User).filter(column == identifier)
        ).one_or_none()
        if not user or not user.verify_password(password):
            return None, '账号或密码错误'

        return user, None

    @staticmethod
    def sign_up(
            username: str,
            phone: str,
            email: str,
            password: str,
    ) -> tuple[User | None, str | None]:
        """
        注册：查重三个标识字段 → 创建用户
        :return: user, err
        """
        # 查重
        for value, column, label in (
                (username, User.username, '用户名'),
                (phone, User.phone, '手机号'),
                (email, User.email, '邮箱')
        ):
            if value and db.session.scalars(
                    db.select(User).filter(column == value)
            ).one_or_none():
                return None, label + '已被占用'

        # 创建
        user = User()
        user.username = username or None
        user.phone = phone or None
        user.email = email or None
        user.set_password(password)

        # 提交, 数据库物理查重
        try:
            db.session.add(user)
            db.session.commit()
        except IntegrityError:
            db.session.rollback()  # 必须回滚，否则 session 进入 invalid 状态
            return None, '用户名/手机号/邮箱已被占用'

        return user, None
