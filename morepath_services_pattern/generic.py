from reg import dispatch


@dispatch()
def dbsession_service(app):
    raise NotImplementedError


@dispatch()
def users_service(app):
    raise NotImplementedError
