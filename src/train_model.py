import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
import joblib

def train_model():
    # We load the data
    data = pd.read_csv('../data/iris.csv')
    X = data.drop('species', axis=1)
    y = data['species']

    # Here We Split data into train and test sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Training a simple Random Forest classifier
    model = RandomForestClassifier()
    model.fit(X_train, y_train)

    # We make predictions on the test set
    predictions = model.predict(X_test)

    # We check model accureacy and print it out
    accuracy = accuracy_score(y_test, predictions)
    print(f'Model Accuracy: {accuracy}')

    # Save the trained model to current directory ies
    joblib.dump(model, '../models/model.joblib')

if __name__ == 'main':
    train_model()