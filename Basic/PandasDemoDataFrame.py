import pandas as pd
import numpy as np

#Create DataFrame from List
olympic_data_list = {
    'HostCity':['London', 'Beijin'],
    'Year': ['2012','2008'],
    'Participating Countries': [205,204]
}
olympic_data_list

olympic_dataframe = pd.DataFrame(olympic_data_list)
olympic_dataframe

#view a dataframe
olympic_dataframe.HostCity

#view entire content
olympic_dataframe.describe

#Create DataFrame from Dictionary of Dicts
olympic_data_dict = {
    'London':{2012:205},
    'Beijin':{2008:204}
}

dataframe_dict = pd.DataFrame(olympic_data_dict)
dataframe_dict

#Create DataFrame from Series

year_array = [205,204,201]
country_array = ['London','Beijin','Athens']
idx_array = [2012,2008,2004]

participation_series = pd.Series(year_array,index=[idx_array])
country_series = pd.Series(country_array,index=[idx_array])

dict_series = {
    'Participating Countries': participation_series,
    'HostCities': country_series
}

dataframe_series = pd.DataFrame(dict_series)
dataframe_series

#Create DataFrame from ndArray
ndarr = np.array([2012,2008,2004])

ndarr_dict = {
    'year':ndarr
}

df_ndarr = pd.DataFrame(ndarr_dict)
df_ndarr

#Create DataFrame from DataFrame

df_from_df = pd.DataFrame(dataframe_series)
df_from_df

