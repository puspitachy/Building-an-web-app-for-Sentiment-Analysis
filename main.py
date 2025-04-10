#!/usr/bin/env python
# coding: utf-8

from sklearn import *
from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer
from sklearn.feature_selection import SequentialFeatureSelector
from sklearn.feature_selection import SelectKBest, chi2
from flask import Flask, render_template, request
from wtforms import Form, TextAreaField, validators
import pickle
import sqlite3
import os
from sklearn.pipeline import Pipeline
from pyspark.ml import Pipeline, PipelineModel

from jinja2 import Template

import numpy as np
import joblib
import pandas as pd
from sklearn.metrics import accuracy_score
analysis_model = joblib.load(r"C:\Users\puspi\PycharmProjects\pythonProject10 -new\sample_data_datareview_model.pkl")
analysis_stopwords = joblib.load(r"C:\Users\puspi\PycharmProjects\pythonProject10 -new\sample_data_The_stopwords (1).pkl")
analysis_vectorization = joblib.load(r"C:\Users\puspi\PycharmProjects\pythonProject10 -new\sample_data_analysis_vectorizer (1).pkl")

app = Flask(__name__)

#single review analysing
#classifying sentiment and calculating probablity
def classify(document):
    label = {0: 'negative', 1: 'positive'}
    X = analysis_vectorization.transform([document])
    y = analysis_model.predict(X)[0]
    proba = np.max(analysis_model.predict_proba(X))
    return y, proba

#creating inputbox with character number
class ReviewForm(Form):
    moviereview = TextAreaField('', [validators.DataRequired(), validators.length(min=15)])




@app.route('/')
def index():
    form = ReviewForm(request.form)
    return render_template('reviewform.html', form=form)

#reviewform page to home page
@app.route('/results', methods=['POST', 'GET'])
def results():
    form = ReviewForm(request.form)
    if request.method == 'POST' and form.validate():

        review = request.form['moviereview']
        y, proba = classify(review)
        return render_template('home.html', content=review, prediction=y, probability=round(proba * 100, 2))
        return render_template('reviewform.html', form=form)









# Defining reviewform page route
@app.route('/')
def home():
    return render_template('reviewform.html')

# Defining route for analyzing sentiment from  CSV file
@app.route('/analyze', methods=['POST'])
def analyze():
    # choose the file
    file = request.files['file']
    if not file:
        return render_template('error.html', message='No file uploaded')

    # Loaded CSV file into pd dataframe
    try:
        data = pd.read_csv(file)
    except Exception as e:
        #shows error if no file found
        return render_template('error.html', message=str(e))

    # Extract features from data
    # csv file need to have a column 'Review'
    review= data['Review']

    # Vectorizing csv textual data
    reviewr = analysis_vectorization.transform(review)

    # Predicting  using saved LRmodel
    sentiment = analysis_model.predict(reviewr)




    # Calculate the accuracy of the predictions by the model
    accuracy = accuracy_score(data['Review'], sentiment)
    print(f'Accuracy: {accuracy}')
    # Create a histogram of the predicted sentiments
    his_data_analysis = pd.DataFrame({'sentiment': sentiment}).replace({0 : 'Negative', 1: 'Positive'})
    his_data_analysis = his_data_analysis.value_counts().reset_index(name='count')
    his_data_analysis['percentage'] = his_data_analysis['count'] / len(sentiment) * 100

    # Passing dataframe to form template and rendere it
    return render_template('form.html', results=list(zip(data['Review'], sentiment)),
                           his_data_analysis=his_data_analysis.to_dict(orient='records'))

if __name__ == "__main__":
    app.run(debug=True,  port=5002, threaded=True)






