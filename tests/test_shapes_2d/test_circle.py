from math import pi

from shapes_2d import Circle


def test_diameter_of_circle():
    radius = 2
    circle = Circle(radius)

    assert circle.diameter == 4


def test_area_of_circle():
    radius = 2
    circle = Circle(radius)

    assert circle.area == pi * 4


def test_circumference_of_circle():
    radius = 2
    circle = Circle(radius)

    assert circle.circumference == 4 * pi
