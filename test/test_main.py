'''Automates testing'''

import sys

import pytest

sys.path.append('..')
from gridmaus import main

# Test code

def adjust_coordinate_to_boundary():
    assert main.adjust_coordinate_to_boundary(1, 5) == 1
    assert main.adjust_coordinate_to_boundary(-1, 5) == 0
    assert main.adjust_coordinate_to_boundary(7, 5) == 5

def test_get_distance():
    assert main.get_distance((0, 0, 1), (0, 0, 0)) == 1
    assert main.get_distance((0, 7, 0), (0, 0, 0)) == 7
    assert main.get_distance((0, 0, 0), (0, 0, 0)) == 0

def test_get_velocity():
    assert main.get_velocity(goal=(0, 0, 0), from_address=(0, 0, 1), to_address=(0, 0, 2)) == -1
    assert main.get_velocity(goal=(0, 0, 0), from_address=(0, 0, 3), to_address=(0, 0, 2)) == 1
    assert main.get_velocity(goal=(0, 2, 0), from_address=(0, 1, 0), to_address=(0, 3, 0)) == 0

def test_rand_range():
    assert 0 <= main.rand_range(5) < 5

if __name__ == '__main__':
    pytest.main()
