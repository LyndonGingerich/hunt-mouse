"""Miscellaneous non-project-specific helpers"""

from math import hypot


def difference(x, y):
    return abs(x - y)


def distance(address1, address2):
    differences = [difference(coord1, coord2) for coord1, coord2 in zip(address1, address2)]
    return hypot(*differences)


def repeat_tuple(element, length):
    return tuple([element] * length)
