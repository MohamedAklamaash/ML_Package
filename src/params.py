param_grid = {
        "Linear Regression": {},  # No hyperparameters to tune
        "Ridge": {
            'alpha': [0.01, 0.1, 1, 10, 100],
            'solver': ['auto', 'svd', 'cholesky', 'lsqr', 'sparse_cg', 'sag', 'saga'],
            'max_iter': [100, 500, 1000],
        },
        "K-Nearest-Neighbour": {
            'n_neighbors': [3, 5, 7, 9, 11],
            'weights': ['uniform', 'distance'],
            'algorithm': ['auto', 'ball_tree', 'kd_tree', 'brute'],
            'p': [1, 2]
        },
        "Decision Tree": {
            'criterion': ['mse', 'friedman_mse', 'mae'],
            'splitter': ['best', 'random'],
            'max_depth': [None, 10, 20, 30],
            'min_samples_split': [2, 5, 10],
            'min_samples_leaf': [1, 2, 4],
            'max_features': ['auto', 'sqrt', 'log2'],
        },
        "CatBoost": {
            'depth': [4, 6, 8, 10],
            'learning_rate': [0.01, 0.05, 0.1],
            'iterations': [200, 500, 1000],
            'l2_leaf_reg': [1, 3, 5, 7],
        },
        "Adaboost": {
            'n_estimators': [50, 100, 200],
            'learning_rate': [0.01, 0.1, 0.5, 1],
            'loss': ['linear', 'square', 'exponential']
        },
        "XGBoost": {
            'n_estimators': [50, 100, 200],
            'learning_rate': [0.01, 0.1, 0.3],
            'max_depth': [3, 5, 7],
            'colsample_bytree': [0.3, 0.5, 0.7, 1],
            'subsample': [0.6, 0.8, 1.0],
            'gamma': [0, 0.1, 0.3],
            'reg_lambda': [1, 1.5, 2],
        },
        "Random Forest": {
            'n_estimators': [100, 200, 300],
            'max_depth': [None, 10, 20, 30],
            'min_samples_split': [2, 5, 10],
            'min_samples_leaf': [1, 2, 4],
            'bootstrap': [True, False],
            'max_features': ['auto', 'sqrt', 'log2'],
        }
    }