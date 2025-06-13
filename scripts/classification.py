from sklearn.svm import SVC
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

def train_and_evaluate(features, labels):
    """
    Trains an SVM classifier on extracted EEG features and evaluates its accuracy.

    Parameters:
        features (list of dict): List of feature dictionaries
        labels (list): List of labels (e.g., 0 for low focus, 1 for high focus)

    Returns:
        model: Trained SVM model
        float: Accuracy on test set
    """
    import pandas as pd
    df = pd.DataFrame(features)

    # Split the dataset
    X_train, X_test, y_train, y_test = train_test_split(df, labels, test_size=0.2, random_state=42)

    # Train SVM classifier
    model = SVC(kernel='linear')
    model.fit(X_train, y_train)

    # Predict and evaluate
    y_pred = model.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)

    return model, accuracy
