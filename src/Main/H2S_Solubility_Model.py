'''
Created on Jul 27, 2015

@author: aeames
'''
from scipy.optimize import brenth
from numpy import exp, zeros
from Overhead.Constants import k_4_coefficients, k_6_coefficients, k_7_coefficients,\
    H_H2S_coefficients
# P = total pressure in psig
# T_F = temperature in fahrenheit 
# A_w = amine weight percent
# These are the known inputs from the data
# This function converts input into use-able form
def f(Input_Array, A, B, B_M):
    '''
    This function calculates total loading from H2S partial pressure,
    temperature, and amine concentration
    Inputs:
        - Input_Array        :: 4xN NDARRAY    :: Contains 4 rows of inputs
            - Input_Array[0] :: NDARRAY        :: Temperatures
            - Input_Array[1] :: NDARRAY        :: H2S Partial Pressures
            - Input_Array[2] :: NDARRAY        :: Amine Weight Percent
            - Input_Array[3] :: NDARRAY        :: Amine Molar Mass
        - A                  :: FLOAT          :: Guess for C0 (constant in fit)
        - B                  :: FLOAT          :: Guess for C1 (T^-1 param in fit)
        - B_M                :: FLOAT          :: Guess for C2 (M param in fit)
    Outputs:
        - beta               :: NDARRAY        :: Predicted loading for all N cases
    '''
    #
    #    Convert from inputs:
    #    from ... psi,  Fahrenheit, and weight percent 
    #    to   ... mmHg, Kelvin,     and molar
    #
    [T_F, P, A_w, Amm]  = Input_Array
    (P_H2S, T, M)       = ConvertInputs(P, T_F, A_w, Amm)
    #
    #    Retrieve values of the equilibrium constants and Henry's
    #    Law at a given temperature per the polynomial fits in 
    #    Abu-Arabi's paper
    #
    k_4                 = exp(Get_Poly_Fit(T, k_4_coefficients))
    k_6                 = exp(Get_Poly_Fit(T, k_6_coefficients))
    k_7                 = exp(Get_Poly_Fit(T, k_7_coefficients))
    H_H2S               = exp(Get_Poly_Fit(T, H_H2S_coefficients))
    #
    num_obvs        = len(P)
    #
    #    Estimate bounding values on H2 concentration
    #
    a               = zeros((num_obvs)) + float(1.0e-16)
    b               = zeros((num_obvs)) + 1.
    #
    #    Find H2 concentration
    #
    hydrogen_conc   = brenth_array(Residual, a, b, unknown_args=(A, B, B_M), known_args=(T, k_4, k_6, k_7, H_H2S, P_H2S, M))
    #
    #    Infer loading from H2 concentration per Abu-Arabi's paper
    #    (in which he defines the parameter A)
    #
    Paper_A         = ((P_H2S*k_6*k_7)/H_H2S)*((1+(hydrogen_conc/k_7))/(hydrogen_conc**2))
    beta            = (1/M)*(Paper_A + (P_H2S/H_H2S))
    #
    return beta
#
#
#
def Get_Poly_Fit(In_temp, In_coefficients):
    '''
    Return value of polynomial fit given coefficients of 
    some parameter for a 4th order polynomial in T^-1
    Inputs:
        - In_Temp            :: NDARRAY        :: Temperatures for calc in Kelvin
        - In_coefficients    :: len-5 NDARRAY  :: Coefficients 0 - 4 of poly-fit
    Outputs:
        - K4, K6, K7, H_H2S  :: NDARRAY        :: Result depends on input coeffs
    '''
    return  In_coefficients[0]                   + \
            In_coefficients[1] * (1./(In_temp))    + \
            In_coefficients[2] * (1./(In_temp**2)) + \
            In_coefficients[3] * (1./(In_temp**3)) + \
            In_coefficients[4] * (1./(In_temp**4))
            
    
#
#
def ConvertInputs(P, T_F, A_w, Amm):
    '''
    Converts units of inputs
    Inputs:
        - P        :: NDARRAY    :: H2S Partial Pressure in psi
        - T_F      :: NDARRAY    :: Temperature in Fahrenheit
        - A_w      :: NDARRAY    :: Amine weight percent
        - Amm      :: NDARRAY    :: Amine molar mass
    Outputs:
        - P_H2S    :: NDARRAY    :: H2S Partial Pressure in mmHg
        - T        :: NDARRAY    :: Temeprature in Kelvin
        - M        :: NDARRAY    :: Amine concentration in molar
    '''
    P_H2S   = (P) * 51.7149326                      # partial pressure of H2S in mmHg
    T_C     = (((T_F) - 32)*(0.55555556))           # Temperature in Celsius
    T       = T_C + 273.15                          # Temperature in Kelvin
    M       = (A_w * 1000)/(100 * Amm)              # Molar concentration of amine, right now for MDEA
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
    for i in range(l):
        temp_args[i]  = unknown_args[i]
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
        try:
            out_zeros[i]    = brenth(Residual, a_i, b_i, args=arg_i)
        except:
            AAA = Residual(a_i, arg_i[0], 
                                arg_i[1], 
                                arg_i[2], 
                                arg_i[3], 
                                arg_i[4], 
                                arg_i[5], 
                                arg_i[6], 
                                arg_i[7], 
                                arg_i[8], 
                                arg_i[9])
            
            B = Residual(b_i,   arg_i[0], 
                                arg_i[1], 
                                arg_i[2], 
                                arg_i[3], 
                                arg_i[4], 
                                arg_i[5], 
                                arg_i[6], 
                                arg_i[7], 
                                arg_i[8], 
                                arg_i[9])
            print AAA, B
    #   
    #
    return out_zeros
#
#
def ln_k_1_function(T, M, A, B, B_M):
    # parameters A, B, C, D, E of k_1 function
    return A + B*(T**-1) + B_M*(M)