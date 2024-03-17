import pandas as pd

def analyze_data(data: pd.DataFrame) -> None:
    """
    Perform analysis on the breast cancer dataset.

    Parameters:
    - data (pd.DataFrame): DataFrame containing the cleaned data.

    Returns:
    - None
    """
    # Example: Print summary statistics of numerical features
    print("Summary Statistics:")
    print(data.describe())
