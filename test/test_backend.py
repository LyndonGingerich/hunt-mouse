'''Automates testing'''

import sys

import pytest

sys.path.append('..')
from gridmaus.gridmaus import backend

# Test code

def test_adjust_to_boundaries():
    assert backend.adjust_to_boundaries(1, 5) == 1
    assert backend.adjust_to_boundaries(-1, 5) == 0
    assert backend.adjust_to_boundaries(7, 5) == 5

def test_get_difference():
    assert backend.get_difference(10, 7) == 3

def test_get_distance():
    assert backend.get_distance((0, 0, 1), (0, 0, 0)) == 1
    assert backend.get_distance((0, 7, 0), (0, 0, 0)) == 7
    assert backend.get_distance((0, 0, 0), (0, 0, 0)) == 0

def test_get_velocity():
    assert backend.get_velocity(goal=(0, 0, 0), address1=(0, 0, 1), address2=(0, 0, 2)) == -1
    assert backend.get_velocity(goal=(0, 0, 0), address1=(0, 0, 3), address2=(0, 0, 2)) == 1
    assert backend.get_velocity(goal=(0, 2, 0), address1=(0, 1, 0), address2=(0, 3, 0)) == 0

def test_rand_range():
    assert 0 <= backend.rand_range(5) < 5

if __name__ == '__main__':
    pytest.main()
