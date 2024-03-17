import pandas as pd

def clean_data(data) -> pd.DataFrame:
    """
    Clean the loaded data by converting it into a DataFrame.

    Parameters:
    - data (Bunch): Dictionary-like object containing the dataset.

    Returns:
    - cleaned_data (pd.DataFrame): DataFrame containing the cleaned data.
    """
    cleaned_data = pd.DataFrame(data.data, columns=data.feature_names)
    cleaned_data['target'] = data.target
    return cleaned_data