import joblib
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score

MODEL_PATH = "models/model.pkl"

def main():
    model, X_test, y_test = joblib.load(MODEL_PATH)
    predictions = model.predict(X_test)

    with open("results/metrics.txt", "w") as f:
        f.write(f"Accuracy: {accuracy_score(y_test, predictions)}\n")
        f.write(f"Precision: {precision_score(y_test, predictions)}\n")
        f.write(f"Recall: {recall_score(y_test, predictions)}\n")
        f.write(f"F1 Score: {f1_score(y_test, predictions)}\n")

if __name__ == "__main__":
    main()
