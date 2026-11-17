"""
时间戳
"""
from datetime import datetime

from app.extensions import db


class TimestampMixin:
    """时间戳"""
    # 创建时间
    create_time = db.Column(db.DateTime, default=datetime.now)
    # 更新时间
    update_time = db.Column(db.DateTime, default=datetime.now, onupdate=datetime.now)
