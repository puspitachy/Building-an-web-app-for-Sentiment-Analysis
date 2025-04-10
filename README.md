**A Web based Application for Analysing Sentiment in Online Consumer Reviews**

dataset-  Amazon review and IMDV review dataset with total 75,000 reviews. 
Please Download IMDB dataset from kaggle                [ File is too big to upload here]

Process:

Run SentimentAnalysisonCR_(2) (3).ipnyb for model deployment.

Logistic regression,SVM Model and Gaussian naive bayes Model used for finding out which model perform best.

Model whuch oerform best has been hypertuned for more good performence.



Testing code performance:

Input Data testing

Ouput data testing

Saving model, vectorizer, stop words

file name as follows ;
               sample_data_The_stopwords (1).pkl
              
               sample_data_datareview_model.pkl
               
               sample_data_analysis_vectorizer (1).pkl
               
               sentimentanalysis.pkl


                                                            Building the web application
    For deployment purposes http://127.0.0.1:5002                                                      
  
  run main.py [used pycharm for creating the web app]
  
  for web app created file using HTML; form.html, ReviewForm.html, and home.html
  
  Reviewform.html is the main page which will display after opening the web application. Other pages are result page.
  
  The first step in using the app is to create a little tools that categorizes text. For that some

   helper function has been created. The model and vectorizer loaded previously will be used for categorizing text.

• A class name ReviewForm has been created for validating input text size length minimum of 25 characters.


• A function name Classify has been created for calculating probability score for single review.

• A helper function name result has been created to analyse single review from user.

• A helper function name analyze has been created to analyse .CSV format file sentiment and plot has been used for visualizing large amount dataset in a pie chart.

• All the HTML files form.html, ReviewForm.html, and home.html has been created and has been associated with the ”/” home route.
• A result route has been deployed which will classify the sentiment and will show the result
of sentiment from the text and file which has been inputted by user.

User can either put sentiment by a sentence or also can upload .csv file for getting total percentage of sentiment.
![Image description](https://github.com/puspitachy/image/blob/main/Screenshot%202025-04-10%20153022.png)

![Image description]([https://github.com/puspitachy/image/blob/main/Screenshot%202025-04-10%20153041.png)
  
