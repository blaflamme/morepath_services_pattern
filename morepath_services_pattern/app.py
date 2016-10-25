from morepath import dispatch_method
from more.transaction import TransactionApp


class App(TransactionApp):

    @dispatch_method()
    def get_dbsession_service(self):
        raise NotImplementedError

    @dispatch_method()
    def get_user_service(self):
        raise NotImplementedError


@App.setting_section(section='sqlalchemy')
def get_sqlalchemy_setting_section():
    return {
        'sqlalchemy.url': 'sqlite:///morepath_services_pattern.db'
        }
