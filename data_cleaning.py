import pandas as pd

df = pd.read_csv('zillow.csv')
#df = pd.read_csv('zillow.csv', index_col=0)
#df.columns = ['price', 'bedrooms', 'bathrooms', 'floorsize', 'address']
#df.to_csv('zillow.csv', index=False)

#delelte unusable data points
df = df[df['bathrooms'] != '-- ba']
df = df[df['floorsize'] != '-- sqft']
df = df[df['floorsize'] != '1 sqft']
df = df[df['address'].apply(lambda x: len(x.split(','))) == 3]

# property price
price = df['price'].apply(lambda x: x.replace('$', ''))
price = price.apply(lambda x: x.replace(',', ''))
price = price.apply(lambda x: int(x.replace('+', '')))

#number of bedrooms
bd = df['bedrooms'].apply(lambda x: x.replace('Studio', '0'))
bd = bd.apply(lambda x: int(x.split(' ')[0]))

#number of bathrooms
ba = df['bathrooms'].apply(lambda x: float(x.split(' ')[0]))

#property floorsize
area = df['floorsize'].apply(lambda x: x.replace('sqft', ''))
area = area.apply(lambda x: int(x.replace(',', '')))

#city name
city = df['address'].apply(lambda x: x.split(',')[1])
city = city.apply(lambda x: x.replace(' ', ''))

#zipcode number
zipcode = df['address'].apply(lambda x: x.split(',')[2])
zipcode = zipcode.apply(lambda x: int(x.split(' ')[2]))

#making the cleaned dataframe
df_clean = pd.DataFrame()
df_clean['price'] = price
df_clean['bedrooms'] = bd
df_clean['bathrooms'] = ba
df_clean['floorsize'] = area
df_clean['city'] = city
df_clean['zipcode'] = zipcode

df_clean.to_csv('zillow_clean.csv', index=False)