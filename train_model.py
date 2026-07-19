import pandas as pd
import pickle

from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix
from sklearn.metrics import classification_report

# -----------------------------
# Load Dataset
# -----------------------------
df = pd.read_csv("cleaned_passwords.csv")

print("Original Dataset Shape :", df.shape)

# -----------------------------
# Keep only valid labels (0,1,2)
# -----------------------------
df = df[df["strength"].astype(str).isin(["0", "1", "2"])]

# Convert strength to integer
df["strength"] = df["strength"].astype(int)

print("Cleaned Dataset Shape :", df.shape)

print("\nStrength Distribution")
print(df["strength"].value_counts())

# -----------------------------
# Features and Labels
# -----------------------------
X = df["password"]
y = df["strength"]

# -----------------------------
# Convert Password to Features
# -----------------------------
vectorizer = TfidfVectorizer(analyzer="char")

X = vectorizer.fit_transform(X)

# -----------------------------
# Split Dataset
# -----------------------------
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y
)

# -----------------------------
# Train Model
# -----------------------------
model = LogisticRegression(
    max_iter=1000,
    class_weight="balanced"
)

model.fit(X_train, y_train)

# -----------------------------
# Prediction
# -----------------------------
pred = model.predict(X_test)

print("\nAccuracy")
print(accuracy_score(y_test, pred))

print("\nConfusion Matrix")
print(confusion_matrix(y_test, pred))

print("\nClassification Report")
print(classification_report(y_test, pred))

# -----------------------------
# Save Model
# -----------------------------
pickle.dump(model, open("password_model.pkl", "wb"))
pickle.dump(vectorizer, open("vectorizer.pkl", "wb"))

print("\nModel Saved Successfully")