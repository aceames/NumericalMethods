'''
Created on Aug 7, 2015

@author: jcochran
'''
#
#
#
from csv import DictReader, DictWriter
from numpy import asarray
#
#
#
def LoadAmineDataFromCSV(InFileName = None):
    '''
    Reads data from a CSV file for the parameter fitting routine. The
    program assumes that the Y-data is in first position (column 0).
    Inputs:
        - InFileName    :: STRING    :: Name of file containing the data
    Outputs:
        - X, Y          :: NDARRAY   :: The dependent and independent variables from data
    '''
    #
    X       = []
    Y       = []
    #
    with open(InFileName, 'rb') as csvfile:
        #
        TEMP_READER     = DictReader(csvfile, delimiter=',')
        #
        for row in TEMP_READER:
            #
            #    Assumes the data has headers that match the labels used below
            #
            Y.append( float(row["Loading"])                                                 )
            X.append( [float(row["Temperature"]),           float(row["Pressure"])          , 
                       float(row["Amine Weight Percent"]),  float(row["Amine Molar Mass"])] )
            #
        #
    #
    return asarray(Y), asarray(X).transpose()
#
#
#
def WriteOptimalCoefficientsToCSV(InFileName    = None, 
                                  InPopt        = None, 
                                  InPcov        = None):
    #
    with open(InFileName, 'wb') as csvfile:
        #
        n           = len(InPopt)
        FIELD_NAMES = ["C%i"%i for i in range(n)]
        OUTPUT_DICT = {}
        #
        #    Compile outputs as a dictionary
        #
        for i in range(n):
            #
            OUTPUT_DICT[FIELD_NAMES[i]] = InPopt[i]
            #
        #
        TEMP_WRITER = DictWriter(csvfile, delimiter=',', fieldnames=FIELD_NAMES)
        #
        TEMP_WRITER.writeheader()
        TEMP_WRITER.writerow(OUTPUT_DICT)
        #
    #
    #
    return
