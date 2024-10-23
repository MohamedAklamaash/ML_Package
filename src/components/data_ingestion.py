import os
import sys
from src.exception import CustomException
from src.logger import logging
import pandas as pd
from sklearn.model_selection import train_test_split
from dataclasses import dataclass
from src.components.data_transformation import DataTransformation,DataTransformationConfig

@dataclass
class DataIngestionConfig:
    train_data_path:str = os.path.join("artifacts","train.csv")
    test_data_path:str = os.path.join("artifacts","test.csv")
    raw_data_path:str = os.path.join("artifacts","raw.csv")

class DataIngestion:
    def __init__(self):
        self.ingestion_config = DataIngestionConfig()
    
    def initiate_data_ingestion(self):
        logging.info("Data ingestion pipeline is started")
        try:
            df1 = pd.read_csv("notebook/data/stud.csv")
            logging.info("Read the dataset as a dataframe")

            os.makedirs(os.path.dirname(self.ingestion_config.train_data_path),exist_ok=True) # makes sure artifacts folder is there

            df1.to_csv(self.ingestion_config.raw_data_path,index=False,header=True)
            logging.info("train test split initiated")
            train_set: pd.DataFrame
            test_set: pd.DataFrame
            train_set,test_set = train_test_split(df1,test_size=0.2,random_state=42)

            train_set.to_csv(self.ingestion_config.train_data_path,index=False,header=True)
            test_set.to_csv(self.ingestion_config.test_data_path,index=False,header=True)

            logging.info("ingestion of data is updated")

            return (
                self.ingestion_config.train_data_path,
                self.ingestion_config.test_data_path
            )

        except Exception as e:
            logging.error("Error in executing the ingestion pipeline")
            raise CustomException(e,sys)
        
if __name__ == "__main__":
    obj = DataIngestion()
    train_data_path,test_data_path = obj.initiate_data_ingestion()
    data_tranformation = DataTransformation()
    data_tranformation.initiate_data_transformation(train_data_path,test_data_path)
    