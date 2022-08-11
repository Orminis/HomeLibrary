from sqlalchemy import func

from db import db
from models.enum import UserRoles


class BasicUserModel(db.Model):
    __abstract__ = True

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), nullable=False, unique=True)
    first_name = db.Column(db.String(35), nullable=False)
    last_name = db.Column(db.String(35), nullable=False)
    email = db.Column(db.Email(100), nullable=False, unique=True)
    password = db.Column(db.String(255), nullable=False)
    created_on = db.Column(db.DateTime, server_default=func.now())


# Minimal class for users in the system
class StandardUserModel(BasicUserModel):
    __tablename__ = "standard_user"

    role = db.Column(db.Enum(UserRoles), default=UserRoles.user, nullable=False)


# Class for users who check new additions or editions of books in the system
class CheckerModel(BasicUserModel):
    __tablename__ = "checker"

    role = db.Column(db.Enum(UserRoles), default=UserRoles.checker, nullable=False)


# Class for users who keep the system running and creates new admins or checkers
class AdminModel(BasicUserModel):
    __tablename__ = "admin"

    role = db.Column(db.Enum(UserRoles), default=UserRoles.admin, nullable=False)