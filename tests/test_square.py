import pytest

from figure import Figure
from rectangle import Rectangle
from square import Square


@pytest.mark.parametrize('side, expected', [
    (1, 1),
    (5, 25),
    (10, 100),
    (2.5, 6.25),
])
def test_area(side, expected):
    assert Square(side).area == expected


@pytest.mark.parametrize('side, expected', [
    (1, 4),
    (5, 20),
    (10, 40),
    (2.5, 10),
])
def test_perimeter(side, expected):
    assert Square(side).perimeter == expected


@pytest.mark.parametrize('side', [0, -1, -10])
def test_raises_for_not_positive_side(side):
    with pytest.raises(ValueError):
        Square(side)


def test_square_is_rectangle():
    assert issubclass(Square, Rectangle)


def test_square_is_figure():
    assert issubclass(Square, Figure)
