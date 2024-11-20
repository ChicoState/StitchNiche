import pytest
from src.utils import StitchPattern
import os

""" tests must start with "test_"
 test classes must start with "Test_"

"""

# test StitchPattern class
p = StitchPattern()

def test_init_default():
    assert p.smul == 1
    assert p.srem == 0
    assert p.rmul == 1
    assert p.rrem == 0

def test_init():
    p = StitchPattern(1, 2, 3, 4)
    assert p.smul == 1
    assert p.srem == 2
    assert p.rmul == 3
    assert p.rrem == 4

def test_set_pattern():
    p.setpattern(4, 3, 2, 1)
    assert p.smul == 4
    assert p.srem == 3
    assert p.rmul == 2
    assert p.rrem == 1

def test_full_save():
    matrix = [[1,0,1,0],[-1,1,-1,1]]
    assert p.full_save(matrix)

def test_encode():
    matrix = [[0,1,0,1],[-1,-1,-1,-1]]
    encoded = p.encode(matrix)
    assert encoded == "4,3,2,1\n-1,-1,-1,-1\n"

def test_decode():
    encoded = "4,3,2,1\n-1,-1,-1,-1\n"
    p.decode(encoded)
    assert p.smul == 4
    assert p.srem == 3
    assert p.rmul == 2
    assert p.rrem == 1
    assert p.pattern_matrix == [[-1,-1,-1,-1]]

def test_save():
    matrix = [[1,0,1,0],[1,-1,1,-1]]
    p.save(p.id, matrix)
    filename = "saved_patterns/"+p.id+".txt" # TODO:find way to duplicate filename 
    assert os.path.exists(filename)

def test_load():                            # same here ^^^^^
    assert True
