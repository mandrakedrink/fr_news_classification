# French News Classification

This project focuses on automatic classification of French sport news articles using Natural Language Processing methods.

## Models
- TF-IDF + Logistic Regression
- CamemBERT for sequence classification

## Dataset
The dataset contains French news articles collected from Eurosport.

## Metrics
The models are evaluated using accuracy, precision, recall and F1-score.

## How to run
1. Install dependencies:
   pip install -r requirements.txt

2. Run notebook:
   french-news-classiifier.ipynb
   camembert.ipynb

3. Run API:
   uvicorn main:app --reload
