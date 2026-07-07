from enum import Enum


class PassStatus(Enum):
    PENDING = "pending"
    APPROVED = "approved"
    REJECTED = "rejected"