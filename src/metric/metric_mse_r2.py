from sklearn.metrics import r2_score


def calculate_metric(model_pipe, X, y, metric=r2_score):
    y_model = model_pipe.predict(X)
    return metric(y, y_model)
