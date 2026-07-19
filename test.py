import pickle

model = pickle.load(open("password_model.pkl","rb"))
vectorizer = pickle.load(open("vectorizer.pkl","rb"))

while True:
    password = input("Password: ")

    X = vectorizer.transform([password])

    pred = model.predict(X)[0]

    print("Prediction =", pred)