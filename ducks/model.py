"""Represent a duck class"""
from dataclasses import dataclass

from fly_behavior.fly_no_way import FlyNoWay
from quack_behavior.quack import Quack

from ducks.duck import Duck


@dataclass
class ModelDuck(Duck):
    """Mallard concrete duck class"""

    quack_behavior = Quack()
    fly_behavior = FlyNoWay()

    def display(self) -> None:
        """Display"""
        print("I'm a model duck")
