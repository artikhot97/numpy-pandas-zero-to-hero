
import pandas as pd
import os

csv_file_path = os.path.join(os.path.dirname(__file__), 'zomato_2.csv')

df = pd.read_csv(csv_file_path)

print(df.head(2))


print(df.columns)

df.rename(columns={'listed_in(city)': 'city', 'listed_in(type)': 'type', 'approx_cost(for two people)': 'cost_of_two', 'rate': 'rating'}, inplace=True)

df['rating'] = df['rating'].replace('NEW', pd.NA).replace('-', pd.NA).replace('nan', pd.NA).replace("", pd.NA)
df['rating'] = df['rating'].str.replace('/5', '', regex=False)
df['rating'] = pd.to_numeric(df['rating'], errors='coerce')


#Task 1 : Average rating of restaurants in each location. This will help in understanding which locations have better-rated restaurants on average.
print(df.groupby('location')['rating'].mean().sort_values(ascending=False))


# Task 2 : Count of restaurants in each location. This will help in understanding the distribution of restaurants across different locations.
print(df['city'].value_counts())


# Task 3 : Average cost for two people in each restaurant type. This will help in understanding the pricing trends across different types of restaurants.

df['cost_of_two'] = df['cost_of_two'].str.replace(',', '', regex=False)
df['cost_of_two'] = pd.to_numeric(df['cost_of_two'], errors='coerce')

print(df.groupby('rest_type').agg(
    avg_cost=('cost_of_two', 'mean'),
    max_cost=('cost_of_two', 'max'),
    n=('name', 'count')
).sort_values(ascending=False, by='avg_cost')
)


#Task 4: average Rating grouped by BOTH online order and table book
print(df.groupby(['online_order', 'book_table']).mean().sort_values(ascending=False, by='rating').head(10))


# df.groupby(['main_']).agg(
#     avg = ('rating', 'mean'),
#     n=(('cuisines', 'count') and (n>= 50)
# ).sort_values(ascending=False, by='rating')