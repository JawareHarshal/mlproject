import os
import sys
import dill

import numpy as np
import pandas as pd
from sklearn.metrics import r2_score
from sklearn.model_selection import GridSearchCV

from src.exception import CustomException 

def save_object(file_path, obj):
    try:
        dir_path = os.path.dirname(file_path)

        os.makedirs(dir_path, exist_ok = True)

        with open(file_path, "wb") as file_obj:
            dill.dump(obj, file_obj)

    except Exception as e:
        raise CustomException(e, sys)

def evaluate_models(X_train, y_train, X_test, y_test, models, param):

    try:
        report={}

        # to iterate over each model
        for i in range(len(list(models))):

            # fetching individual values(models)
            model = list(models.values())[i]

            # fetching the list of params
            para=param[list(models.keys())[i]]

            # cv = cross validation
            gs = GridSearchCV(model, para, cv=3)
            gs.fit(X_train, y_train)

            model.set_params(**gs.best_params_)

            # fitting the model o X_train and y_train
            model.fit(X_train, y_train)     # Train model

            # making prediction on X_train and X_test
            y_train_pred = model.predict(X_train)
            y_test_pred = model.predict(X_test)

            # compute the r2 score 
            train_model_score = r2_score(y_train, y_train_pred)
            test_model_score = r2_score(y_test, y_test_pred)

            # appending the values 
            report[list(models.keys())[i]] = test_model_score

        return report 

    except Exception as e:
        raise CustomException(e, sys)

    
def load_object(file_path):

    try:
        with open (file_path, "rb") as file_obj:
            return dill.load(file_obj)

    except Exception as e:
        raise CustomException(e, sys)
