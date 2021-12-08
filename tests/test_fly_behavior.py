"""Test fly bahaviors"""
from fly_behavior.fly_no_way import FlyNoWay
from fly_behavior.fly_rocket_powered import FlyRocketPowered
from fly_behavior.fly_with_wings import FlyWithWings


def test_fly_with_wings(capfd):
    """Test fly with wings behavior"""
    FlyWithWings().fly()
    out, _ = capfd.readouterr()
    assert out == "I'm flying!!\n"


def test_fly_rocket_powered(capfd):
    """Test fly rocket powered behavior"""
    FlyRocketPowered().fly()
    out, _ = capfd.readouterr()
    assert out == "I 'm flying with a rocket!\n"


def test_fly_no_way(capfd):
    """Test fly no way behavior"""
    FlyNoWay().fly()
    out, _ = capfd.readouterr()
    assert out == "I can't fly\n"
