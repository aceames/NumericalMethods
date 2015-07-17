'''
Created on Jul 17, 2015

@author: aeames
'''
from nose.tools import *
import numpy as np
from Functions import HouseholderReflection
#
def test_HouseholderReflection():
    x = np.matrix([[1], [2], [3]])
    u = np.matrix([[0], [0], [1]])
    x_prime = np.matrix([1], [2], [-3])
    assert_equal(HouseholderReflection(x, u), x_prime)
    
def test_H():
    assert_equal()

def test_QRFactorization():
    assert_equal()
    
def test_QR():
    assert_equal()