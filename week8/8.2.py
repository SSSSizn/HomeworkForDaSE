import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
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
colors = {'setosa': 'red', 'versicolor': 'green', 'virginica': 'blue'}
plt.scatter(df['sepal length (cm)'], df['sepal width (cm)'], c=df['species'].map(colors))
plt.title('Scatter Plot')
plt.xlabel('sepal length (cm)')
plt.ylabel('sepal width (cm)')

# 小提琴图
plt.subplot(1, 3, 2)
sns.violinplot(x='species', y='petal length (cm)', data=df)
plt.title('Violin Plot')

# 热图
plt.subplot(1, 3, 3)
df['species_code'] = df['species'].astype('category').cat.codes
correlation_matrix = df.drop(['species', 'species_code'], axis=1).corr()
plt.imshow(correlation_matrix, interpolation='none')
plt.colorbar()
plt.xticks(np.arange(len(correlation_matrix.columns)), correlation_matrix.columns, rotation=90)
plt.yticks(np.arange(len(correlation_matrix.columns)), correlation_matrix.columns)
plt.title('Heatmap')
plt.tight_layout()
plt.show()
