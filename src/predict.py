import pandas as pd
import joblib

def predict(input_data):
    # Now we Load the trained model
    model = joblib.load('../models/model.joblib')

    # We make predictions
    predictions = model.predict(input_data)

    return predictions