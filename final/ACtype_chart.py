import pandas as pd
from wordcloud import WordCloud
import matplotlib.pyplot as plt

df = pd.read_csv('ACtype.csv', header=None, names=['Phrase', 'Frequency'])

df['Frequency'] = pd.to_numeric(df['Frequency'], errors='coerce', downcast='integer')

df = df.dropna(subset=['Frequency'])

grouped_df = df.groupby('Phrase')['Frequency'].sum().reset_index()

text = ' '.join([(str(row['Phrase']) + ' ') * int(row['Frequency']) for index, row in grouped_df.iterrows()])

wordcloud = WordCloud(width=800, height=400, background_color='white').generate(text)

plt.figure(figsize=(10, 5))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')
plt.show()
