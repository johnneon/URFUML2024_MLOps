import numpy as np
from sklearn.base import BaseEstimator, TransformerMixin
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline


class QuantileReplacer(BaseEstimator, TransformerMixin):
    def __init__(self, threshold=0.05):
        self.threshold = threshold
        self.quantiles = {}

    def fit(self, X, y=None):
        for col in X.select_dtypes(include='number'):
            low_quantile = X[col].quantile(self.threshold)
            high_quantile = X[col].quantile(1 - self.threshold)
            self.quantiles[col] = (low_quantile, high_quantile)
        return self

    def transform(self, X):
        X_copy = X.copy()
        for col in X.select_dtypes(include='number'):
            low_quantile, high_quantile = self.quantiles[col]
            rare_mask = ((X[col] < low_quantile) | (X[col] > high_quantile))
            if rare_mask.any():
                rare_values = X_copy.loc[rare_mask, col]
                replace_value = np.mean([low_quantile, high_quantile])
                if rare_values.mean() > replace_value:
                    X_copy.loc[rare_mask, col] = high_quantile
                else:
                    X_copy.loc[rare_mask, col] = low_quantile
        return X_copy


class RareGrouper(BaseEstimator, TransformerMixin):
    def __init__(self, threshold=0.05, other_value='Other'):
        self.threshold = threshold
        self.other_value = other_value
        self.freq_dict = {}

    def fit(self, X, y=None):
        for col in X.select_dtypes(include=['object']):
            freq = X[col].value_counts(normalize=True)
            self.freq_dict[col] = freq[freq >= self.threshold].index.tolist()
        return self

    def transform(self, X, y=None):
        X_copy = X.copy()
        for col in X.select_dtypes(include=['object']):
            X_copy[col] = X_copy[col].apply(lambda x: x if x in self.freq_dict[col] else self.other_value)
        return X_copy


class TargetEncoder(BaseEstimator, TransformerMixin):
    def __init__(self, cols=None):
        self.cols = cols
        self.target_mean = {}

    def fit(self, X, y):
        if self.cols is None:
            self.cols = X.columns
        for col in self.cols:
            self.target_mean[col] = {}
            X_copy = X.copy()
            X_copy[y.name] = y
            self.target_mean[col] = X_copy.groupby(col)[y.name].mean().to_dict()
        return self

    def transform(self, X):
        for col in self.cols:
            X[col] = X[col].map(self.target_mean[col])
            X[col] = X[col].fillna(np.mean(X[col]))
        return X


# num_pipe_longitude = Pipeline([
#     ('QuantReplace', QuantileReplacer(threshold=0.01, )),
#     ('scaler', None)
# ])
#
# num_longitude = ['longitude']

# num_pipe_latitude = Pipeline([
#     ('scaler', None)
# ])
#
# num_latitude = ['latitude']

num_pipe_housing_median_age = Pipeline([
    ('QuantReplace', QuantileReplacer(threshold=0.01, )),
    ('power', None)
])

num_housing_median_age = ['housing_median_age']

num_pipe_total_rooms = Pipeline([
    ('scaler', None)
])

num_total_rooms = ['total_rooms']

num_pipe_total_bedrooms = Pipeline([
    ('scaler', None)
])

num_total_bedrooms = ['total_bedrooms']

num_pipe_population = Pipeline([
    ('scaler', None)
])

num_population = ['population']

num_pipe_households = Pipeline([
    ('scaler', None)
])

num_households = ['households']

num_pipe_median_income = Pipeline([
    ('scaler', None)
])

num_median_income = ['median_income']

cat_pipe_ocean_proximity = Pipeline([
    ('replace_rare', RareGrouper(threshold=0.001, other_value='Other')),
    ('encoder', TargetEncoder())
])

cat_ocean_proximity = ['ocean_proximity']

preprocessors = ColumnTransformer(transformers=[
    # ('num_longitude', num_pipe_longitude, num_longitude),
    # ('num_latitude', num_pipe_latitude, num_latitude),
    ('num_housing_median_age', num_pipe_housing_median_age, num_housing_median_age),
    ('num_total_rooms', num_pipe_total_rooms, num_total_rooms),
    ('num_total_bedrooms', num_pipe_total_bedrooms, num_total_bedrooms),
    ('num_population', num_pipe_population, num_population),
    ('num_households', num_pipe_households, num_households),
    ('num_median_income', num_pipe_median_income, num_median_income),
])

preprocessors_all = ColumnTransformer(transformers=[
    # ('num_longitude', num_pipe_longitude, num_longitude),
    # ('num_latitude', num_pipe_latitude, num_latitude),
    ('num_housing_median_age', num_pipe_housing_median_age, num_housing_median_age),
    ('num_total_rooms', num_pipe_total_rooms, num_total_rooms),
    ('num_total_bedrooms', num_pipe_total_bedrooms, num_total_bedrooms),
    ('num_population', num_pipe_population, num_population),
    ('num_households', num_pipe_households, num_households),
    ('num_median_income', num_pipe_median_income, num_median_income),
    ('cat_ocean_proximity', cat_pipe_ocean_proximity, cat_ocean_proximity),
])

columns = np.hstack([# num_longitude,
                     # num_latitude,
                     num_housing_median_age,
                     num_total_rooms,
                     num_total_bedrooms,
                     num_population,
                     num_households,
                     num_median_income,
                     cat_ocean_proximity,
                     ])
