import os
import sys

from src.logger import logging
from src.exception import CustomException
from src.utils import save_object, evaluate_model

import numpy as np
from dataclasses import dataclass

from sklearn.linear_model import LogisticRegression
from sklearn.naive_bayes import MultinomialNB


@dataclass
class ModelTrainerConfig:
    logistic_regression_path = os.path.join('artifacts', 'logistic.pkl')
    naive_bayes_path = os.path.join('artifacts', 'multinomialNB.pkl')


class ModelTrainer:
    def __init__(self) -> None:
        self.config = ModelTrainerConfig()

    
    def train_model(self, train_data, test_data):
        try: 
            X_train, y_train = train_data[:, :-1], train_data[:, -1]

            logging.info("Training Logistic Regression")
            clf1 = LogisticRegression(max_iter=100)
            logging.info("Training Multinomial Naive Bayes")
            clf2 = MultinomialNB()

            clf1.fit(X_train, y_train)
            clf2.fit(X_train, y_train)

            models = [clf1, clf2]

            evaluation = evaluate_model(models, test_data)
            logging.info(f'Accuracy Score on Test Data: {str(evaluation)}')

            return clf1, clf2

        except Exception as e:
            raise CustomException(e, sys)
        

    def initiate_training(self, train_data, test_data):
        try:
            logging.info('Initiating Model Training')
            clf1, clf2 = self.train_model(train_data, test_data)
            logging.info("Trained Models successfully")

            logging.info('Saving Models into Pickle File')
            save_object(
                self.config.logistic_regression_path,
                clf1
            )

            save_object(
                self.config.naive_bayes_path,
                clf2
            )

            logging.info('Trained, Evaluated and Saved Models successfully')
        except Exception as e:
            raise CustomException(e, sys)


