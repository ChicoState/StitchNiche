import pytest
from src.utils import PatternMatrix
import os

""" tests must start with "test_"
 test classes must start with "Test_"

"""

def test_get_matrix():
    matrix = [[0,0],[1,1]]
    color_value_map = {}

    for v in range(0,5):
        color_value_map[v] = ("test: ", (0, 0, 0, 0))
    p = PatternMatrix(matrix, color_value_map)
    assert p.get_matrix() == matrix


def test_value_to_color():
    matrix = [[0,0],[1,1]]
    color_value_map = {}

    for v in range(0,5):
        color_value_map[v] = ("test: ", (0, 0, 0, 0))
    p = PatternMatrix(matrix, color_value_map)
    assert p.value_to_color(0) == (0,0,0,0)

def test_change_color():
    matrix = [[0,0],[1,1]]
    color_value_map = {}

    for v in range(0,5):
        color_value_map[v] = ("test: ", (0, 0, 0, 0))
    p = PatternMatrix(matrix, color_value_map)
    p.change_color(p.children[0])
    assert p.get_matrix()[0][0] == 0

