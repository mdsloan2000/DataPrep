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

pd.options.display.float_format = '{:.6f}'.format
    

continent = {u'Australia':'Australia',
             u'Austria':'Europe',
             u'Belgium':'Europe',
             u'Canada':'North America',
             u'Chile':'South America',
             u'CzechRepublic':'Europe',
             u'Denmark':'Europe',
             u'Estonia':'Europe',
             u'Finland':'Europe',
             u'France':'Europe',
             u'Germany':'Europe',
             u'Greece':'Europe',
             u'Hungary':'Europe',
             u'Iceland':'Europe',
             u'Ireland':'Europe',
             u'Israel':'Asia',
             u'Italy':'Europe',
             u'Japan':'Asia',
             u'Korea':'Asia',
             u'Luxembourg':'Europe',
             u'Mexico':'North America',
             u'Netherlands':'Europe',
             u'NewZealand':'Oceania',
             u'Norway':'Europe',
             u'Poland':'Europe',
             u'Portugal':'Europe',
             u'SlovakRepublic':'Europe',
             u'Slovenia':'Europe',
             u'Spain':'Europe',
             u'Sweden':'Europe',
             u'Switzerland':'Europe',
             u'Turkey':'Asia',
             u'UnitedKingdom':'Europe',
             u'UnitedStates':'North America',
             u'Brazil':'South America',
             u'China':'Asia',
             u'India':'Asia',
             u'Indonesia':'Asia',
             u'RussianFederation':'Europe',
             u'SouthAfrica':'Africa' }

def main():
    #Local Declarations for Main
    data_file = "energy.csv"
    energy_data = DataFrame()
    summary_columns = ['num_countries',\
                        'mean',\
                        'small',\
                        'avg', \
                        'large']
    world_stats = {'world_mean'       : 0,\
                   'world_stdev'      : 0}
    
    output_header = "\n51100, Spring 2017\n"\
                + "Name:  Mike Sloan\n"\
                + "PROGRAMMING ASSIGNMENT #5"
                
    #Import CSV to a Dataframe and create original copy in memory
    energy_data = pd.read_csv(data_file,index_col=0,na_values='..')
    original_data = energy_data.copy(deep=True)
    
    
    #Drop Unnecessary Rows
    energy_data=energy_data.drop(['EU27total','OECDtotal','World'])
    
   #Transpose, Fill NA, and repeat transpose energy_data 
   #Using ugly tranposition so I can use fillna.  Axis (row) methods
   # are not yet implemented.
   
    a = energy_data.transpose()         #Transpose to columns
    a = a.fillna(a.mean(0), axis=0)     #Employ fillna over columns
    energy_data = a.transpose()         #Return to orginal format.
    
    
    #Add additional column and populate it from the dictionary of 
    # country.contienent pairs.
    for j, country in enumerate(energy_data.index) :
        energy_data.loc[country,'Continent'] = continent[country]
    
    #Build Summary Dataframe - by grabbing unique continets
    rows=(energy_data['Continent'].unique())
    #rows.sort()
    energy_summary = DataFrame(index = rows, columns=summary_columns)
    
    world_stats['world_mean'] = (energy_data.mean(axis=1)).mean(axis=0)
    world_stats['world_stdev'] = (energy_data.mean(axis=1)).std(axis=0) 
    
    for k, summary_continent in enumerate(energy_summary.index) :
        local_small = 0
        local_avg   = 0
        local_large = 0

        energy_summary.loc[summary_continent, 'num_countries'] \
         = len(energy_data[energy_data['Continent']==summary_continent])
        continental_mean = round((energy_data.loc[energy_data['Continent'] \
         == summary_continent].mean(axis=1)).mean(axis=0), 6)
        energy_summary.loc[summary_continent, 'mean'] = continental_mean
        if (continental_mean < world_stats['world_mean']-world_stats['world_stdev']) :
            local_small = 1
        else :
            if (continental_mean > world_stats['world_mean'] + world_stats['world_stdev']) :
                local_large = 1
            else :
                local_avg = 1
               
        energy_summary.loc[summary_continent, 'small'] = local_small
        energy_summary.loc[summary_continent, 'avg'] = local_avg
        energy_summary.loc[summary_continent, 'large'] = local_large  
    
    #Sort Dataframe
    energy_summary.sort_values(['num_countries','mean'], \
                                axis=0, \
                                ascending=False, \
                                inplace=True)    
     
    print output_header
    print energy_summary
 
    
    
  
    
    
#Executes Main Function

if __name__ == "__main__":
    main()
        #Loops through and counts the total rating values
    
