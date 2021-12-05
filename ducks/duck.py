"""Represent a duck class"""
from abc import ABC, abstractmethod

from fly_behavior.fly_behavior import FlyBehavior
from quack_behavior.quack_behavior import QuackBehavior


class Duck(ABC):
    """Duck abstract base class"""

    def __init__(self) -> None:
        self.fly_behavior: FlyBehavior
        self.quack_behavior: QuackBehavior

    @abstractmethod
    def display(self) -> None:
        """Display"""
        ...

    def set_fly_behavior(self, fly_behavior: FlyBehavior) -> None:
        """Set fly behavior"""
        self.fly_behavior = fly_behavior

    def set_quack_behavior(self, quack_behavior: QuackBehavior) -> None:
        """Set quack behavior"""
        self.quack_behavior = quack_behavior

    def perform_fly(self) -> None:
        """Perform fly"""
        self.fly_behavior.fly()

    def perform_quack(self) -> None:
        """Perform quack"""
        self.quack_behavior.quack()

    @staticmethod
    def swim() -> None:
        """Swim"""
        print("All ducks float, even decoys!")
