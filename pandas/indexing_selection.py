import pandas as pd


area = pd.Series({'California': 423967, 'Texas': 695662,
                  'New York': 141297, 'Florida': 170312,
                  'Illinois': 149995})
pop = pd.Series({'California': 38332521, 'Texas': 26448193,
                 'New York': 19651127, 'Florida': 19552860,
                 'Illinois': 12882135})
data = pd.DataFrame({'area':area, 'pop':pop})

print(data)
print("----------------------------------------------------------")

print(data['area'])  # Accessing a single column by column label
# print(data.area)


print(data['area']['California'])  # Accessing a single value by column and index label

print(data.area is data['area'])  # Checking if two ways of accessing a column return the same object


print("**********************************************************")
print(data.area)

# print("----------------------------------------------------------")
print(data['area'])



data['density'] = data['pop'] / data['area']

print(data.values)  # Getting the values of the DataFrame


print(data.T)  # Transposing the DataFrame (swapping rows and columns)

print(data['area'])


print(data.iloc[:3, :2])  # Selecting a subset of rows and columns using iloc

print("----------------------------------------------------------")
print(data.loc[:'Florida', :'pop'])  # Selecting a subset of rows and columns using loc


#Its deprecated in newer versions of pandas, so it is commented out to avoid errors. You can use loc or iloc instead.
# print(data.ix[:3, :'pop'])  # Selecting a subset of rows and columns using ix (deprecated in newer versions of pandas)


