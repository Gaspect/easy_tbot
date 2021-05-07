import argparse
import inspect
from easy_tbot.core.shell.backend import Backend, ShellCommand

class ShellBackend(Backend):
    """
    Handles all commands and stuff of every base or created section in the bot
    """

    def __init__(self):
        self.__parser = argparse.ArgumentParser()
        self.__subparsers = self.__parser.add_subparsers()

    def add_command(self, command):
        """
        Adds a command to the handler
        :param command: Command to add
        :return: None
        """
        parser = self.__subparsers.add_parser(command.name, **command.extra)
        parser.set_defaults(func=command.do)

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