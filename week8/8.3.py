import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.datasets import load_iris

iris = load_iris()
data = iris.data
target = iris.target
target_names = iris.target_names
df = pd.DataFrame(data, columns=iris.feature_names)
df['species'] = target_names[target]

# 散点图
plt.figure(figsize=(12, 5))
plt.subplot(1, 3, 1)
sns.scatterplot(x='sepal length (cm)', y='sepal width (cm)', hue='species', data=df)
plt.title('Scatter Plot')

# 小提琴图
plt.subplot(1, 3, 2)
sns.violinplot(x='species', y='petal length (cm)', data=df)
plt.title('Violin Plot')

# 热图
plt.subplot(1, 3, 3)
df['species_code'] = df['species'].astype('category').cat.codes
correlation_matrix = df.drop('species', axis=1).corr()
sns.heatmap(correlation_matrix, annot=True)
plt.title('Heatmap')

plt.tight_layout()
plt.show()
