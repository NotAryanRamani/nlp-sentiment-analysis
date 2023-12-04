import os
import sys
from src.exception import CustomException
from src.logger import logging
from sklearn.metrics import accuracy_score

import pickle


def save_object(path, obj):
    try:
        dir_path = os.path.dirname(path)

        os.makedirs(dir_path, exist_ok=True)

        with open(path, 'wb') as f:
            pickle.dump(obj, f)
    
    except Exception as e:
        raise CustomException(sys, e)
    

def evaluate_model(models, test_data):
    evals = {}
    X_test, y_test = test_data[:, :-1], test_data[:, -1]
    for model in models:
        model_name = type(model).__name__
        y_pred = model.predict(X_test)
        score = accuracy_score(y_test, y_pred)
        evals[model_name] = score
    return evals
    pass