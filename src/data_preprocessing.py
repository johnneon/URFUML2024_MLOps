import opendatasets as od
import pandas as pd
from scipy.stats import yeojohnson
from sklearn.model_selection import train_test_split

od.download("https://www.kaggle.com/datasets/camnugent/california-housing-prices", force=False)


def preprocessing(data: pd.DataFrame, threshold=0.01) -> pd.DataFrame:
    cat_columns = []
    num_columns = []

    # Разделение столбцов на категориальные и числовые
    for column_name in data.columns:
        if data[column_name].dtypes == 'object':
            cat_columns.append(column_name)
        else:
            num_columns.append(column_name)

    # Определение порога для удаления столбцов
    threshold = threshold * len(data)

    # Обработка категориальных столбцов
    for column in cat_columns:
        if data[column].isna().sum() <= threshold:
            data = data.dropna(subset=column)
        else:
            data[column] = data[column].fillna('Other')

    # Обработка числовых столбцов
    for column in num_columns:
        if data[column].isna().sum() <= threshold:
            data = data.dropna(subset=column)
        else:
            data[column] = data[column].fillna(data[column].median())
    data.reset_index(drop=True, inplace=True)
    return data, cat_columns, num_columns


def delete_columns(data: pd.DataFrame, *args) -> pd.DataFrame:
    for column in args:
        if column in data.columns:
            data = data.drop(column, axis=1)
    return data


def normal_distribution(data: pd.DataFrame, num_columns: list) -> pd.DataFrame:
    for column in num_columns:
        if data[column].dtype != 'object':
            data[column], _ = yeojohnson(data[column])
    return data


def to_teach_and_separate_data():
    df = pd.read_csv('california-housing-prices/housing.csv')

    df = delete_columns(df, 'longitude', 'latitude')

    df, _, num_columns = preprocessing(df)

    df = normal_distribution(df, num_columns)

    X, y = df.drop(columns=['median_house_value']), df['median_house_value']

    X_train, X_val, y_train, y_val = train_test_split(X, y, test_size=0.3, random_state=42)

    X_train.to_csv('test/X_train.csv', index=False)
    y_train.to_csv('test/y_train.csv', index=False)

    X_val.to_csv('train/X_val.csv', index=False)
    y_val.to_csv('train/y_val.csv', index=False)


if __name__ == '__main__':
    to_teach_and_separate_data()
