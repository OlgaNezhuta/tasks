from tasks.task1 import *


def test_01_some_triangle():
    result = Triangle(55, 55, 65)
    result2 = "The triangle with sides a = 55, b = 55, " \
                     "c = 65, has perimeter = 87.5 and square = 1442.0444471305314. " \
                     "This is the triangle with two equal sides"
    assert set(result.split()) == set(result2.split())




