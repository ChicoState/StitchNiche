import pytest
from src.utils import StitchCalculator
from src.utils import simple
import os

""" tests must start with "test_"
 test classes must start with "Test_"

"""

# access the calculators
Test_input = StitchCalculator()

# one dim
# happy tests
def test_one_dim_true():
    Test_input.setpattern(1,0,1,0)
    assert Test_input.one_dim_calculator(7.5,4.25,True) == 32
    assert (Test_input.pattern.smul,
            Test_input.pattern.srem,
            Test_input.pattern.rmul,
            Test_input.pattern.rrem) == (1,0,1,0)
    
def test_one_dim_false():
    Test_input.setpattern(1,0,1,0)
    assert Test_input.one_dim_calculator(7.5,4.25,False) == 32
    assert (Test_input.pattern.smul,
            Test_input.pattern.srem,
            Test_input.pattern.rmul,
            Test_input.pattern.rrem) == (1,0,1,0)
    
def test_one_dim_true_pat_change_small():
    Test_input.setpattern(3,1,2,4)
    assert (Test_input.pattern.smul,
            Test_input.pattern.srem,
            Test_input.pattern.rmul,
            Test_input.pattern.rrem) == (3,1,2,4)
   
    assert Test_input.one_dim_calculator(7.5,4.25,True) == 31

def test_one_dim_false_pat_change_small():
    Test_input.setpattern(3,1,2,4)
    assert (Test_input.pattern.smul,
            Test_input.pattern.srem,
            Test_input.pattern.rmul,
            Test_input.pattern.rrem) == (3,1,2,4)
    assert Test_input.one_dim_calculator(7.5,4.25,False) == 32

def test_one_dim_true_pat_change_large():
    Test_input.setpattern(5, 0, 2, 6)
    assert (Test_input.pattern.smul,
            Test_input.pattern.srem,
            Test_input.pattern.rmul,
            Test_input.pattern.rrem) == (5,0,2,6)
   
    assert Test_input.one_dim_calculator(7.5,4.25,True) == 30

def test_one_dim_false_pat_change_large():
    Test_input.setpattern(5, 0, 2, 6)
    assert (Test_input.pattern.smul,
            Test_input.pattern.srem,
            Test_input.pattern.rmul,
            Test_input.pattern.rrem) == (5,0,2,6)
    assert Test_input.one_dim_calculator(7.5,4.25,False) == 32

def test_one_dim_true_large():
    Test_input.setpattern(1,0,1,0)
    assert Test_input.one_dim_calculator(18.0,7.5,True) == 135
    assert (Test_input.pattern.smul,
            Test_input.pattern.srem,
            Test_input.pattern.rmul,
            Test_input.pattern.rrem) == (1,0,1,0)
    
def test_one_dim_false_large():
    Test_input.setpattern(1,0,1,0)
    assert Test_input.one_dim_calculator(18.0,7.5,False) == 135
    assert (Test_input.pattern.smul,
            Test_input.pattern.srem,
            Test_input.pattern.rmul,
            Test_input.pattern.rrem) == (1,0,1,0)
    
def test_one_dim_true_large_pat_change_small():
    Test_input.setpattern(3,1,2,4)
    assert (Test_input.pattern.smul,
            Test_input.pattern.srem,
            Test_input.pattern.rmul,
            Test_input.pattern.rrem) == (3,1,2,4)
   
    assert Test_input.one_dim_calculator(18.0,7.5,True) == 136

def test_one_dim_false_large_pat_change_small():
    Test_input.setpattern(3,1,2,4)
    assert (Test_input.pattern.smul,
            Test_input.pattern.srem,
            Test_input.pattern.rmul,
            Test_input.pattern.rrem) == (3,1,2,4)
    assert Test_input.one_dim_calculator(18.0,7.5,False) == 134
    
def test_one_dim_true_large_pat_change_large():
    Test_input.setpattern(5,0,2,6)
    assert (Test_input.pattern.smul,
            Test_input.pattern.srem,
            Test_input.pattern.rmul,
            Test_input.pattern.rrem) == (5,0,2,6)
   
    assert Test_input.one_dim_calculator(18.0,7.5,True) == 135

def test_one_dim_false_large_pat_change_large():
    Test_input.setpattern(5,0,2,6)
    assert (Test_input.pattern.smul,
            Test_input.pattern.srem,
            Test_input.pattern.rmul,
            Test_input.pattern.rrem) == (5,0,2,6)
    assert Test_input.one_dim_calculator(18.0,7.5,False) == 134

# sad tests 
def test_one_dim_true_sad():
    Test_input.setpattern(1,0,1,0)
    
    assert Test_input.one_dim_calculator(7.5,4.25,True) != 31 
    assert (Test_input.pattern.smul,
            Test_input.pattern.srem,
            Test_input.pattern.rmul,
            Test_input.pattern.rrem) != (1,1,1,0)
    
def test_one_dim_false_sad():
    Test_input.setpattern(1,0,1,0)
    assert  (Test_input.one_dim_calculator(7.5,4.25,False) != 31)
    assert (Test_input.pattern.smul,
            Test_input.pattern.srem,
            Test_input.pattern.rmul,
            Test_input.pattern.rrem) != (1,1,1,0)
    
def test_one_dim_true_pat_change_sad():
    Test_input.setpattern(3,1,2,4)
    assert (Test_input.pattern.smul,
            Test_input.pattern.srem,
            Test_input.pattern.rmul,
            Test_input.pattern.rrem) != (2,1,2,4)
   
    assert Test_input.one_dim_calculator(7.5,4.25,True) != 32

def test_one_dim_false_pat_change_sad():
    Test_input.setpattern(3,1,2,4)
    assert (Test_input.pattern.smul,
            Test_input.pattern.srem,
            Test_input.pattern.rmul,
            Test_input.pattern.rrem) != (2,1,2,4)
    assert Test_input.one_dim_calculator(7.5,4.25,False) != 31

# change width

# rectangle calc
def test_empty_rectangle():
    with pytest.raises(TypeError):
        Test_input.rectangle_calculator() 

def test_str_rectangle():
    with pytest.raises(TypeError):
        Test_input.rectangle_calculator("","","","")

# isValid
# happy tests
def test_isValid_int_true():
    msg=[]
    assert Test_input.isValid("1","int",msg) == True
    assert msg == []
    
def test_isValid_int_false():
    msg=[]
    assert Test_input.isValid("1.0","int",msg) == False
    assert msg[0] == "Number must be a positive integer!"

def test_isValid_float_true():
    msg=[]
    assert Test_input.isValid("1.0","float",msg) == True
    assert msg == []

def tests_isValid_float_false():
    msg=[]
    assert Test_input.isValid(".","float",msg) == False
    assert msg[0] == "Number must be a valid float!"

def test_isValid_misc():
    msg=[]
    assert Test_input.isValid("1","misc",msg) == False
    assert msg[0] == "Mode must be int or float"

# sad tests
def test_isValid_int_sad():
    msg=[]
    assert Test_input.isValid("1.0","int",msg) != True

def test_isValid_float_sad():
    msg=[]
    assert Test_input.isValid("1","float",msg) != False

def test_isValid_misc_sad():
    msg=[]
    assert Test_input.isValid("1","misc",msg) != True
