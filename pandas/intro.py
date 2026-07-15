
import pandas as pd


# Introduction to Data Cleaning with Pandas


print(pd.__version__)


#Series is a one-dimensional labeled array capable of holding any data type (integers, strings, floating point numbers, Python objects, etc.). The axis labels are collectively referred to as the index. A Series is like a fixed-size dict in that you can get and set values by index label.


data = pd.Series([1,2,3,4,5], index=['a','b','c','d','e'])
print(data)

print(data['a'])  # Accessing a single value by index label


print('a' in data)  # Checking if an index label exists in the Series

print(data.keys())  # Getting the index labels of the Series

print(data.values)  # Getting the values of the Series

print(data.items())  # Getting the index-value pairs of the Series

print(list(data.items()))  # Converting the index-value pairs to a list

data['f'] = 9  # Adding a new value to the Series
print(data)


#Slices are a way to access a subset of elements from a Series or DataFrame. You can use slicing to select a range of index labels or positions.

data['a':'c']  # Slicing by index labels (inclusive of start, exclusive of end)
print(data[:'c'])


print(data[0:4])  # Slicing by index positions (inclusive of start, exclusive of end)


#Masking is a technique used to filter data based on certain conditions. In Pandas, you can create a boolean mask to select elements that meet specific criteria.

data[data>3]  # Masking to select values greater than 3
print(data[(data>3) & (data<5)])  # Masking to select values equal to 3 and less than 5


print(data[['a', 'b', 'c']])  # Selecting multiple values by index labels


#loc and iloc are two methods used for indexing and selecting data in Pandas. The loc method is label-based, meaning you use the index labels to select data, while the iloc method is integer position-based, meaning you use the integer positions of the rows or columns to select data.

print(data.loc['a':'c'])  # Using loc to select a single value by index label
print(data.iloc[0:4])  # Using iloc to select a single value by index position
