import pytest

from circle import Circle
from figure import Figure
from rectangle import Rectangle
from square import Square
from triangle import Triangle

ALL_FIGURES = [
    Square(3),
    Rectangle(2, 5),
    Triangle(3, 4, 5),
    Circle(2),
]


def test_figure_cannot_be_instantiated():
    with pytest.raises(TypeError):
        Figure()


def test_add_area_returns_sum_of_areas():
    square = Square(10)
    triangle = Triangle(13, 14, 15)
    assert triangle.add_area(square) == 184


@pytest.mark.parametrize('other', ALL_FIGURES)
@pytest.mark.parametrize('figure', ALL_FIGURES)
def test_add_area_works_for_any_figures(figure, other):
    assert figure.add_area(other) == figure.area + other.area


@pytest.mark.parametrize('not_a_figure', [10, 3.14, 'square', None, [Square(1)]])
def test_add_area_raises_for_not_figure(not_a_figure):
    with pytest.raises(ValueError):
        Square(2).add_area(not_a_figure)
