# MLOps Titanic Pipeline

This project is an automated machine learning pipeline for predicting survival on the Titanic dataset using **GNU Make**. All steps are automated through a Makefile for reproducibility.

## Project Structure
makefile/
├── data/
│ ├── raw/ # Raw Titanic dataset (downloaded automatically)
│ └── processed/ # Preprocessed dataset
├── src/
│ ├── download_data.py
│ ├── preprocess.py
│ ├── features.py
│ ├── train.py
│ ├── predict.py
│ └── evaluate.py
├── models/
│ └── model.pkl
├── results/
│ ├── predictions.csv
│ └── metrics.txt
├── requirements.txt
├── Makefile
└── README.md
## Makefile Targets

- `make setup` → Install Python dependencies  
- `make download-data` → Download Titanic dataset  
- `make preprocess` → Clean and prepare data  
- `make features` → Feature engineering  
- `make train` → Train the ML model  
- `make predict` → Generate predictions  
- `make evaluate` → Compute evaluation metrics  
- `make all` → Run the full pipeline  
- `make clean` → Remove all generated files and folders  

## How to Run

1. Install dependencies:

make setup

2. Run the pipline:

make all

3. Clean the artifacts:

make clean

##Available Commands

make setup – Install dependencies

make download-data – Download dataset

make preprocess – Clean data

make features – Feature engineering

make train – Train model

make predict – Generate predictions

make evaluate – Evaluate model

make clean – Remove generated files
