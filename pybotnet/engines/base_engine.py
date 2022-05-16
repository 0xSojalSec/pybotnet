from abc import ABC
from abc import abstractmethod


from typing import List, Union, Literal


class BaseEngine(ABC):
    """Base Engine"""

    @abstractmethod
    def __str__(self):
        return "Base Engine"

    @abstractmethod
    def receive(self) ->Union[List[str], Literal[False]]:
        """get last admin command"""
        ...

    @abstractmethod
    def send(self, message: str) -> bool:
        """send message to admin"""
        ...

    @abstractmethod
    def send_file(self, file_route: str) -> bool:
        """send file to admin"""
        ...
