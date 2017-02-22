#*******************************DataPrep.py**********************************
#
#  Assignment:      Week Five Assignment
#  Course:          CPSC 51100
#  Student:         Michael D Sloan
#  Date Created:    20-FEB-2017
#  Date Due:        26-FEB-2017
# 
#*******************************************************************************


#Imports and global declarations

import pandas as pd
from pandas import DataFrame, Series 

def main():
    #Local Declarations for Main
    data_file = "energy.csv"
    energy_data = DataFrame()
    
    output_header = "\n51100, Spring 2017\n"\
                + "Name:  Mike Sloan\n"\
                + "PROGRAMMING ASSIGNMENT #5"
                
    #Import CSV to a Dataframe and create original copy in memory
    energy_data = pd.read_csv(data_file,index_col=0,na_values='..')
    original_data = energy_data.copy(deep=True)
    
    
    #Drop Unnecessary Rows
    energy_data=energy_data.drop(['EU27total','OECDtotal','World'])
    
   #Transpose, Fill NA, and Retranspose energy_data 
   #Using ugly tranposition so I can use fillna.  Axis (row) methods
   #Are not yet implemented.
   
    a = energy_data.transpose()         #Transpose to columns
    a = a.fillna(a.mean(0), axis=0)     #Employ fillna over columns
    energy_data = a.transpose()         #Return to orginal format.
    
    
    
    
    #Prints Results
    print output_header
    print energy_data
    
    
  
    
    
#Executes Main Function

if __name__ == "__main__":
    main()
        #Loops through and counts the total rating values
    
