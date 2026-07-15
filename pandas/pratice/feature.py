import pandas as pd
import os

csv_file_path = os.path.join(os.path.dirname(__file__), 'zomato_2.csv')

df = pd.read_csv(csv_file_path)

print(df.head())

df.rename(columns={'listed_in(city)': 'city', 'listed_in(type)': 'type', 'approx_cost(for two people)': 'cost_of_two', 'rate': 'rating'}, inplace=True)
df['cost_of_two'] = df['cost_of_two'].str.replace(',', '', regex=False)
df['cost_of_two'] = pd.to_numeric(df['cost_of_two'], errors='coerce')
print("\nCleaned 'cost_of_two' column:")
print(df['cost_of_two'].head())

print("\nRenamed Columns:")
print(df['cost_of_two'])



#Task 1: Create a new column 'cost_per_person' by dividing the 'cost_of_two' column by 2. This will give the average cost for one person.
df['cost_per_person'] = df['cost_of_two'] / 2
print("\nAdded 'cost_per_person' column:")
print(df[['cost_of_two', 'cost_per_person']].head())


#Cleaning the 'rating' column to ensure it is in a proper float format and handling non-numeric values.
df['rating'] = df['rating'].replace('NEW', pd.NA).replace('-', pd.NA)
df['rating'] = df['rating'].str.replace('/5', '', regex=False)
df['rating'] = pd.to_numeric(df['rating'], errors='coerce')
df['rating'] = df['rating'].fillna(df['rating'].median())

#Task 2: Create a new column 'rating_band' that categorizes the 'rating' column into bands: 'Poor' (0-2.5), 'Average' (2.5-3.5), 'Good' (3.5-4.5), and 'Excellent' (4.5-5). This will help in understanding the distribution of ratings in a more categorical manner.
df['rating_band'] = pd.cut(df['rating'], bins=[0, 2.5, 3.5, 4.5, 5], labels=['Poor', 'Average', 'Good', 'Excellent'])
print("\nAdded 'rating_band' column:")
print(df['rating_band'].head())


#Task 3: Create a new column 'num_cuisines' that counts the number of cuisines listed in the 'cuisines' column. This will help in understanding how diverse the food offerings are for each restaurant.
df['num_cuisines'] = df['cuisines'].str.split(',').str.len()
print("\nAdded 'num_cuisines' column:")
print(df[['cuisines', 'num_cuisines']].tail())


#Task 4: Create a new column 'main_cuisine' that extracts the first cuisine listed in the 'cuisines' column. This will help in identifying the primary cuisine offered by each restaurant.
df['main_cuisine'] = df['cuisines'].str.split(',').str[0].str.strip()
print("\nAdded 'main_cuisine' column:")
print(df[['cuisines', 'main_cuisine']].tail())

#Task 5: Create dummy variables for the 'listed_type' column. This will convert the categorical 'listed_type' column into multiple binary columns, making it easier to use in machine learning models.
# #pd.get_dummies() is used to convert categorical variable(s) into dummy/indicator variables. It creates a new column for each unique value in the specified column, with 1s and 0s indicating the presence of that value in each row. This is useful for machine learning algorithms that require numerical input.
# df = pd.get_dummies(df, columns=['listed_in(type)'], prefix='type', drop_first=True)
# print("\nAdded dummy variables for 'listed_type' column:")
# print(df.head())


print("\nFinal DataFrame with new features:")
print(df.head())
print(df['rating_band'])