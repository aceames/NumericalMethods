'''
Created on Jul 16, 2015

@author: aeames
'''
import numpy as np 
import os
from H2S_Solubility_Model import f , ln_k_1_function, ConvertInputs
from Overhead.Functions import LoadAmineDataFromCSV,\
    WriteOptimalCoefficientsToCSV
from scipy.optimize import curve_fit
#
#    Name the amine
#
AMINE_NAME      = "MDEA"
#
#    Load data from /Data directory
#
HOME_DIRECTORY  = os.getcwd()
DATA_DIRECTORY  = HOME_DIRECTORY + r"\Data"
os.chdir(DATA_DIRECTORY)
Y, X            = LoadAmineDataFromCSV(InFileName = AMINE_NAME + ".csv")
os.chdir(HOME_DIRECTORY)
#
#    Choose initial guesses foor the parameters
#
A_guess         = -2.0
b_guess         = -5.5e3
B_M_guess       = 1.
Initial_guess   = [A_guess, b_guess, B_M_guess]
#
#    Curve Fit the data using Levenberg-Marquardt algorithm,
#    The 
#
#print X

popt, pcov = curve_fit(f, X, Y, p0=Initial_guess)     
#
#    Write results to /Results directory
#
RESULTS_DIRECTORY   = HOME_DIRECTORY + r"\Results"
os.chdir(RESULTS_DIRECTORY)
WriteOptimalCoefficientsToCSV(InFileName    = AMINE_NAME + "_OptimalCoeffs.csv",
                              InPopt        = popt)
os.chdir(HOME_DIRECTORY)  
#   
#
#