"""Generic library functions."""

from math import hypot


def difference(x, y):
    return abs(x - y)


def abs_difference_of_tuple(x):
    return difference(*x)


def distance(address1, address2):
    return hypot(*map(abs_difference_of_tuple, zip(address1, address2)))


def repeat_tuple(element, length):
    return tuple([element] * length)
