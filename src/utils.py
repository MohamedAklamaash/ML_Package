import os
import sys

import numpy as np 
import pandas as pd
# import dill
import pickle
from sklearn.metrics import r2_score,mean_absolute_error,mean_squared_error
from sklearn.model_selection import GridSearchCV
from typing import List
from sklearn.model_selection import RandomizedSearchCV
from src.params import param_grid
from src.exception import CustomException

def save_object(file_path, obj):
    try:
        dir_path = os.path.dirname(file_path)

        os.makedirs(dir_path, exist_ok=True)

        with open(file_path, "wb") as file_obj:
            pickle.dump(obj, file_obj)

    except Exception as e:
        raise CustomException(e, sys)


def evaluateModel(true:List[float],predicted:List[float])->List[float]:
    mae = mean_absolute_error(true,predicted)
    mse = mean_squared_error(true,predicted)
    rmse = np.sqrt(mse)
    r2_sq = r2_score(true,predicted)
    return mae,rmse,r2_sq

def modelEvaluation(x_train, y_train, x_test, y_test, models):
    model_list = []
    r2_list = []
    report = {}

    for model_name, model in models.items():
        # Get the corresponding parameters for this model from param_grid
        para = param_grid.get(model_name, {})  # Use .get() to safely fetch parameters
        
        if para:  # If param_grid contains parameters for this model
            gs = GridSearchCV(model, para, cv=3, n_jobs=-1)
            gs.fit(x_train, y_train)
            model = gs.best_estimator_  # Use the best estimator from GridSearchCV
        else:
            # Fit the model without hyperparameter tuning
            model.fit(x_train, y_train)

        # After fitting, use the model to predict
        y_train_pred = model.predict(x_train)
        y_test_pred = model.predict(x_test)

        # Evaluate model performance
        model_train_mae, model_train_rmse, model_train_r2 = evaluateModel(y_train, y_train_pred)
        model_test_mae, model_test_rmse, model_test_r2 = evaluateModel(y_test, y_test_pred)

        report[model_name] = model_test_r2

        # Output the model performance metrics
        print(model_name)
        print('Model performance for Training set')
        print(f"- Root Mean Squared Error: {model_train_rmse:.4f}")
        print(f"- Mean Absolute Error: {model_train_mae:.4f}")
        print(f"- R2 Score: {model_train_r2:.4f}")
        print('----------------------------------')
        print('Model performance for Test set')
        print(f"- Root Mean Squared Error: {model_test_rmse:.4f}")
        print(f"- Mean Absolute Error: {model_test_mae:.4f}")
        print(f"- R2 Score: {model_test_r2:.4f}")
        print('=' * 35)
        print('\n')

    return report
