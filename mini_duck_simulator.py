"""Main function"""
from ducks.mallard import MallardDuck
from ducks.model import ModelDuck
from fly_behavior.fly_rocket_powered import FlyRocketPowered


def main():
    """Main function"""

    mallard = MallardDuck()
    mallard.perform_quack()
    mallard.perform_fly()

    model = ModelDuck()
    model.perform_fly()
    model.set_fly_behavior(FlyRocketPowered())
    model.perform_fly()


if __name__ == "__main__":
    main()
