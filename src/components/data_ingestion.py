import os
import sys

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from dataclasses import dataclass

from src.exception import CustomException
from src.logger import logging
from src.components.data_transformation import DataTransformation, DataTransformationConfig


@dataclass
class DataIngestionConfig:
    train_data_path = os.path.join('artifacts', 'train.csv')
    test_data_path = os.path.join('artifacts', 'test.csv')
    data_path = os.path.join('artifacts', 'data.csv')


class DataIngestion:
    def __init__(self) -> None:
        self.ingestion_config = DataIngestionConfig()

    
    def read_data(self):
        logging.info('Ingesting Data')
        try:
            df = pd.read_csv('src/notebook/data/train.csv')
            logging.info('Read data')
            os.makedirs(os.path.dirname(self.ingestion_config.data_path), exist_ok=True)
            df.dropna(inplace=True)
            df.to_csv(self.ingestion_config.data_path, index=False, header=True)            

            logging.info('Splitting data in Train and Test')
            train_set, test_set = train_test_split(df, test_size=0.1)

            train_set.to_csv(self.ingestion_config.train_data_path, index=False, header=True)
            test_set.to_csv(self.ingestion_config.test_data_path, index=False, header=True)

            logging.info('Ingestion Completed')

            return (
                self.ingestion_config.train_data_path,
                self.ingestion_config.test_data_path
            )
        except Exception as e:
            raise CustomException(e, sys)

# This main function to just make sure the code writing till now is working  
'''
if __name__ == '__main__':
    obj = DataIngestion()
    train_data_path, test_data_path = obj.read_data()
    print(train_data_path, test_data_path)
    data_transformation_obj = DataTransformation()
    train_data, test_data, preprocess_path = data_transformation_obj.preprocess(train_data_path, test_data_path)
'''