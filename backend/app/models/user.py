"""
user模型
"""
from werkzeug.security import generate_password_hash, check_password_hash
import re

from app.extensions import db
from app.models.timestamp_mixin import TimestampMixin

PHONE_PATTERN = re.compile(r'^1\d{10}$')
EMAIL_PATTERN = re.compile(r'^[\w.+-]+@[\w-]+(\.[\w-]+)+$')
USERNAME_PATTERN = re.compile(r'^[a-zA-Z0-9]{8,16}$')


class User(TimestampMixin, db.Model):
    """用户表"""
    __tablename__ = 'user'

    id = db.Column(db.Integer, primary_key=True)

    # 用户名（字母数字 8-16 位）
    username = db.Column(
        db.String(32),
        unique=True,
        nullable=True
    )

    # 手机号
    phone = db.Column(
        db.String(16),
        unique=True,
        nullable=True
    )

    # 邮箱
    email = db.Column(
        db.String(64),
        unique=True,
        nullable=True
    )

    # 密码
    password = db.Column(
        db.String(256),
        nullable=False
    )

    def verify_password(self, pwd):
        """验证密码"""
        return check_password_hash(self.password, pwd)  # 比对哈希值

    def set_password(self, pwd):
        """写入密码"""
        self.password = generate_password_hash(pwd)  # 生成哈希值

    def to_dict(self):
        """字典输出，排除密码"""
        return {
            'username': self.username,
            'phone': self.phone,
            'email': self.email,
            'create_time': self.create_time.strftime('%Y-%m-%d %H:%M:%S')
            if self.create_time else None,
        }
