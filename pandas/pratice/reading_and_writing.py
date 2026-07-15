import pandas as pd
import os

csv_file_path = os.path.join(os.path.dirname(__file__), 'zomato_2.csv')

print(f"Reading CSV file from: {csv_file_path}")
# df = pd.read_csv(csv_file_path)
# print(df)

print("\nDataFrame Info:")
# print(df.info())


print("\nDataFrame Description:")
# print(df.describe())


#Task 1: Read the CSV file into a DataFrame but load only the first 4 columns: 'name', 'age', 'city', and 'country'. Print the first 5 rows of the DataFrame.
# df = pd.read_csv(csv_file_path, usecols=['name', 'rate', 'votes', 'location'])
# print(df)


#Task 2: Read only first 1000 rows of the CSV file into a DataFrame. Print the shape of the DataFrame.
df_first_1000 = pd.read_csv(csv_file_path, nrows=1000)
print(df_first_1000.shape)
# print(f"\nShape of the DataFrame with first 1000 rows: {df_first0_1000.shape}")



#Task 3 : read the csv in chunks of 5000 an print how many chunck there are in the csv file , pluse the totle row count( sum of len of each chunk)
df_chunks = pd.read_csv(csv_file_path, chunksize=5000)
chunk_count = 0
total_rows = 0
for chunk in df_chunks:
    chunk_count += 1
    total_rows += len(chunk)
print(f"\nTotal number of chunks: {chunk_count}")
print(f"Total number of rows in the CSV file: {total_rows}")


