import pandas as pd
import joblib
import os
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier

DATA_PATH = "data/processed/processed.csv"
MODEL_PATH = "models/model.pkl"

def main():
    df = pd.read_csv(DATA_PATH)

    X = df.drop("Survived", axis=1)
    y = df["Survived"]

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    model = RandomForestClassifier(random_state=42)
    model.fit(X_train, y_train)

    os.makedirs("models", exist_ok=True)
    joblib.dump((model, X_test, y_test), MODEL_PATH)

if __name__ == "__main__":
    main()
