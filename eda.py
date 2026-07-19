import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("cleaned_passwords.csv")

print(df.head())

print(df['strength'].value_counts())

df['strength'].value_counts().plot(kind='bar')

plt.title("Password Strength Distribution")

plt.xlabel("Strength")

plt.ylabel("Count")

plt.show()