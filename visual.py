import pandas as pd
import matplotlib.pyplot as plt


def visualize_data(data: pd.DataFrame) -> None:
    """
    Visualize the breast cancer dataset.

    Parameters:
    - data (pd.DataFrame): DataFrame containing the cleaned data.

    Returns:
    - None
    """
    # Example: Create a histogram of target variable (house prices)
    plt.hist(data['target'])
    plt.xlabel('Cancer type')
    plt.ylabel('Frequency')
    plt.title('Distribution of cancer')
    plt.show()