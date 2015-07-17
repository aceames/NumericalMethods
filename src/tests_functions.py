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
    x_prime = np.matrix([[1], [2], [-3]])
    m = x.shape[0]
    m_prime = x_prime.shape[0]
    assert_equal(m, m_prime)
    H_x = HouseholderReflection(x, u)
    for i in range(m):
        assert_equal(x_prime[i, 0], H_x[i, 0])
    
