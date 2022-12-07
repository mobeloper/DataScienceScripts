#Demo for Pandas
import pandas as pd
import numpy as np

# CREATE SERIES FROM A LIST
#Create a list
data = list(('abcdefg'))
first_series = pd.Series(data)

#shows the index and the object
print(first_series)


#CREATE SERIES FROM SCALAR

#Create a float Scalar
scalar_ser = pd.Series(5.,index=['a','b','c','d','e','f'])

print(scalar_ser)



#CREATE SERIES FROM ndarray
countries = np.array(['Luxembourg','Mexico','Brazil','USA','South Korea','Norway'])
ndarray_series = pd.Series(countries) #dtype is object

print(ndarray_series)


#CREATE SERIES FROM DICTIONARY (key-value pair)
#create an array of random numbers
xx = np.random.rand(1,6)*10000
print(xx)
#convert ndarray to simple array (dictionary)
sample_gdp = xx.flatten()
print(sample_gdp)

country_gdp = pd.Series(sample_gdp,index=[countries]) #Add country name as label or index
print(country_gdp)


#Accessing data in Series
#Using functions loc, iloc, data element or index range

#access first element in series
print(country_gdp[0])

#access a range of first 3 elements
print(country_gdp[0:3])

#access data by lookup by name
print(country_gdp.loc['Mexico'])

#look up by index position
print(country_gdp.iloc[4])



#Vector Operations

first_vector = pd.Series([3,5,1,7,35,2,9],index=['a','b','c','d','e','f','g'])
second_vector = pd.Series([6,2,1.6,.6,3,40,1],index=['a','b','c','d','e','f','g'])

add_vectors = first_vector+second_vector

print(add_vectors)

