from sklearn.metrics import mean_squared_error as mse
import pandas as pd
import joblib
import os

from metric.metric_mse_r2 import calculate_metric


def predict():
    X_val = pd.read_csv(os.path.join(os.path.dirname(__file__), 'test/X_val.csv'))
    y_val = pd.read_csv(os.path.join(os.path.dirname(__file__), 'test/y_val.csv'))

    model = joblib.load(os.path.join(os.path.dirname(__file__), "model/DecisionTreeRegressor_model.joblib"))

    predict_new_data = model.predict(X_val)

    print(f"r2 на валидационной выборке: {calculate_metric(model, X_val, y_val):.4f}")
    print(f"mse на валидационной выборке: {calculate_metric(model, X_val, y_val, mse):.4f}")


predict()
