import pandas as pd

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
