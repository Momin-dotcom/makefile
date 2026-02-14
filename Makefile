.PHONY: setup download-data preprocess features train predict evaluate all clean

setup:
	pip install -r requirements.txt

download-data:
	python src/download_data.py

preprocess: download-data
	python src/preprocess.py

features: preprocess
	python src/features.py

train: features
	python src/train.py

predict: train
	python src/predict.py

evaluate: predict
	python src/evaluate.py

all: setup download-data preprocess features train predict evaluate

clean:
	if exist data\raw rmdir /S /Q data\raw
	if exist data\processed rmdir /S /Q data\processed
	if exist models rmdir /S /Q models
	if exist results rmdir /S /Q results

