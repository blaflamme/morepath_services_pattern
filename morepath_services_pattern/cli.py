import click
import morepath
import transaction

from .app import App
from .generic import (
    dbsession_service,
    users_service
    )
from .models import Base


USERS = [{
    'username': 'john',
    'email': 'john@doe.com'
    }, {
    'username': 'jane',
    'email': 'jane@doe.com'
    }]


@click.command()
def initdb():
    click.echo('Initialize database...')
    morepath.autoscan()
    morepath.scan()
    App.commit()
    app = App()
    app.set_implicit()
    # create database
    dbsession = app.service(dbsession_service)
    Base.metadata.create_all(dbsession.bind)
    # add users
    users = app.service(users_service)
    with transaction.manager:
        for user in USERS:
            users.add(**user)
        transaction.commit()


if __name__ == '__main__':
    initdb()
