from .app import App
from .db import get_dbsession
from .models import User


@App.method(App.get_dbsession_service)
def get_dbsession_service(app):
    return get_dbsession(app.settings.sqlalchemy.__dict__)


class UserService(object):
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


@App.method(App.get_user_service)
def get_user_service(app):
    dbsession = app.get_dbsession_service()
    return UserService(dbsession=dbsession)
