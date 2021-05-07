from abc import ABC, abstractmethod
from typing import List

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

class Backend(ABC):

    @abstractmethod
    def add_command(self, command:ShellCommand ):
        pass

    @abstractmethod
    def handle_input(self, *args):
        pass

    def add_commands(self, *commands:List[ShellCommand]):
        for command in commands:
            self.add_commands(command)