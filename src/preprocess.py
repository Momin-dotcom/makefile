import pandas as pd
import os

RAW_PATH = "data/raw/titanic.csv"
PROCESSED_PATH = "data/processed/processed.csv"

def main():
    df = pd.read_csv(RAW_PATH)

    df["Age"].fillna(df["Age"].median(), inplace=True)
    df["Embarked"].fillna(df["Embarked"].mode()[0], inplace=True)
    df["Fare"].fillna(df["Fare"].median(), inplace=True)

    df["Sex"] = df["Sex"].map({"male": 0, "female": 1})
    df = pd.get_dummies(df, columns=["Embarked"], drop_first=True)

    df.drop(["Name", "Ticket", "Cabin"], axis=1, inplace=True)

    os.makedirs("data/processed", exist_ok=True)
    df.to_csv(PROCESSED_PATH, index=False)

if __name__ == "__main__":
    main()
