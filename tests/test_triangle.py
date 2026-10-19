import math

import pytest

from figure import Figure
from triangle import Triangle


@pytest.mark.parametrize('sides, expected', [
    ((13, 14, 15), 84),
    ((3, 4, 5), 6),
    ((2, 2, 2), math.sqrt(3)),
])
def test_area(sides, expected):
    assert Triangle(*sides).area == pytest.approx(expected)


@pytest.mark.parametrize('sides, expected', [
    ((13, 14, 15), 42),
    ((3, 4, 5), 12),
    ((2, 2, 2), 6),
])
def test_perimeter(sides, expected):
    assert Triangle(*sides).perimeter == expected


@pytest.mark.parametrize('sides', [(0, 1, 1), (1, 0, 1), (1, 1, 0), (-1, 2, 2), (2, -2, 3)])
def test_raises_for_not_positive_sides(sides):
    with pytest.raises(ValueError):
        Triangle(*sides)


@pytest.mark.parametrize('sides', [(1, 2, 3), (3, 1, 2), (2, 1, 1), (5, 1, 1), (10, 4, 5)])
def test_raises_for_impossible_triangle(sides):
    with pytest.raises(ValueError):
        Triangle(*sides)


def test_triangle_is_figure():
    assert issubclass(Triangle, Figure)
