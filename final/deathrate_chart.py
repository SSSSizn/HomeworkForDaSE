import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('deathrate.csv')

bins = [0, 0.2, 0.4, 0.6, 0.8, 1.0]

deathrate_bins = pd.cut(df['DeathRate'], bins=bins, include_lowest=True)
deathrate_counts = deathrate_bins.value_counts(sort=False)

plt.figure(figsize=(8, 8))
plt.pie(deathrate_counts, labels=deathrate_counts.index, autopct='%1.1f%%', startangle=140)
plt.title('Death Rate Distribution')
plt.show()
