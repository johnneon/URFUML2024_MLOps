from sklearn.metrics import mean_squared_error as mse
import pandas as pd
import joblib
import os

from app.ml.metric.metric_mse_r2 import calculate_metric


def predict():
    X_train = pd.read_csv(os.path.join(os.path.dirname(__file__), 'train/X_val.csv'))
    y_train = pd.read_csv(os.path.join(os.path.dirname(__file__), 'train/y_val.csv'))

    model = joblib.load(os.path.join(os.path.dirname(__file__), "model/DecisionTreeRegressor_model.pkl"))

    predict_new_data = model.predict(X_train)

    print(f"r2 на валидационной выборке: {calculate_metric(model, X_train, y_train):.4f}")
    print(f"mse на валидационной выборке: {calculate_metric(model, X_train, y_train, mse):.4f}")


predict()
