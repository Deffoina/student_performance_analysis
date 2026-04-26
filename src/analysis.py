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
print(df.groupby('gender')[['math_score', 'reading_score', 'writing_score']].mean())

# Correlation
print("\nCorrelation:")
print(df.corr())

# -------------------------
#  GRAPHS SECTION
# -------------------------

# 1. Distribution of scores
df[['math_score', 'reading_score', 'writing_score']].hist(bins=15)
plt.suptitle("Distribution of Scores")
plt.show()

# 2. Average scores by gender
df.groupby('gender')[['math_score', 'reading_score', 'writing_score']].mean().plot(kind='bar')
plt.title("Average Scores by Gender")
plt.ylabel("Score")
plt.show()

# 3. Correlation heatmap
sns.heatmap(df.corr(), annot=True, cmap='coolwarm')
plt.title("Correlation Matrix")
plt.show()

print("\nAnalysis completed successfully!")
