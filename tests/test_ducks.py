"""Test ducks"""
from ducks.mallard import MallardDuck
from ducks.model import ModelDuck


def test_mallard(capfd):
    """Test mallard duck"""
    MallardDuck().display()
    out, _ = capfd.readouterr()
    assert out == "I'm a real Mallard duck\n"


def test_model(capfd):
    """Test model duck"""
    ModelDuck().display()
    out, _ = capfd.readouterr()
    assert out == "I'm a model duck\n"
