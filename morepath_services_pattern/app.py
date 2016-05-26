from functools import lru_cache
from dectate import convert_dotted_name
from more.transaction import TransactionApp

from .generic import service


class App(TransactionApp):

    @lru_cache()
    def service(self, func):
        if isinstance(func, str):
            func = convert_dotted_name(func)
        return func(self)

    @lru_cache()
    def find_service(self, name=''):
        return service(self, name=name)


@App.setting_section(section='sqlalchemy')
def get_sqlalchemy_setting_section():
    return {
        'sqlalchemy.url': 'sqlite:///morepath_services_pattern.db'
        }
