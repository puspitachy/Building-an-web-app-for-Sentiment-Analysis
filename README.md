**A Web based Application for Analysing Sentiment in Online Consumer Reviews**

dataset-  Amazon review and IMDV review dataset with total 75,000 reviews. 
Please Download IMDB dataset from kaggle                [ File is too big to upload here]

Process:

Run SentimentAnalysisonCR_(2) (3).ipnyb for model deployment.

Logistic regression,SVM Model and Gaussian naive bayes Model used for finding out which model perform best.

Model which perform best has been hypertuned for more good performence.



Testing code performance:

Input Data testing

Ouput data testing

Saving model, vectorizer, stop words

#file name as follows ;
sample_data_The_stopwords (1).pkl
              
sample_data_datareview_model.pkl
               
sample_data_analysis_vectorizer (1).pkl
               
sentimentanalysis.pkl


                                                           # Building the web application
                                                   For deployment purposes http://127.0.0.1:5002                                                      
  
  run main.py [used pycharm for creating the web app]
  
  for web app created file using HTML; form.html, ReviewForm.html, and home.html
  
  Reviewform.html is the main page which will display after opening the web application. Other pages are result page.
  
  The first step in using the app is to create a little tools that categorizes text. For that some

   helper function has been created. The model and vectorizer loaded previously will be used for categorizing text.

•  input text size length minimum of 25 characters.


User can either put sentiment by a sentence or also can upload .csv file for getting total percentage of sentiment.
#For testing the app   .CSV file you can use book1.csv and reviewbook.csv . This file  must be in .CSV format. The web application is case sensitive. Therefore, in the csv file the review column name (which contains feedback of consumers) needs to be replaced by ‘Review’.

Home page
![Image description](https://github.com/puspitachy/image/blob/main/Screenshot%202025-04-10%20153022.png)

  



![Image description](https://github.com/puspitachy/image/blob/main/Screenshot%202025-04-10%20153041.png)

                          prediction analysis
![Image description](https://github.com/puspitachy/image/blob/main/Screenshot%202025-04-10%20165324.png)


![Image description](https://github.com/puspitachy/image/blob/main/Screenshot%202023-04-03%20171526.png)


short review 
![Image description](https://github.com/puspitachy/image/blob/main/Screenshot%202023-04-03%20172203.png)

Long review sentence as a peragraph 
![Image description](https://github.com/puspitachy/image/blob/main/Screenshot%202023-04-03%20172049.png)

checking sentiment from a file of reviews.


![Image description](https://github.com/puspitachy/image/blob/main/Screenshot%202023-04-03%20171646.png)

![Image description](https://github.com/puspitachy/image/blob/main/Screenshot%202023-04-03%20171719.png)

percentage of positive and negative review in a .CSV file.

![Image description](https://github.com/puspitachy/image/blob/main/Screenshot%202025-04-10%20165343.png)
