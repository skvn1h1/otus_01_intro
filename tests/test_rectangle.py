import pytest

from figure import Figure
from rectangle import Rectangle


def test_rectangle():
    r = Rectangle(3, 5)
    assert r.area == 15


@pytest.mark.parametrize('sides, expected', [
    ((2, 7), 14),
    ((10, 10), 100),
    ((2.5, 4), 10),
])
def test_area_with_different_sides(sides, expected):
    assert Rectangle(*sides).area == expected


@pytest.mark.parametrize('sides, expected', [
    ((3, 5), 16),
    ((10, 10), 40),
    ((2.5, 4), 13),
])
def test_perimeter(sides, expected):
    assert Rectangle(*sides).perimeter == expected


@pytest.mark.parametrize('sides', [(0, 5), (5, 0), (-1, 5), (5, -2), (-3, -3)])
def test_raises_for_not_positive_sides(sides):
    with pytest.raises(ValueError):
        Rectangle(*sides)


def test_rectangle_is_figure():
    assert issubclass(Rectangle, Figure)
