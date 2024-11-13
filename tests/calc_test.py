import pytest
from src.utils import StitchCalculator
from src.utils import simple

""" tests must start with "test_"
 test classes must start with "Test_"

"""
# very simple example
def test_simple_int():
    assert simple(2) == 2

# access the calculators
Test_input = StitchCalculator()

# one dim
# two pass
def test_one_dim_int():
    assert Test_input.one_dim_calculator(7.5,4.25,True) == 32
    # assert Test_input.pattern == (1,0,1,0)

# two fail

# change width
# two pass
# two fail

# rectangle calc
def test_empty_rectangle():
    with pytest.raises(TypeError):
        Test_input.rectangle_calculator() 

def test_str_rectangle():
    with pytest.raises(TypeError):
        Test_input.rectangle_calculator("","","","")




  