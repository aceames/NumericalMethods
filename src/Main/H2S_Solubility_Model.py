'''
Created on Jul 27, 2015

@author: aeames
'''
from scipy.optimize import brenth
from numpy import exp, zeros
from Overhead.Constants import k_4_coefficients, k_6_coefficients, k_7_coefficients,\
    H_H2S_coefficients
#
#
#
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
    P_H2S   = (P) * 51.7149326                      
    T_C     = (((T_F) - 32)*(0.55555556))           
    T       = T_C + 273.15                          
    M       = (A_w * 1000)/(100 * Amm)              
    return (P_H2S, T, M) 
#
#
#
#

def H_plus_func(x, A, B, B_M, T, k_4, k_6, k_7, H_H2S, P_H2S, M):
    '''
    Find the concentration of H+ in solution, Equation # in Section 7 of Technical Report.
    Inputs:
        - x             :: NDARRAY      :: H2 concentration
        - A             :: FLOAT        :: Guess for C0 (constant in fit)
        - B             :: FLOAT        :: Guess for C1 (T^-1 param in fit)
        - B_M           :: FLOAT        :: Guess for C2 (M param in fit)
        - T             :: NDARRAY      :: Temperature in Kelvin
        - k_4           :: NDARRAY      :: Equilibrium Constant
        - k_6           :: NDARRAY      :: Equilibrium Constant
        - k_7           :: NDARRAY      :: Equilibrium Constant
        - H_H2S         :: NDARRAY      :: Henry's Law Constant
        - P_H2S         :: NDARRAY      :: Partial Pressure of H2S in mmHg
        - M             :: NDARRAY      :: Molar Amine Concentration
    Outputs:
        -H_plus_conc    :: NDARRAY      :: H2 concentration
    '''
    #
    # Calculate k_1 equilibrium constant with parameter guesses
    #
    k_1             = exp(ln_k_1_function(T, M, A, B, B_M))
    #
    # Calculated a term that appears twice in the denominator of the expression
    #
    D               = 1. + (M/(k_1*(1. + (x/k_1))))
    #
    # Terms added to find H2 concentration
    # from Abu-Arabi equation 14
    #
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
    '''
    Function for residual, G should be 0 to find true H2 value.
    Abu-Arabi equation 14 set equal to 0. 
    Inputs:
        - x             :: NDARRAY      :: H2 concentration
        - A             :: FLOAT        :: Guess for C0 (constant in fit)
        - B             :: FLOAT        :: Guess for C1 (T^-1 param in fit)
        - B_M           :: FLOAT        :: Guess for C2 (M param in fit)
        - T             :: NDARRAY      :: Temperature in Kelvin
        - k_4           :: NDARRAY      :: Equilibrium Constant
        - k_6           :: NDARRAY      :: Equilibrium Constant
        - k_7           :: NDARRAY      :: Equilibrium Constant
        - H_H2S         :: NDARRAY      :: Henry's Law Constant
        - P_H2S         :: NDARRAY      :: Partial Pressure of H2S in mmHg
        - M             :: NDARRAY      :: Molar Amine Concentration
    Outputs:
        -G              :: NDARRAY      :: Value of Residual, should be 0
    '''
    
    G       = H_plus_func(x, A, B, B_M, T, k_4, k_6, k_7, H_H2S, P_H2S, M) - x  
    return G 
#
#
#
def brenth_array(f, a, b, known_args=None, unknown_args=None):
    #
    '''
    Applies brenth root-finding method to an array.
    Inputs:
        - f             :: FUNCTION        :: A function in NDARRAY that we need the root of
        - a             :: NDARRAY         :: Lower bound
        - b             :: NDARRAY         :: Upper bound
        - known_args    :: TUPLE           :: T, k_4, k_6, k_7, H_H2S, P_H2S, M
        - unkown_args   :: TUPLE           :: A, B, B_M
    Output:
        -out_zeros      :: NDARRAY         :: Roots of function f
    NOTE: The known arguments and unknown arguments are concatenated 
          with the known arguments appearing first.
    '''  
    #
    assert(isinstance(known_args, tuple))
    assert(isinstance(unknown_args, tuple))
    #
    # m is the number of rows of a
    #
    m           = a.shape[0]
    #
    # k is the number of elements in known_args
    #
    k           = len(known_args)
    #
    # l is the number of elements in unknown args
    #
    l           = len(unknown_args)
    #
    # out_zeros is an array with m rows
    #
    out_zeros   = zeros((m))
    #
    # temp_args is an array with k+1 rows
    #
    temp_args   = zeros((k+l))
    #
    # begin with the ith element of temp_args and unknown_args being the same
    #
    for i in range(l):
        temp_args[i]  = unknown_args[i]
    #
    # access the elements of a and b
    #
    for i in range(m):
        #
        a_i             = a[i]      
        b_i             = b[i]      
        assert(a_i > 0.0)
        #
        for j in range(k):
            temp_args[l+j]    = known_args[j][i]
        #
        arg_i           = tuple(temp_args)
        #
        # use brenth on the ith value of each argument then update out_zero
        # to create an array of all of the zeros
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
    ''' Function of equilibrium constant K1 to be optimized.
    Inputs:
        - T             :: NDARRAY      :: Temperature in Kelvin
        - M             :: NDARRAY      :: Molar Amine Concentration
        - A             :: FLOAT        :: Guess for C0 (constant in fit)
        - B             :: FLOAT        :: Guess for C1 (T^-1 param in fit)
        - B_M           :: FLOAT        :: Guess for C2 (M param in fit)
    Outputs:
        -ln_k_1         :: NDARRAY      :: Natural log of K1 at each temperature and concentration
    '''
    #
    ln_k_1              = A + B*(T**-1) + B_M*(M)
    #
    return ln_k_1
#
#