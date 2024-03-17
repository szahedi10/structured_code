from sklearn.datasets import load_breast_cancer

def load_data():
    """
    Load the breast cancer dataset from scikit-learn.

    Returns:
    - data (Bunch): Dictionary-like object containing the dataset.
    """
    data = load_breast_cancer()
    return data