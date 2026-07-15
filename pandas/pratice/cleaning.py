import pandas as pd
import os


csv_file_path = os.path.join(os.path.dirname(__file__), 'zomato_2.csv')

df = pd.read_csv(csv_file_path)


# Task 1: Rename the columns 'listed_in(city)' to 'city', 'listed_in(type)' to 'type', 'approx_cost(for two people)' to 'cost_of_two', and 'rate' to 'rating'.
df.rename(columns={'listed_in(city)': 'city', 'listed_in(type)': 'type', 'approx_cost(for two people)': 'cost_of_two', 'rate': 'rating'}, inplace=True)
print("\nRenamed Columns:")
print(df.columns)


#Task 2: Drop the columns 'url', 'address', 'phone', and 'menu_item' from the DataFrame as they are not necessary for analysis.
df.drop(columns=['url', 'address', 'phone', 'menu_item'], inplace=True)
print("\nDataFrame after dropping unnecessary columns:")
print(df.head())



# Task 3: Check for duplicate rows in the DataFrame and drop them if any exist. Print the number of duplicate rows found and dropped.
duplicate_drops = df.duplicated().sum()
print(f"\nNumber of duplicate rows in the DataFrame: {duplicate_drops}")
df.drop_duplicates(inplace=True)
print(f"\nNumber of duplicate rows dropped: {duplicate_drops}")



#Task 4 : Clean 'rating' column it has values like '4.1/5' and 'NEW', '-' , 'NaN. Trun it into a proper float e.g 4.1 non-numeric -> NaN
df['rating'] = df['rating'].replace('NEW', pd.NA).replace('-', pd.NA)
df['rating'] = df['rating'].str.replace('/5', '', regex=False)
df['rating'] = pd.to_numeric(df['rating'], errors='coerce')
print("\nCleaned 'rating' column:")
print(df['rating'].tail())


# Task 5: Clean 'cost_of_two' column it has values like '₹1,200' and '₹500' and 'NaN'. Remove the currency symbol and commas, then convert it to a numeric type. Non-numeric values should be converted to NaN.
df['cost_of_two'] = df['cost_of_two'].str.replace(',', '', regex=False)
df['cost_of_two'] = pd.to_numeric(df['cost_of_two'], errors='coerce')
print("\nCleaned 'cost_of_two' column:")
print(df['cost_of_two'].head())


# Task 6: Fill missing values in the 'rating' column with the median rating value. This will help to maintain the overall distribution of ratings in the dataset.
#Why median is used instead of mean? Because median is less affected by outliers and skewed data, making it a better measure of central tendency for filling missing values in this context.

df['rating'] = df['rating'].fillna(df['rating'].median())
print("\nFilled missing values in 'rating' column with median:")
print(df['rating'].tail())
print(df['rating'].isnull().sum())  # Check for any remaining missing values in 'rating' column


# Task 7: Convert the 'online_order' and 'book_table' columns to boolean values (True/False) instead of 'Yes'/'No'. This will make it easier to work with these columns in analysis and modeling.
df['online_order'] = df['online_order'].replace({'Yes': 1, 'No': 0})
df['book_table'] = df['book_table'].replace({'Yes': 1, 'No': 0})
print("\nConverted 'online_order' and 'book_table' columns to boolean:")
print(df[['online_order', 'book_table']].head())


df['location'] = df['location'].str.strip().str.title()  # Remove leading/trailing whitespace from 'location' column
print("\nCleaned 'location' column:")
print(df['location'].head())


print("\nFinal cleaned DataFrame:")
print(df.head())