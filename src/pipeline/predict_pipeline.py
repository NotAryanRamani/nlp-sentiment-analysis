import os
import sys
import pickle

import numpy as np

from dataclasses import dataclass

from src.exception import CustomException
from src.logger import logging



@dataclass
class PredictPipelineConfig():
    vectorizer_path = os.path.join('artifacts', 'count_vec.pkl')
    logistic_reg_path = os.path.join('artifacts', 'logistic.pkl')
    multinomialNB_path = os.path.join('artifacts', 'multinomialNB.pkl')


class PredictPipeline():
    def __init__(self) -> None:
        # print('loading_models')
        self.config = PredictPipelineConfig()
        self.vectorizer = pickle.load(open(self.config.vectorizer_path, 'rb'))
        self.log_clf = pickle.load(open(self.config.logistic_reg_path, 'rb'))
        self.mulNB_clf = pickle.load(open(self.config.multinomialNB_path, 'rb'))
        # print('models_loaded')

    def get_vertorized_array(self, text:str):
        text = text.lower()
        text = [text]
        arr = np.array(self.vectorizer.transform(text).toarray())
        return arr
    
    def get_predictions(self, text):
        try:
            logging.info('Vectorizing Text')
            vectorized_text = self.get_vertorized_array(text)
            predictions = {}
            logging.info('Predicting')
            log_pred = self.log_clf.predict(vectorized_text)
            mulNB_pred = self.mulNB_clf.predict(vectorized_text)
            predictions['LogisticRegression'] = log_pred
            predictions['MultinomialNaiveBayes'] = mulNB_pred
            return predictions
        except Exception as e:
            raise CustomException(e, sys)
    
