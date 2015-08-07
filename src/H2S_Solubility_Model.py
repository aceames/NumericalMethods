'''
Created on Jul 27, 2015

@author: aeames
'''
from scipy.optimize import brenth
from numpy import exp, zeros
from CONSTANTS import k_4_coefficients, k_6_coefficients, k_7_coefficients,\
    H_H2S_coefficients
# P = total pressure in psig
# T_F = temperature in fahrenheit 
# A_w = amine weight percent
# These are the known inputs from the data
# This function converts input into use-able form
def f(Input_Array, A, B, B_M):
    #
    [P, T_F, A_w]   = Input_Array
    (P_H2S, T, M)   = inputs(P, T_F, A_w)
    k_4             = exp(Get_Poly_Fit(T, k_4_coefficients))
    k_6             = exp(Get_Poly_Fit(T, k_6_coefficients))
    k_7             = exp(Get_Poly_Fit(T, k_7_coefficients))
    H_H2S           = exp(Get_Poly_Fit(T, H_H2S_coefficients))
    k_1             = exp(ln_k_1_function(T, M, A, B, B_M))
    #
    num_obvs        = len(P)
    #
    a               = zeros((num_obvs)) + float(1.0e-12)
    b               = zeros((num_obvs)) + 1.
    #
    fa              = Residual(a, A, B, B_M, T, k_4, k_6, k_7, H_H2S, P_H2S, M)
    fb              = Residual(b, A, B, B_M, T, k_4, k_6, k_7, H_H2S, P_H2S, M)
    hydrogen_conc   = brenth_array(Residual, a, b, unknown_args=(A, B, B_M), known_args=(T, k_4, k_6, k_7, H_H2S, P_H2S, M))
    Paper_A         = ((P_H2S*k_6*k_7)/H_H2S)*((1+(hydrogen_conc/k_7))/(hydrogen_conc**2))
    beta            = (1/M)*(Paper_A + (P_H2S/H_H2S))
    #
    return beta
#
#
#
def Get_Poly_Fit(In_temp, In_coefficients):
    return  In_coefficients[0]                   + \
            In_coefficients[1] * (1./(In_temp))    + \
            In_coefficients[2] * (1./(In_temp**2)) + \
            In_coefficients[3] * (1./(In_temp**3)) + \
            In_coefficients[4] * (1./(In_temp**4))
            
    
#
#
def inputs(P, T_F, A_w):
    P_H2S   = (P) * 51.7149326                  # partial pressure of H2S in mmHg
    T_C     = (((T_F) - 32)*(0.55555556))       # Temperature in Celsius
    T       = T_C + 273.15                      # Temperature in Kelvin
    M       = (A_w * 1000)/(100 * 119.163)      # Molar concentration of amine, right now for MDEA
    return (P_H2S, T, M) 
#
#
#
#
# function to find hydrogen ion concentration
# basically equation 14 (corrected) modified A to be in terms of x
# x is hydrogen ion concentration
# H_plus_conc should equal x
def H_plus_func(x, A, B, B_M, T, k_4, k_6, k_7, H_H2S, P_H2S, M):
    k_1             = exp(ln_k_1_function(T, M, A, B, B_M))
    D               = 1. + (M/(k_1*(1. + (x/k_1))))
    try:
        AddTerm1    = (k_4/x)/D
        AddTerm2    = ((P_H2S*k_6*k_7)/H_H2S)*((1.+(x/k_7))/(x**2.))*(1./D)*(1.+(k_7/(1.+x)))
        H_plus_conc = AddTerm1 + AddTerm2
    except TypeError:
        print "come on"
        print "come on"
        print "come on"
    return H_plus_conc
#
#
def Residual(x, A, B, B_M, T, k_4, k_6, k_7, H_H2S, P_H2S, M):
    G       = H_plus_func(x, A, B, B_M, T, k_4, k_6, k_7, H_H2S, P_H2S, M) - x  #residual equation, G should be 0
    return G 
#
#
#
def brenth_array(f, a, b, known_args=None, unknown_args=None):
    #
    '''
    NOTE: The known arguments and unknown arguments are concatenated 
          with the known arguments appearing first.
    '''  
    #
    assert(isinstance(known_args, tuple))
    assert(isinstance(unknown_args, tuple))
    #
    m           = a.shape[0]
    k           = len(known_args)
    l           = len(unknown_args)
    out_zeros   = zeros((m))
    temp_args   = zeros((k+l))
    #
    for bobross in range(l):
        temp_args[bobross]  = unknown_args[bobross]
    #
    for i in range(m):
        #
        a_i             = a[i]
        b_i             = b[i]
        assert(a_i > 0.0)
        #Get
        for j in range(k):
            temp_args[l+j]    = known_args[j][i]
        #
        arg_i           = tuple(temp_args)
        #
        out_zeros[i]    = brenth(Residual, a_i, b_i, args=arg_i)
    #   
    #
    return out_zeros
#
#
def ln_k_1_function(T, M, A, B, B_M):
    # parameters A, B, C, D, E of k_1 function
    return A + B*(T**-1) + B_M*(M**-1)