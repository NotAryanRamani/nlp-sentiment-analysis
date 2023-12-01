import os
import sys
from src.exception import CustomException
from src.logger import logging

import pickle


def save_object(path, obj):
    try:
        dir_path = os.path.dirname(path)

        os.makedirs(dir_path, exist_ok=True)

        with open(path, 'wb') as f:
            pickle.dump(obj, f)
    
    except Exception as e:
        raise CustomException(sys, e)