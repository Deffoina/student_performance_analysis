import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# Load data
df = pd.read_csv('data/students.csv')

# Preview
print("Dataset Preview:")
print(df.head())

# Average scores
print("\nAverage Scores:")
print(df[['math_score', 'reading_score', 'writing_score']].mean())

# By gender
print("\nAverage by Gender:")
print(df.groupby('gender').mean())

# Correlation
print("\nCorrelation:")
print(df.corr())

df[['math_score', 'reading_score', 'writing_score']].hist(bins=15)
plt.suptitle("Distribution of Scores")
plt.show()

df.groupby('gender')[['math_score', 'reading_score', 'writing_score']].mean().plot(kind='bar')
plt.title("Average Scores by Gender")
plt.show()

sns.heatmap(df.corr(), annot=True, cmap='coolwarm')
plt.title("Correlation Matrix")
plt.show()

import matplotlib.pyplot as plt

plt.plot([1,2,3,4], [10,20,25,30])
plt.title("Test Graph")
plt.show()

