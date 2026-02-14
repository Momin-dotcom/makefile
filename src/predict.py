import joblib
import pandas as pd
import os

MODEL_PATH = "models/model.pkl"

def main():
    model, X_test, y_test = joblib.load(MODEL_PATH)

    predictions = model.predict(X_test)

    os.makedirs("results", exist_ok=True)
    pd.DataFrame({
        "Actual": y_test,
        "Predicted": predictions
    }).to_csv("results/predictions.csv", index=False)

if __name__ == "__main__":
    main()
