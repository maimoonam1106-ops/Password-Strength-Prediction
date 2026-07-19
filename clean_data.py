import pandas as pd

# Read excel file
df = pd.read_excel("dataset/DataPasswordSecure.csv.xlsx")

# Keep only required columns
df = df[['password', 'strength']]

# Remove missing values
df = df.dropna()

# Remove duplicates
df = df.drop_duplicates()

print("Shape after cleaning:")
print(df.shape)

# Save cleaned data
df.to_csv("cleaned_passwords.csv", index=False)

print("Dataset cleaned successfully!")
print("Shape after cleaning:", df.shape)
print("Dataset cleaned successfully!")