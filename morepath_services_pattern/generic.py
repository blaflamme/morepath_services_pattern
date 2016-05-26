from reg import (
    dispatch,
    match_key
    )


@dispatch()
def dbsession_service(app):
    raise NotImplementedError


@dispatch()
def users_service(app):
    raise NotImplementedError


@dispatch(match_key('name', lambda name: name, default=''))
def service(app, name):
    raise NotImplementedError
