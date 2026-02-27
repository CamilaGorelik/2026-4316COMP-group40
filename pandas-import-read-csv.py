import pandas as pd

df = pd.read_csv("student_productivity_distraction_dataset_20000.csv")

print(df.head())
print(df.info())
print(df.describe())
print(df.isnull().sum())