"""Represent a duck class"""
from dataclasses import dataclass

from fly_behavior.fly_with_wings import FlyWithWings
from quack_behavior.quack import Quack

from ducks.duck import Duck


@dataclass
class MallardDuck(Duck):
    """Mallard concrete duck class"""

    quack_behavior = Quack()
    fly_behavior = FlyWithWings()

    def display(self) -> None:
        """Display"""
        print("I'm a real Mallard duck")
