"""Main function"""
from ducks.mallard import MallardDuck


def main():
    """Main function"""

    mallard = MallardDuck()
    mallard.perform_quack()
    mallard.perform_fly()
    mallard.swim()
    mallard.display()


if __name__ == "__main__":
    main()
