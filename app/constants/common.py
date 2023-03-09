from enum import Enum


class Status(Enum):
    PENDING = 'pending'
    ACTIVE = 'active'
    REJECT = 'reject'


class ComplainStatus(Enum):
    PENDING = 'pending'
    ACTIVE = 'active'
    REJECT = 'reject'


class NewsStatus(Enum):
    DRAFT = 'Chờ phê duyệt'
    REJECT = 'Từ chối duyệt'
    ACTIVE = 'Đã đăng'


class BannerStatus(Enum):
    PENDING = "Pending"
    ACTIVE = "active"


class HanbookStatus(Enum):
    PENDING = 'pending'
    ACTIVE = 'active'
    REJECT = 'reject'
