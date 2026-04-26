import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('data/students.csv')

print("Dataset Preview:")
print(df.head())

# -------------------------
#  BASIC STATS
# -------------------------

print("\nAverage Scores:")
print(df[['math_score', 'reading_score', 'writing_score']].mean())

print("\nAverage by Gender:")
print(df.groupby('gender')[['math_score', 'reading_score', 'writing_score']].mean())

# -------------------------
#  GRAPHS 
# -------------------------

# 1. Distribution
df[['math_score', 'reading_score', 'writing_score']].hist(bins=15)
plt.suptitle("Distribution of Scores")
plt.show()

# 2. Average by gender
df.groupby('gender')[['math_score', 'reading_score', 'writing_score']].mean().plot(kind='bar')
plt.title("Average Scores by Gender")
plt.ylabel("Score")
plt.show()

print("\nAnalysis completed successfully!")
