import math

import pytest

from circle import Circle
from figure import Figure


@pytest.mark.parametrize('radius, expected', [
    (1, math.pi),
    (2, math.pi * 4),
    (2.5, math.pi * 6.25),
])
def test_area(radius, expected):
    assert Circle(radius).area == pytest.approx(expected)


@pytest.mark.parametrize('radius, expected', [
    (1, 2 * math.pi),
    (2, 4 * math.pi),
    (2.5, 5 * math.pi),
])
def test_perimeter(radius, expected):
    assert Circle(radius).perimeter == pytest.approx(expected)


@pytest.mark.parametrize('radius', [0, -1, -0.5])
def test_raises_for_not_positive_radius(radius):
    with pytest.raises(ValueError):
        Circle(radius)


def test_circle_is_figure():
    assert issubclass(Circle, Figure)
