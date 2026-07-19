import pandas as pd

from sklearn.feature_extraction.text import TfidfVectorizer

df = pd.read_csv(

"cleaned_passwords.csv"

)

X = df['password']

y = df['strength']

vectorizer = TfidfVectorizer(

analyzer='char'

)

X = vectorizer.fit_transform(X)

print(

X.shape

)