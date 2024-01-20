from matplotlib import pyplot as plt
import pandas as pd
import seaborn as sns

x = range(2000,2025,1)
y = [63,58,55,62,46,45,38,43,51,46,40,36,26,25,23,18,23,15,18,13,8,9,6,4,1]

plt.plot(x,y)
plt.xlabel('year')
plt.ylabel('count')
plt.show()

months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
count = [73,49,67,50,71,60,75,84,63,63,66,52]
plt.bar(months, count, color='skyblue', edgecolor='black')
plt.xlabel('month')
plt.ylabel('count')
plt.show()


hourly_counts = [12, 15, 14, 9, 14, 7, 26, 40, 48, 47, 44, 48, 42, 35, 46, 50, 43, 28, 34, 32, 18, 10, 17, 15]
data = pd.DataFrame({'Hour': range(24), 'Counts': hourly_counts})
plt.figure(figsize=(12, 2))
sns.heatmap(data[['Counts']].T, cmap='YlGnBu', annot=True, fmt='g', cbar_kws={'label': 'Counts'}, xticklabels=24)
plt.xlabel('time in a day')
plt.title('count')
plt.show()