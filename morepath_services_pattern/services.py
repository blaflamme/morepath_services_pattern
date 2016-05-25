from .app import App
from .db import get_dbsession
from .generic import (
    dbsession_service,
    users_service
    )
from .models import User


@App.function(dbsession_service)
def my_dbsession_service(app):
    return get_dbsession(app.settings.sqlalchemy.__dict__)


class UsersService(object):
    def __init__(self, dbsession):
        self.dbsession = dbsession

    def all(self):
        return self.dbsession.query(User).all()

    def by_id(self, id):
        return self.dbsession.query(User)\
            .filter(User.id == id)\
            .first()

    def by_username(self, username):
        return self.dbsession.query(User)\
            .filter(User.username == username)\
            .first()

    def by_email(self, email):
        return self.dbsession.query(User)\
            .filter(User.email == email)\
            .first()

    def add(self, username, email):
        user = User(
            username=username,
            email=email
            )
        self.dbsession.add(user)
        self.dbsession.flush()
        return user


@App.function(users_service)
def my_users_service(app):
    dbsession = app.service(dbsession_service)
    return UsersService(dbsession=dbsession)
