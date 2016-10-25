from .app import App
from .models import (
    Root,
    Users,
    User
    )


@App.path(model=Root, path='/')
def get_root(request):
    return Root()


@App.path(model=Users, path='/users')
def get_users(request):
    service = request.app.get_user_service()
    users = service.all()
    return Users(users)


@App.path(
    model=User,
    path='/users/{id}',
    converters={'id': int}
    )
def get_user(request, id):
    service = request.app.get_user_service()
    return service.by_id(id=id)
