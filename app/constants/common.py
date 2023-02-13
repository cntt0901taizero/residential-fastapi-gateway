from enum import Enum


class ComplainStatus(Enum):
    PENDING = 'pending'
    ACTIVE = 'active'
    REJECT = 'reject'
