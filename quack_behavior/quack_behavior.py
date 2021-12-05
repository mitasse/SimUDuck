"""Represent a quack behavior"""
from typing import Protocol


class QuackBehavior(Protocol):
    """Quack behavior protocol"""

    def quack(self) -> None:
        """Quack"""
        ...
