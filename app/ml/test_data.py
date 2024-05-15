from sklearn.metrics import mean_squared_error as mse
import pandas as pd
import joblib
import os

from app.ml.metric.metric_mse_r2 import calculate_metric


def test_dataset():
    X_val = pd.read_csv(os.path.join(os.path.dirname(__file__), 'test/X_val.csv'))
    y_val = pd.read_csv(os.path.join(os.path.dirname(__file__), 'test/y_val.csv'))

    model = joblib.load(os.path.join(os.path.dirname(__file__), "model/DecisionTreeRegressor_model.pkl"))

    predict_new_data = model.predict(X_val)

    print('    Тестирование валидационной выборки     ')
    print(f"r2 на валидационной выборке: {calculate_metric(model, X_val, y_val):.4f}")
    print(f"mse на валидационной выборке: {calculate_metric(model, X_val, y_val, mse):.4f}")
    assert mse < 3.0, 'MSE превышает 3.0'
    print()


def test_dataset1():
    X_train = pd.read_csv(os.path.join(os.path.dirname(__file__), 'train/X_train.csv'))
    y_train = pd.read_csv(os.path.join(os.path.dirname(__file__), 'train/y_train.csv'))

    model = joblib.load(os.path.join(os.path.dirname(__file__), "model/DecisionTreeRegressor_model.pkl"))

    predict_new_data = model.predict(X_train)

    print('    Тестирование тренировочной выборки     ')
    print(f"r2 на тренировочной выборке: {calculate_metric(model, X_train, y_train):.4f}")
    print(f"mse на тренировочной выборке: {calculate_metric(model, X_train, y_train, mse):.4f}")
    assert mse < 3.0, 'MSE превышает 3.0'
    print()





