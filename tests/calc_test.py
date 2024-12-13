import pytest
from src.utils import StitchCalculator
from src.utils import simple
import os

""" tests must start with "test_"
 test classes must start with "Test_"

"""
# very simple example
def test_simple_int():
    assert simple(2) == 2

# access the calculators
Test_input = StitchCalculator()

# one dim
# passing tests
def test_one_dim_true_pass1():
    Test_input.setpattern(1,0,1,0)
    assert Test_input.one_dim_calculator(7.5,4.25,True) == 32
    assert (Test_input.pattern.smul,
            Test_input.pattern.srem,
            Test_input.pattern.rmul,
            Test_input.pattern.rrem) == (1,0,1,0)
    
def test_one_dim_false_pass1():
    Test_input.setpattern(1,0,1,0)
    assert Test_input.one_dim_calculator(7.5,4.25,False) == 32
    assert (Test_input.pattern.smul,
            Test_input.pattern.srem,
            Test_input.pattern.rmul,
            Test_input.pattern.rrem) == (1,0,1,0)
    
def test_one_dim__true_pat_change_pass1():
    Test_input.setpattern(3,1,2,4)
    assert (Test_input.pattern.smul,
            Test_input.pattern.srem,
            Test_input.pattern.rmul,
            Test_input.pattern.rrem) == (3,1,2,4)
   
    assert Test_input.one_dim_calculator(7.5,4.25,True) == 31

def test_one_dim_false_pat_change_pass1():
    Test_input.setpattern(3,1,2,4)
    assert (Test_input.pattern.smul,
            Test_input.pattern.srem,
            Test_input.pattern.rmul,
            Test_input.pattern.rrem) == (3,1,2,4)
    assert Test_input.one_dim_calculator(7.5,4.25,False) == 32

def test_one_dim__true_pat_change_pass1v2():
    Test_input.setpattern(5, 0, 2, 6)
    assert (Test_input.pattern.smul,
            Test_input.pattern.srem,
            Test_input.pattern.rmul,
            Test_input.pattern.rrem) == (5,0,2,6)
   
    assert Test_input.one_dim_calculator(7.5,4.25,True) == 30

def test_one_dim_false_pat_change_pass1v2():
    Test_input.setpattern(5, 0, 2, 6)
    assert (Test_input.pattern.smul,
            Test_input.pattern.srem,
            Test_input.pattern.rmul,
            Test_input.pattern.rrem) == (5,0,2,6)
    assert Test_input.one_dim_calculator(7.5,4.25,False) == 32

def test_one_dim_true_pass2():
    Test_input.setpattern(1,0,1,0)
    assert Test_input.one_dim_calculator(18.0,7.5,True) == 135
    assert (Test_input.pattern.smul,
            Test_input.pattern.srem,
            Test_input.pattern.rmul,
            Test_input.pattern.rrem) == (1,0,1,0)
    
def test_one_dim_false_pass2():
    Test_input.setpattern(1,0,1,0)
    assert Test_input.one_dim_calculator(18.0,7.5,False) == 135
    assert (Test_input.pattern.smul,
            Test_input.pattern.srem,
            Test_input.pattern.rmul,
            Test_input.pattern.rrem) == (1,0,1,0)
    
def test_one_dim__true_pat_change_pass2():
    Test_input.setpattern(3,1,2,4)
    assert (Test_input.pattern.smul,
            Test_input.pattern.srem,
            Test_input.pattern.rmul,
            Test_input.pattern.rrem) == (3,1,2,4)
   
    assert Test_input.one_dim_calculator(18.0,7.5,True) == 136

def test_one_dim_false_pat_change_pass2():
    Test_input.setpattern(3,1,2,4)
    assert (Test_input.pattern.smul,
            Test_input.pattern.srem,
            Test_input.pattern.rmul,
            Test_input.pattern.rrem) == (3,1,2,4)
    assert Test_input.one_dim_calculator(18.0,7.5,False) == 134
    
def test_one_dim__true_pat_change_pass2v2():
    Test_input.setpattern(5,0,2,6)
    assert (Test_input.pattern.smul,
            Test_input.pattern.srem,
            Test_input.pattern.rmul,
            Test_input.pattern.rrem) == (5,0,2,6)
   
    assert Test_input.one_dim_calculator(18.0,7.5,True) == 135

def test_one_dim_false_pat_change_pass2v2():
    Test_input.setpattern(5,0,2,6)
    assert (Test_input.pattern.smul,
            Test_input.pattern.srem,
            Test_input.pattern.rmul,
            Test_input.pattern.rrem) == (5,0,2,6)
    assert Test_input.one_dim_calculator(18.0,7.5,False) == 134

# failing tests 
def test_one_dim_true_fail():
    Test_input.setpattern(1,0,1,0)
    assert Test_input.one_dim_calculator(7.5,4.25,True) == 31
    assert (Test_input.pattern.smul,
            Test_input.pattern.srem,
            Test_input.pattern.rmul,
            Test_input.pattern.rrem) == (1,0,1,0)
    
def test_one_dim_false_fail():
    Test_input.setpattern(1,0,1,0)
    assert Test_input.one_dim_calculator(7.5,4.25,False) == 31
    assert (Test_input.pattern.smul,
            Test_input.pattern.srem,
            Test_input.pattern.rmul,
            Test_input.pattern.rrem) == (1,0,1,0)
    
def test_one_dim__true_pat_change_fail():
    Test_input.setpattern(3,1,2,4)
    assert (Test_input.pattern.smul,
            Test_input.pattern.srem,
            Test_input.pattern.rmul,
            Test_input.pattern.rrem) == (3,1,2,4)
   
    assert Test_input.one_dim_calculator(7.5,4.25,True) == 32

def test_one_dim_false_pat_change_fail():
    Test_input.setpattern(3,1,2,4)
    assert (Test_input.pattern.smul,
            Test_input.pattern.srem,
            Test_input.pattern.rmul,
            Test_input.pattern.rrem) == (3,1,2,4)
    assert Test_input.one_dim_calculator(7.5,4.25,False) == 31

# change width

# rectangle calc
def test_empty_rectangle():
    with pytest.raises(TypeError):
        Test_input.rectangle_calculator() 

def test_str_rectangle():
    with pytest.raises(TypeError):
        Test_input.rectangle_calculator("","","","")


# isValid
# passing tests
def test_isValid_int_pass():
    msg=[]
    assert Test_input.isValid("1","int",msg) == True
    assert msg == []
    
def test_isValid_int_pass2():
    msg=[]
    assert Test_input.isValid("1.0","int",msg) == False
    assert msg[0] == "Number must be a positive integer!"

def test_isValid_float_pass():
    msg=[]
    assert Test_input.isValid("1.0","float",msg) == True
    assert msg == []

def tests_isValid_float_pass2():
    msg=[]
    assert Test_input.isValid(".","float",msg) == False
    assert msg[0] == "Number must be a valid float!"

def test_isValid_misc_pass():
    msg=[]
    assert Test_input.isValid("1","misc",msg) == False
    assert msg[0] == "Mode must be int or float"

# failing tests
def test_isValid_int_fail():
    msg=[]
    assert Test_input.isValid("1.0","int",msg) == True

def test_isValid_float_fail():
    msg=[]
    assert Test_input.isValid("1","float",msg) == False

def test_isValid_misc_fail():
    msg=[]
    assert Test_input.isValid("1","misc",msg) == True
