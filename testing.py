from prepare_data import prepare_data
from load_data import load_data
from clean_data import clean_data
from analyze import analyze_data
from visual import visualize_data
from model_train import train_and_evaluate

if __name__ == "__main__":
    # Load data
    data = load_data()

    # Clean data
    cleaned_data = clean_data(data)

    # Analyze data
    analyze_data(cleaned_data)

    # Visualize data
    visualize_data(cleaned_data)

    # Prepare data
    X, y = prepare_data(cleaned_data)

    # Train and evaluate model
    accuracy = train_and_evaluate(X, y)
    print(f"Accuracy score: {accuracy:.2f}")