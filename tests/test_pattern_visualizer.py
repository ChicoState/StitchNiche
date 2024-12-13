import pytest
from src.utils import PatternVisualizer
import os

""" tests must start with "test_"
 test classes must start with "Test_"

"""

def test_get_matrix():
    matrix = [[0,0],[1,1]]
    color_value_map = {}

    for v in range(0,5):
        color_value_map[v] = ("test: ", (0, 0, 0, 0))
    p = PatternVisualizer(matrix, color_value_map)
    assert p.get_matrix() == matrix
