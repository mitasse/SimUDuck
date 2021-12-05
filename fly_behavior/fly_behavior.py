"""Represent a fly behavior"""
from typing import Protocol


class FlyBehavior(Protocol):
    """Fly behavior protocol"""

    def fly(self) -> None:
        """Fly"""
        ...
