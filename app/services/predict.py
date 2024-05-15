import joblib
import os
import pandas as pd


def predict(data):
    """ Predict the class of a given iris sample """

    # Load model

    with open(os.path.join(os.path.dirname(__file__), "../ml/model/DecisionTreeRegressor_model.pkl"), 'rb') as file:
        model = joblib.load(file)
        df = pd.DataFrame(data=[data.values()], columns=data.keys())
        prediction = model.predict(df)

        return prediction[0]
