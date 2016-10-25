import click
import morepath
import transaction

from .app import App
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
    # create database
    dbsession = app.get_dbsession_service()
    Base.metadata.create_all(dbsession.bind)
    # add users
    users = app.get_user_service()
    with transaction.manager:
        for user in USERS:
            users.add(**user)
        transaction.commit()


if __name__ == '__main__':
    initdb()
