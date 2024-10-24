import sys
import pandas as pd # type:ignore

from src.exception import CustomException
from src.utils import save_object,load_object
from src.logger import logging

class PredictPipeline():
    def __init__(self) -> None:
        pass
    
    def predict(self,features):
        try:
            model_path = "artifacts/model.pkl"
            preprocessor_path = "artifacts/preprocessor.pkl"
            model = load_object(file_path = model_path)
            preprocessor = load_object(file_path = preprocessor_path)
            data_scaled = preprocessor.transform(features)
            pred = model.predict(data_scaled)
            return pred
        except Exception as e:
            logging.info("error in prediction file")
            raise CustomException(e,sys)

class CustomDataClass():
    def __init__(self,
                 gender:str,
                 race_ethinicity:str,
                 parental_level_of_education,
                 lunch:str,
                 test_preparation_course:int,
                 reading_score:int,
                 writing_score:int) -> None:
        self.gender = gender
        self.race_ethinicity = race_ethinicity
        self.parental_level_of_education = parental_level_of_education
        self.lunch = lunch
        self.test_preparation_course = test_preparation_course
        self.reading_score = reading_score
        self.writing_score = writing_score
    
    def get_data_as_frame(self):
        try:
            custom_data_dict = {
                "gender":[self.gender],
                "race_ethinicity":[self.race_ethinicity],
                "parental_level_of_education":[self.parental_level_of_education],
                "lunch":[self.lunch],
                "test_preparation_course":[self.test_preparation_course],
                "reading_score":[self.reading_score],
                "writing_score":[self.writing_score]
            }
            return pd.DataFrame(custom_data_dict)
        except Exception as e:
            logging.info()
            raise CustomException(e,sys)