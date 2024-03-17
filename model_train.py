import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# Step 3: Model Training and Evaluation
def train_and_evaluate(X: pd.DataFrame, y: pd.Series) -> float:
    """
    Train a logistic regression model and evaluate its accuracy.

    Parameters:
    - X (pd.DataFrame): DataFrame containing the features.
    - y (pd.Series): Series containing the target variable.

    Returns:
    - accuracy (float): accuracy score of the trained model.
    """
    # Split data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    # Train logistic regression model
    model = LogisticRegression()
    model.fit(X_train, y_train)
    
    # Evaluate model
    y_pred = model.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)
    return accuracy