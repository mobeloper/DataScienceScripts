#import libraries
import pandas as pd
import numpy as np

#IMPORT DATA
#Read the FAA (Federal Aviation Authority) dataset
#faa_original_df = pd.read_csv('C:\\faa_ai_prelim.csv')
faa_original_df = pd.read_csv('/content/sample_data/faa_ai_prelim.csv')


#KNOW THE DATA
#See ALL the columns present in the dataset
faa_original_df.columns

#view the first 5 observations
faa_original_df.head()

print('Original DATA: \n\n',faa_original_df.head())
#view the shape 
print(faa_original_df.shape)


########################################
#CLEAN DATA
########################################
#Select important columns
#Create a new data frame with only required columns
faa_required_df = faa_original_df[['LOC_STATE_NAME','RMK_TEXT','EVENT_TYPE_DESC',
                                    'ACFT_MAKE_NAME', 'ACFT_MODEL_NAME',
                                    'FLT_PHASE','FATAL_FLAG']]

#View the type of the object
type(faa_required_df)

#View the first 5 observations
print('VIEW REQUIRED DATA: \n\n', faa_required_df.head())
print(faa_required_df.shape)

#Remove useless rows
#Drop all observations where ACFT_MAKE_NAME (aircraft make name) is not available
faa_clean_df = faa_required_df.dropna(subset=['ACFT_MAKE_NAME'])

#Find the aircraft names types existing in the dataset
aircraft_types_df = faa_required_df.groupby('ACFT_MAKE_NAME')

#View the aircrafts
#CESSNA has the most frequent flights, 23
print('Grouped Aircrafts: \n\n', aircraft_types_df.size())

#View the new shape of the new dataframe

print('CLEANED DATA: \n\n',faa_clean_df.head())
#view the shape 
print(faa_clean_df.shape)


########################################
#FIX DATA
########################################
#Replace all NaN (Not available) in Fatal flag with 'No'
faa_clean_df['FATAL_FLAG'].fillna(value='No',inplace=True)


#View first 5 observations
print('FIXED DATA: \n\n', faa_clean_df.head())
#view the shape 
print(faa_clean_df.shape) 



########################################
#ANALYZE DATA
########################################
#Group dataset by fatal flag
fatal_flights_df = faa_clean_df.groupby('FATAL_FLAG')
fatal_flights_df.size()

#Get Aircrafts with fatality
fatality_aircrafts_df = fatal_flights_df.get_group('Yes')

#Display the observations where fatal flag is Yes
print('ANALYZED DATA: \n\n',fatality_aircrafts_df)
print(fatality_aircrafts_df.shape)


