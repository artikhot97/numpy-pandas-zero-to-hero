import pandas as pd
import os

csv_file_path = os.path.join(os.path.dirname(__file__), 'zomato_2.csv')

df = pd.read_csv(csv_file_path)

#Task 1: Print shape , column name and the dtype of each column in the DataFrame.
print(f"Shape of the DataFrame: {df.shape}")
print(f"\nColumn Names: {df.columns}")
print(f"\nData Types:")
print(df.dtypes)



#Task2 : show first 5 rows thenfull technical summary then numeric summary statistics of the DataFrame.
print("\nFirst 5 rows of the DataFrame:")
print(df.head())

print("\nTechnical Summary:")
print(df.info())

print("\nNumeric Summary Statistics:")
print(df.describe())



# Task 3: How many missing values are in each column? sort so the worst columns are on top isna() or isnull() can be used to find missing values. Use sum() to get the count of missing values in each column. Use sort_values() to sort the result in descending order.
missing_values = df.isnull().sum().sort_values(ascending=False)
print("\nMissing Values in Each Column:")
print(missing_values)


# Task 4: show the count of each unique value in listed_in(city) then do the same for online_order
print("\nCount of Unique Values in listed_in(city):")
print(df['listed_in(city)'].value_counts())

print("\nCount of Unique Values in online_order:")
print(df['online_order'].value_counts())


#Task 5: How many unique restutamt names are there ? how many unique locations? (Notice unique name  < total rows -> duplicates exist)
print(f"\nNumber of unique restaurant names: {df['name'].nunique()}")
print(f"\nNumber of unique locations: {df['listed_in(city)'].nunique()}")