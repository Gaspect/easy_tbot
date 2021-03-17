import argparse
from abc import ABC, abstractmethod
from ..backend import Backend
import inspect

class ShellCommand(ABC):
    """
    Represents a command used in the OS shell
    """
    name: str
    extra: dict

    @abstractmethod
    def do(self, *args, **kwargs):
        """
        What does this the command do
        :param args:
        :param kwargs:
        :return:
        """
        pass

    def __eq__(self, other):
        return other.name == self.name

    def post_insert(self, *args, **kwargs):
        """
        This method is invoked after the command is inserted in a shell handler
        :param args:
        :param kwargs:
        :return:None
        """
        pass


class ShellBackend(Backend):
    """
    Handles all commands and stuff of every base or created section in the bot
    """

    def __init__(self):
        self.__parser = argparse.ArgumentParser()
        self.__subparsers = self.__parser.add_subparsers()
        self.__parsers = []
        self._subscriptions = []

    def add_command(self, command: ShellCommand):
        """
        Adds a command to the handler
        :param command: Command to add
        :return: None
        """
        if type(command) not in self._subscriptions:
            self._subscriptions.append(type(command))

        parser = self.__subparsers.add_parser(command.name, **command.extra)
        parser.set_defaults(func=command.do)
        self.__parsers.append(parser)
        command.post_insert(parser)

    def add_commands(self, *args):
        """
        Adds a command  set to the handler
        :param args:
        :return:
        """
        for command in args:
            self.add_command(command)

    def handle_input(self, *args):
        """
        Process the OS command input
        :param args:
        :return:
        """
        args = vars(self.__parser.parse_args(args))
        if 'func' in args:
            func = args['func']
            del args['func']
            return func(**args)
        else:
            return self.__parser.format_help()

    def type_is_command(self, type_obj):
        return issubclass(type_obj, ShellCommand) and \
                    not inspect.isabstract(type_obj) and \
                    type_obj is not ShellCommand