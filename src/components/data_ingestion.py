# used for reading the data 
# when you only have variables then use data class otherwise go with __init__

import os 
import sys
from src.exception import CustomException
from src.logger import logging
import pandas as pd
from sklearn.model_selection import train_test_split
from dataclasses import dataclass

from src.components.data_transformation import DataTransformation
from src.components.data_transformation import DataTransformationConfig

# some kind of input
@dataclass
class DataIngestionConfig:
    # tells where to save test train and raw data
    train_data_path: str = os.path.join('artifacts', "train.csv")
    test_data_path: str = os.path.join('artifacts', "test.csv")
    raw_data_path: str = os.path.join('artifacts', "data.csv")


class DataInjestion:
    def __init__(self):
        self.injestion_config=DataIngestionConfig()

    def inititate_data_injestion(self):
        logging.info("Entered the data ingestion method or component")

        try:
            df = pd.read_csv('notebook/data/stud.csv')
            logging.info("Read the dataset as data frame")

            # combine the directory name and if it is already present then new dir will not be created
            os.makedirs(os.path.dirname(self.injestion_config.train_data_path), exist_ok=True)

            df.to_csv(self.injestion_config.raw_data_path, index=False, header=True)

            logging.info("Train Test split inititated")
            train_set, test_set = train_test_split(df, test_size=0.2, random_state=42)

            train_set.to_csv(self.injestion_config.train_data_path, index=False, header=True)
            test_set.to_csv(self.injestion_config.test_data_path, index=False, header=True)

            logging.info("Ingestion of the data is completed")

            return(
                
                self.injestion_config.train_data_path,
                self.injestion_config.test_data_path

            )

        except Exception as e:
            raise CustomException(e, sys)


if __name__ =="__main__":
    obj = DataInjestion()
    train_data, test_data = obj.inititate_data_injestion()

    data_transformation=DataTransformation()
    data_transformation.initiate_data_transformation(train_data, test_data)