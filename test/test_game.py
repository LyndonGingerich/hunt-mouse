'''Automates testing'''

import pytest

import game

# Test code

def test_adjust_address_to_boundaries():
    assert game.adjust_address_to_boundaries((1, 1, 5), 3) == (1, 1, 3)

def test_adjust_coordinate_to_boundary():
    assert game.adjust_coordinate_to_boundary(1, 5) == 1
    assert game.adjust_coordinate_to_boundary(-1, 5) == 0
    assert game.adjust_coordinate_to_boundary(7, 5) == 5

def test_get_distance():
    assert game.get_distance((0, 0, 1), (0, 0, 0)) == 1
    assert game.get_distance((0, 7, 0), (0, 0, 0)) == 7
    assert game.get_distance((0, 0, 0), (0, 0, 0)) == 0
    assert game.get_distance((0, 0, 0), (1, 1, 1)) == (2 ** 0.5) ** 3

def test_get_velocity():
    assert game.get_velocity(goal=(0, 0, 0), from_address=(0, 0, 1), to_address=(0, 0, 2)) == -1
    assert game.get_velocity(goal=(0, 0, 0), from_address=(0, 0, 3), to_address=(0, 0, 2)) == 1
    assert game.get_velocity(goal=(0, 2, 0), from_address=(0, 1, 0), to_address=(0, 3, 0)) == 0

if __name__ == '__main__':
    pytest.main()
