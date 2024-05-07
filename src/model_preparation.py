import pandas as pd
from sklearn.tree import DecisionTreeRegressor
from sklearn.pipeline import Pipeline
from sklearn.metrics import mean_squared_error as mse
import joblib

from pipeline import preprocessors_all
from metric.metric_mse_r2 import calculate_metric


def model_preparation():
    X_train = pd.read_csv("test/X_train.csv")
    y_train = pd.read_csv("test/y_train.csv").squeeze()

    pipe_all = Pipeline([
        ('preprocessors', preprocessors_all),
        ('model', DecisionTreeRegressor(max_leaf_nodes=40,
                                        min_samples_split=10,
                                        criterion='absolute_error'
                                        )
         )
    ])

    pipe_all.fit(X_train, y_train)

    joblib.dump(pipe_all, 'model/DecisionTreeRegressor_model.pkl')

    print(f"r2 на тренировочной выборке: {calculate_metric(pipe_all, X_train, y_train):.4f}")

    print(f"mse на тренировочной выборке: {calculate_metric(pipe_all, X_train, y_train, mse):.4f}")


model_preparation()
