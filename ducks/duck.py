"""Represent a duck class"""
from abc import ABC, abstractmethod

from fly_behavior.fly_behavior import FlyBehavior
from quack_behavior.quack_behavior import QuackBehavior


class Duck(ABC):
    """Duck abstract base class"""

    fly_behavior: FlyBehavior
    quack_behavior: QuackBehavior

    @abstractmethod
    def display(self):
        """Display"""
        ...

    def perform_fly(self):
        """Perform fly"""
        self.fly_behavior.fly()

    def perform_quack(self):
        """Perform quack"""
        self.quack_behavior.quack()

    @staticmethod
    def swim():
        """Swim"""
        print("All ducks float, even decoys!")
