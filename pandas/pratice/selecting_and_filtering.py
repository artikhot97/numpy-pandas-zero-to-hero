import pandas as pd
import os

csv_file_path = os.path.join(os.path.dirname(__file__), 'zomato_2.csv')

df = pd.read_csv(csv_file_path)


# Task 1: select just the column name, rate , votes into a new df
new_df = df[['name', 'rate', 'votes']]
print(new_df)


# Task 2: select all rows where the location is BTM and store it in a new df
loc = df.loc[df['location']=='BTM']
print(loc)


#Task 3: select all rows where the location is BTM and online_order is Yes
new_res = df.loc[(df['online_order'] == 'Yes') & (df['book_table'] == 'Yes')]
print(new_res)



# Task 4: select all rows where the votes are greater than 1000 and store it in a new df
new_res = df[df['votes'] > 1000]
print(new_res)



# Task 5: select all rows where the location is either BTM or HSR or Koramangala 5th Block and store it in a new df
new_list = df[df['location'].isin(['BTM', 'HSR', 'Koramangala 5th Block'])]
print(new_list)


# Task 6: select all rows where the cuisines column contains the word 'Chinese' (case insensitive) and store it in a new df
new_res = df[df['cuisines'].str.contains('Chinese', case=False, na=False)]
print(new_res)


# Task 7: select all rows where the online_order is Yes and book_table is Yes and store it in a new df
new_res = df.query("online_order == 'Yes' and book_table == 'Yes'")
print(new_res)