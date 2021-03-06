import morepath

from .app import App


def run():  # pragma: no cover
    morepath.autoscan()
    morepath.run(App())


def wsgi_factory():
    morepath.autoscan()
    morepath.scan()
    App.commit()
    return App()


application = wsgi_factory()
