from tasks.task1 import *


def test_01_triangle_with_two_equal_sides():
    result = str(Triangle(55, 55, 65))
    result2 = "The triangle with sides a = 55, b = 55, " \
                     "c = 65, has perimeter = 87.5 and square = 1442.0444471305314. " \
                     "This is the triangle with two equal sides"
    assert set(result.split()) == set(result2.split())


def test_02_equal_triangle():
    result = str(Triangle(55, 55, 55))
    result2 = "The triangle with sides a = 55, b = 55, c = 55, has perimeter = 82.5 " \
              "and square = 1309.8634232239635. This is the equal triangle"
    assert set(result.split()) == set(result2.split())


def test_03_scalene_triangle():
    result = str(Triangle(55, 65, 75))
    result2 = "The triangle with sides a = 55, b = 65, c = 75, has perimeter = 97.5 and" \
              " square = 1740.7231794573197. This is the scalene triangle"
    assert set(result.split()) == set(result2.split())


def test_04_scalene_triangle():
    result = str(Triangle(-1, 0, -18))
    result2 = "The triangle with sides a = -1, b = 0, c = -18, has perimeter = -9.5 and" \
              " square = (4.944511451557439e-15+80.75j). This is the scalene triangle"
    assert set(result.split()) == set(result2.split())


def test_05_equal_triangle():
    result = str(Triangle(0, 0, 0))
    result2 = "The triangle with sides a = 0, b = 0, c = 0, has perimeter = 0.0 and" \
              " square = 0.0. This is the equal triangle"
    assert set(result.split()) == set(result2.split())

