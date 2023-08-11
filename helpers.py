"""Generic library functions."""

from math import hypot


def abs_difference(x, y):
    return abs(x - y)


def abs_difference_of_tuple(x):
    return abs_difference(*x)


def distance(address1, address2):
    return hypot(*map(abs_difference_of_tuple, zip(address1, address2)))
