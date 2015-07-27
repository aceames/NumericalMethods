'''
Created on Jul 27, 2015

@author: aeames
'''
import scipy.optimize
from numpy import exp
from CONSTANTS import k_4_coefficients, k_6_coefficients, k_7_coefficients,\
    H_H2S_coefficients
# P = total pressure in psig
# T_F = temperature in farenheit 
# A_w = amine weight percent
# These are the known inputs from the data
# This function converts input into use-able form
def f(Input_Array,  k_1):
    #
    [P, T_F, A_w]   = Input_Array
    (P_H2S, T, M)   = inputs(P, T_F, A_w)
    k_4             = exp(Get_Poly_Fit(T, k_4_coefficients))
    k_6             = exp(Get_Poly_Fit(T, k_6_coefficients))
    k_7             = exp(Get_Poly_Fit(T, k_7_coefficients))
    H_H2S           = exp(Get_Poly_Fit(T, H_H2S_coefficients))
    #
    a               = float(1.0e-12)
    b               = 1.
    fa              = Residual(a, k_1, k_4, k_6, k_7, H_H2S, P_H2S, M)
    fb              = Residual(b, k_1, k_4, k_6, k_7, H_H2S, P_H2S, M)
    hydrogen_conc   = scipy.optimize.brenth(Residual, a, b, args=(k_1, k_4, k_6, k_7, H_H2S, P_H2S, M))
    A               = ((P_H2S*k_6*k_7)/H_H2S)*((1+(hydrogen_conc/k_7))/(hydrogen_conc**2))
    beta            = (1/M)*(A + (P_H2S/H_H2S))
    #
    return beta
#
#
#
def Get_Poly_Fit(In_temp, In_coefficients):
    return  In_coefficients[0]                   + \
            In_coefficients[1] * (1./In_temp)    + \
            In_coefficients[2] * (1./In_temp**2) + \
            In_coefficients[3] * (1./In_temp**3) + \
            In_coefficients[4] * (1./In_temp**4)
            
    
#
#
def inputs(P, T_F, A_w):
    P_H2S   = (P) * 51.7149326                  # partial pressure of H2S in mmHg
    T       = (T_F - 32)*(5 / 9) + 273.15       # Temperature in Kelvin
    M       = (A_w * 1000)/(100 * 105.14)       # Molar concentration of amine, right now for DGA
    return (P_H2S, T, M) 
#
#
#
#
# "Parameters:"
# K4 = float(7.55767e-14)
# K6 = float(2.22E-7)
# K7 = float(1.39E-13)
# HH2S = 14965.71015
# K1 = float(3.3432e-9)
# function to find hydrogen ion concentration
# basically equation 14 (corrected) modified A to be in terms of x
# x is hydrogen ion concentration
# H_plus_conc should equal x
def H_plus_func(x, k_1, k_4, k_6, k_7, H_H2S, P_H2S, M):
    
    try:
        AddTerm1    = (k_4/x)/(1.+(M/(k_1*(1.+(x/k_1)))))
        AddTerm2    = (P_H2S*k_6*k_7/H_H2S)*((1.+(x/k_7))/(x**2.))*(1./(1.+(M/(k_1*(1.+(x/k_1))))))*(1.+(k_7/(1.+x)))
        H_plus_conc = AddTerm1 + AddTerm2
    except TypeError:
        print "come on"
        print "come on"
        print "come on"
    return H_plus_conc
#
#
def Residual(x, k_1, k_4, k_6, k_7, H_H2S, P_H2S, M):
    G = H_plus_func(x, k_1, k_4, k_6, k_7, H_H2S, P_H2S, M) - x  #residual equation, G should be 0
    return G 
#
#
# 
# print "This is the equilibrium concentration of [H+]: %s" % residual_x
# A = ((P_H2S*K6*K7)/HH2S)*((1+(residual_x/K7))/(residual_x**2))
# print "Actual A is equal to %s." % A 
# beta = (1/M)*(A + (P_H2S/HH2S))
# print "The total loading is %s." % beta 
# wt_percent = (beta*M*34.0809*100)/(1000)
# print "Finally, the weight percent of hydrogen sulfide is %s percent." % wt_percent    