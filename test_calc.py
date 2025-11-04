import pytest_

from calc import additation, subtract, multiply, divide

def test_additation ():
    #compare actual output with expected output
    assert add(2, 3) == 5

def test_substract():
    assert sub(3, 1) == 2

def test_multiply():
    assert multiply(4, 2) == 8

def test_divide():
    assert divide(4, 2) == 2    