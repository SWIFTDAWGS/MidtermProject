import sys
from src.predict import predict

if __name__ == 'main':
    # Example input data for prediction
    test_data = [[5.1, 3.5, 1.4, 0.2], [6.2, 3.4, 5.4, 2.3]]

    # Make predictions
    predictions = predict(test_data)

    # Print predictions
    for i, pred in enumerate(predictions):
        print(f'Prediction for example {i + 1}: {pred}')

print(sys.path)