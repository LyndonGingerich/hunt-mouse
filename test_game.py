'''Automates testing'''

import pytest

import game

# Test code

# def test_convert_movement_address():
#     assert game.convert_movement_address(('+', '-', '')) == (1, -1, 0)

# def test_get_distance():
#     assert game.get_distance((0, 0, 1), (0, 0, 0)) == 1
#     assert game.get_distance((0, 7, 0), (0, 0, 0)) == 7
#     assert game.get_distance((0, 0, 0), (0, 0, 0)) == 0
#     assert game.get_distance((0, 0, 0), (1, 1, 1)) == 3 ** 0.5

# def test_get_velocity():
#     assert game.get_velocity(goal=(0, 0, 0), from_address=(0, 0, 1), to_address=(0, 0, 2)) == -1
#     assert game.get_velocity(goal=(0, 0, 0), from_address=(0, 0, 3), to_address=(0, 0, 2)) == 1
#     assert game.get_velocity(goal=(0, 2, 0), from_address=(0, 1, 0), to_address=(0, 3, 0)) == 0

if __name__ == '__main__':
    pytest.main()
