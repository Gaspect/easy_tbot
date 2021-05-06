
import inspect
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm.session import sessionmaker
from importlib import import_module
from functools import cached_property
from easy_tbot.core.db.backend import Backend
from easy_tbot.core.settings import Settings

class SqlAlchemyBackend(Backend):

    def __init__(self, url):
        self.__engine = create_engine(url)
    
    @property
    def engine(self):
        return self.__engine

    @cached_property
    def model(self):
        return declarative_base()
    
    @cached_property
    def session(self):
        return sessionmaker(self.engine.load())
    
    def migrate(self):
        """
        A helper function that write the proper tables in the database and for some kinds of
        databases (ie sqlite) it generates a database file.
        :return: All subscriptions models of the database, the datatables in raw format.
        """
        subscriptions = []

        def handle_app(app):
            app_module = import_module(f'{app}.models')
            for name, value in inspect.getmembers(app_module, inspect.isclass):
                if issubclass(value, self.model) and name is not self.model and value.__table__ not in subscriptions:
                    subscriptions.append(value.__table__)

        Settings().setup_apps(handle_app)
        self.model.metadata.create_all(self.engine, tables=subscriptions)
        return subscriptions
