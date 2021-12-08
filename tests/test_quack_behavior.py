"""Test quach behaviors"""
from quack_behavior.mute_quack import MuteQuack
from quack_behavior.quack import Quack
from quack_behavior.squeak import Squeak


def test_mute_quack(capfd):
    """Test mute quack behavior"""
    MuteQuack().quack()
    out, _ = capfd.readouterr()
    assert out == "<< Silence >>\n"


def test_quack(capfd):
    """Test quack behavior"""
    Quack().quack()
    out, _ = capfd.readouterr()
    assert out == "Quack\n"


def test_squeak(capfd):
    """Test squeak behavior"""
    Squeak().quack()
    out, _ = capfd.readouterr()
    assert out == "Squeak\n"
