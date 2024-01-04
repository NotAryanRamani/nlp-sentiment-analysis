 # <div align='center'> Sentiment Analysis NLP Project </div> 

---

## About the project
This is a End to End Machine Learning project on a Tweets Dataset, the task is to determine the sentiment of a tweet as positive, neutral or negative.

The project will follow the following steps:
- [x] Setting Up Github Repository and Project Structure
- [x] Custom Exception Handling and Logging
- [x] Exploratory Data Analysis
- [x] Data Ingestion and Data Transformation Implementation
- [x] Model Training and Evaluation
- [x] Flask Web App and API Development
- [x] Deployment on Cloud Server with CI/CD Pipeline

---

## About the Data Set
The dataset is named Tweet Sentiment Extraction which is available on Kaggle and You can get the data set [here](https://www.kaggle.com/competitions/tweet-sentiment-extraction).

It contains 4 features `textId`, `text`, `selected_text` and `sentiment`

The data has `27481` entries/row/samples.

---

# Models Trained 
1. **Logistic Regression**  
    To import the model use the following code:   
    `from sklearn.linear_model import LogisticRegression`

    Parameters used:  
    `LogisticRegression(  
        max_iter=100  
    )`

    Accuracy Achieved:  
    `y_pred = model.predict(X_test)  
    score = accuracy_score(y_true, y_pred)`  
    *Output*:  
    {'LogisticRegression': 0.8535096231602782}

2. **Multinomial Naive Bayes**  
    To import the model use the following code:   
    `from sklearn.naive_bayes import MultinomialNB`

    *No paramerters used*

    Accuracy Achieved:  
    `y_pred = model.predict(X_test)  
    score = accuracy_score(y_true, y_pred)`  
    *Output*:  
    {'MultinomialNB': 0.7907569141193596}

---

## Chronological Updates

- **September 2, 2023**: Created github repository, README.md file, environment, setup.py file  and Project Structure

- **September 3, 2023**: Created Custom Exception class and Logging Configurations and Basic EDA

- **September 14, 2023** : Created Data Ingestion Module

- **December 1, 2023** : Created Data Transformation Module

- **December 2, 2023** : Created and evaluted models in jupyter notebook

- **December 4, 2023** : Implemented Modular coding to develop LogisticRegression model and Multinomial Naive Bayes

- **December 5, 2023** : Developed Prediction Pipeline and Flask App

- **January 4, 2024** : Developed API and hosted on Heroku using Docker and Github actions

---

### Contributors
The project is contributed by myself, Aryan Ramani. You can contact me at:
1. [LinkedIn](https://www.linkedin.com/in/aryan-ramani-a516b5212/)
2. [email](mailto:aryanramani67@gmail.com)