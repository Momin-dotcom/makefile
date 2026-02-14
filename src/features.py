import pandas as pd

PATH = "data/processed/processed.csv"

def main():
    df = pd.read_csv(PATH)
    df["FamilySize"] = df["SibSp"] + df["Parch"] + 1
    df.to_csv(PATH, index=False)

if __name__ == "__main__":
    main()
