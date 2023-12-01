import sys
from dataclasses import dataclass

from src.exception import CustomException
from src.logger import logging
from src.utils import save_object
import os

import numpy as np
import pandas as pd

import nltk
from nltk.corpus import stopwords
import re
from nltk.stem import WordNetLemmatizer

from sklearn.feature_extraction.text import CountVectorizer

nltk.download('stopwords')
nltk.download('punkt')
nltk.download('wordnet')
nltk.download('omw-1.4')


class Text_Preprocessing:
    def clean_tweets(self, tweets):
        cleaned_tweets = []
        stopwords_eng = stopwords.words('english')
        for tweet in tweets:
            #removing hyperlinks
            tweet = re.sub(r"https?://[^\s\n\r]+", ' ', tweet)
            #removing punctuations and digits, only taking words
            tweet = re.sub('[^a-zA-z]', ' ', tweet)
            tweet = re.sub(r'[\W_]+', ' ', tweet)
            tweet = tweet.lower()
            words = nltk.word_tokenize(tweet)
            words = [word for word in words if word not in stopwords_eng]
            cleaned_tweets.append(' '.join(words))
        return cleaned_tweets


    def lemmatize_text(self, tweets):
        lemmatizer = WordNetLemmatizer()
        lem_tweets = []
        for tweet in tweets:
            lem_words = [lemmatizer.lemmatize(word) for word in nltk.word_tokenize(tweet)]
            lem_tweet = ' '.join(lem_words)
            lem_tweets.append(lem_tweet)
        return lem_tweets


    def count_vectorize(self, tweets):
        count_vec = CountVectorizer(max_features=10000)
        count_vec.fit(tweets)
        vec_tweets = count_vec.transform(tweets).toarray()
        return (vec_tweets, count_vec)


    def transform_target_variable(self, target_var):
        target_map = {
            'negative' : 0,
            'positive' : 1,
            'neutral' : 2
        }
        target = target_var.map(target_map).astype(np.int64)
        return target


@dataclass
class DataTransformationConfig:
    textpreprocessing_file_path = os.path.join('artifacts', 'preprocessor.pkl')
    count_vectorizer_path = os.path.join('artifacts', 'count_vec.pkl')


class DataTransformation:
    def __init__(self) -> None:
        self.config = DataTransformationConfig()

    def get_textpreprocessing_obj(self):
        try:
            preprocessor = Text_Preprocessing()
            return preprocessor
        except Exception as e:
            raise CustomException(e, sys)
        
    def preprocess(self, train_path, test_path):

        try:
            train_df = pd.read_csv(train_path)
            test_df = pd.read_csv(train_path)

            logging.info('Imported train and test sets for Text Preprocessing')

            logging.info('Obtaining Preprocessing Object')

            preprocessing_obj = self.get_textpreprocessing_obj()

            target_column = 'sentiment'
            input_column = 'text'

            text_train_df = train_df[input_column]

            
            train_target = np.array(train_df[target_column]).reshape(-1, 1)
            test_target = np.array(test_df[target_column]).reshape(-1, 1)
            logging.info('Mapped Target Variable')


            logging.info('Cleaning Text')
            train_text, test_text = train_df[input_column], test_df[input_column]
            train_clean_tweets, test_clean_tweets = preprocessing_obj.clean_tweets(train_text), preprocessing_obj.clean_tweets(test_text)
            train_lem_tweets = preprocessing_obj.lemmatize_text(train_clean_tweets)
            test_lem_tweets = preprocessing_obj.lemmatize_text(test_clean_tweets)

            logging.info('Implementing Count Vectorizer')
            train_count_vec_data, count_vec = preprocessing_obj.count_vectorize(train_lem_tweets) 
            test_count_vec_data = count_vec.transform(test_lem_tweets).toarray() 

            logging.info('Completed Text Preprocessing') 

            logging.info('Saving Objects')
            save_object(self.config.count_vectorizer_path, count_vec)
            save_object(self.config.textpreprocessing_file_path, preprocessing_obj)

            logging.info('Stacking Data')
            train_arr = np.hstack((train_count_vec_data, train_target))
            test_arr = np.hstack((test_count_vec_data, test_target))

            return (
                train_arr,
                test_arr,
                self.config.textpreprocessing_file_path
            )

            
        except Exception as e:
            raise CustomException(e, sys)