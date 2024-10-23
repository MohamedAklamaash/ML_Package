import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.metrics import mean_squared_error, r2_score, mean_absolute_error
from sklearn.neighbors import KNeighborsRegressor
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import AdaBoostRegressor, RandomForestRegressor
from sklearn.linear_model import LinearRegression, Ridge, Lasso
from catboost import CatBoostRegressor
from xgboost import XGBRegressor
import os
from dataclasses import dataclass
import sys

from src.utils import modelEvaluation
from src.utils import save_object
from src.exception import CustomException
from src.logger import logging

@dataclass
class ModelTrainerConfig:
    trained_model_file_path: str = os.path.join("artifacts", "model.pkl")

class ModelTrainer:
    def __init__(self):
        self.model_trainer_config = ModelTrainerConfig()

    def initiate_model_trainer(self, train_arr, test_arr):
        try:
            logging.info("Splitting train and test data")
            x_train, y_train, x_test, y_test = (
                train_arr[:, :-1],
                train_arr[:, -1],
                test_arr[:, :-1],
                test_arr[:, -1]
            )

            # Define the models to train
            models = {
                "Linear Regression": LinearRegression(),
                "Lasso": Lasso(),
                "Ridge": Ridge(),
                "K-Nearest-Neighbour": KNeighborsRegressor(),
                "Decision Tree": DecisionTreeRegressor(),
                "CatBoost": CatBoostRegressor(verbose=0),
                "Adaboost": AdaBoostRegressor(),
                "XGBoost": XGBRegressor(),
                "Random Forest": RandomForestRegressor()
            }

            # Evaluate models
            logging.info("Evaluating models")
            model_report: dict = modelEvaluation(x_train, y_train, x_test, y_test, models)
            # Find the best model and its score
            bestmodelscore = max(model_report.values())
            bestmodelname = list(model_report.keys())[list(model_report.values()).index(bestmodelscore)]
            best_model = models[bestmodelname]

            if bestmodelscore < 0.6:
                raise CustomException("No model performed well enough", sys)

            logging.info(f"Best model: {bestmodelname} with score: {bestmodelscore}")

            # Save the best model
            file_path = self.model_trainer_config.trained_model_file_path
            save_object(file_path=file_path, obj=best_model)

            # Make predictions and return r2 score
            pred = best_model.predict(x_test)
            r2_square = r2_score(y_test, pred)

            return r2_square

        except Exception as e:
            raise CustomException(e, sys)
