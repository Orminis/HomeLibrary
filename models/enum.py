from enum import Enum


class UserRoles(Enum):
    user = "Standard User"
    checker = "Checker"
    admin = "Admin"


class Covers(Enum):
    soft = "Soft Cover"
    hard = "Hard Cover"


class Status(Enum):
    pending = "Pending"
    approved = "Approved"
    rejected = "Rejected"
