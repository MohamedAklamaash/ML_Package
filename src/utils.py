import os
import sys

import numpy as np 
import pandas as pd
# import dill
import pickle
from sklearn.metrics import r2_score,mean_absolute_error,mean_squared_error
from sklearn.model_selection import GridSearchCV
from typing import List

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

def modelEvaluation(x_train,y_train,x_test,y_test,models):
    model_list = []
    r2_list =[]
    report = {}
    for i in range(len(list(models))):
        model = list(models.values())[i]
        model.fit(x_train, y_train) 

        y_train_pred = model.predict(x_train)
        y_test_pred = model.predict(x_test)
        
        model_train_mae , model_train_rmse, model_train_r2 = evaluateModel(y_train, y_train_pred)

        model_test_mae , model_test_rmse, model_test_r2 = evaluateModel(y_test, y_test_pred)

        report[list(models.keys())[i]] = model_test_r2
        
        print(list(models.keys())[i])
        model_list.append(list(models.keys())[i])
        
        print('Model performance for Training set')
        print("- Root Mean Squared Error: {:.4f}".format(model_train_rmse))
        print("- Mean Absolute Error: {:.4f}".format(model_train_mae))
        print("- R2 Score: {:.4f}".format(model_train_r2))

        print('----------------------------------')
        
        print('Model performance for Test set')
        print("- Root Mean Squared Error: {:.4f}".format(model_test_rmse))
        print("- Mean Absolute Error: {:.4f}".format(model_test_mae))
        print("- R2 Score: {:.4f}".format(model_test_r2))
        r2_list.append(model_test_r2)
        
        print('='*35)
        print('\n')
    
    return report