#import libraries
import pandas as pd
import numpy as np

#IMPORT DATA
#Read the New York Fire Department (FDNY) dataset
#fdny_original_df = pd.read_csv('C://Users/oysterable/Desktop/FDNY_Firehouse_Listing.csv')
fdny_original_df = pd.read_csv('/content/sample_data/FDNY_Firehouse_Listing.csv')


#VIEW THE CONTENT OF THE DATA

#view general content
print(fdny_original_df.describe)

#view summary
print(fdny_original_df.columns)
print(fdny_original_df.head(5))
print(fdny_original_df.shape)



# CLEAN DATA
#Skip importing the first row of the data, sometimes the first row contains the column names as well
#fdny_clean_df = pd.read_csv('/content/sample_data/FDNY_Firehouse_Listing.csv', skiprows=1)

fdny_clean_df = fdny_original_df[['FacilityName', 'FacilityAddress', 'Borough']]
print(fdny_clean_df.head(5))


#View data statistics with describe method
print(fdny_clean_df.describe())
print(fdny_clean_df.columns)



# ANALYZE DATA

#view index of dataset
fdny_clean_df.index

#count number of records
fdny_clean_df.count()

#view datatypes
fdny_clean_df.dtypes

#Group by Borough
groupby_borough = fdny_clean_df.groupby('Borough')
print('Number of Boroughs: \n\n',groupby_borough.size())

#type(groupby_borough)

#Select
fdny_info_manhattan_df = groupby_borough.get_group('Manhattan')
# type(fdny_info_manhattan_df)

#View FDNY information for Manhattan
fdny_info_manhattan_df


