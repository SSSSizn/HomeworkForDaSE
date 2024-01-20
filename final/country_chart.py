import matplotlib.pyplot as plt
import pandas as pd

data = {
    'near': 212, 'russia': 50, 'indonesia': 36, 'congo': 35,
    'new': 29, 'brazil': 25, 'colombia': 23, 'canada': 21,
    'iran': 20, 'alaska': 19, 'sudan': 18, 'mexico': 17,
    'nepal': 17, 'republic': 17, 'venezuela': 16, 'south': 16,
    'afghanistan': 15, 'island': 14, 'democratic': 13, 'york': 13,
    'philippines': 12, 'nigeria': 11, 'papua': 10, 'guinea': 10,
    'pakistan': 10, 'iraq': 10, 'san': 9, 'california': 9, 'lake': 9,
    'china': 9, 'india': 9, 'puerto': 9, 'texas': 9, 'angola': 8,
    'port': 8, 'kenya': 8, 'moscow': 7, 'hawaii': 7, 'australia': 7,
    'el': 7, 'argentina': 7, 'city': 7, 'de': 7, 'ukraine': 7, 'rio': 7,
    'spain': 6, 'france': 6, 'turkey': 6, 'miles': 6, 'la': 6, 'peru': 6,
    'united': 6, 'tehran': 5, 'florida': 5, 'mount': 5, 'taiwan': 5,
    'colorado': 5, 'thailand': 5, 'quebec': 5, 'italy': 5, 'africa': 5,
    'algeria': 5, 'arab': 5, 'emirates': 5, 'air': 5, 'base': 5, 'bay': 5,
    'point': 4, 'sri': 4, 'lanka': 4, 'guyana': 4, 'pennsylvania': 4,
    'manila': 4, 'japan': 4, 'carolina': 4, 'chile': 4, 'missouri': 4,
    'arizona': 4, 'rico': 4, 'sao': 4,
}


filtered_data = {key: value for key, value in data.items() if key not in ['near', 'new', 'island', 'democratic', 'san', 'city', 'de', 'miles', 'la', 'united', 'mount', 'air', 'base', 'bay', 'point']}

df = pd.DataFrame(list(filtered_data.items()), columns=['Country', 'Count'])

df = df.sort_values(by='Count', ascending=False)

plt.figure(figsize=(8, 10))
plt.barh(df['Country'], df['Count'], color='skyblue')
plt.xlabel('Count')
plt.ylabel('Country')

plt.tight_layout()

plt.show()
