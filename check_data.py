import pandas as pd

df = pd.read_csv(
    "cleaned_passwords.csv"
)

print(df.head())

print()

print(df.shape)

print()

print(df.columns)

print()

print(df.isnull().sum())

print()

print(df['strength'].value_counts())