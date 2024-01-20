import pandas as pd
from wordcloud import WordCloud
import matplotlib.pyplot as plt

df = pd.read_csv('reason.csv', header=None, names=['Keyword', 'Frequency'])

df['Frequency'] = pd.to_numeric(df['Frequency'], errors='coerce', downcast='integer')

df = df.dropna(subset=['Frequency'])

wordcloud = WordCloud(width=800, height=400, background_color='white', colormap='viridis', repeat=False).generate_from_frequencies(df.set_index('Keyword')['Frequency'].to_dict())

plt.figure(figsize=(10, 5))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')
plt.show()
