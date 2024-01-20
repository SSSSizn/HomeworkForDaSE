import pandas as pd

df = pd.read_csv('plane.csv')

df['Aboard'] = df['Aboard'].str.extract('(\d+)').astype(float)
df['Fatalities'] = df['Fatalities'].str.extract('(\d+)').astype(float)

df['DeathRate'] = df['Fatalities'] / df['Aboard']

df[['Aboard', 'Fatalities', 'DeathRate']].to_csv('deathrate.csv', index=False)

df[['Aboard', 'Fatalities', 'DeathRate']]
