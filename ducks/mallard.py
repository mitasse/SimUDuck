"""Represent a duck class"""
from fly_behavior.fly_with_wings import FlyWithWings
from quack_behavior.quack import Quack

from ducks.duck import Duck


class MallardDuck(Duck):
    """Mallard concrete duck class"""

    quack_behavior = Quack()
    fly_behavior = FlyWithWings()

    def display(self):
        """Display"""
        print("I'm a real Mallard duck")
