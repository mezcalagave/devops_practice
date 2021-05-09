import pytest
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from functions import plus, minus, multiply, divide

def test_plus():
    assert plus(1,2)== 3

def test_minus():
    assert minus(3,1)== 2

def test_multiply():
    assert multiply(3,2)== 6

def test_divide():
    assert divide(4,2)== 2.0