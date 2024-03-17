import pandas as pd

def prepare_data(data: pd.DataFrame):
    """
    Prepare the data by splitting it into features and target variable.

    Parameters:
    - data (pd.DataFrame): DataFrame containing the dataset.

    Returns:
    - X (pd.DataFrame): DataFrame containing the features.
    - y (pd.Series): Series containing the target variable.
    """
    X = data.drop(columns=['target'])
    y = data['target']
    return (X, y)
