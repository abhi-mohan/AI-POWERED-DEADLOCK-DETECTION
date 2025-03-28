import numpy as np
import joblib

# Load trained model
model = joblib.load("deadlock_model.pkl")

# Sample input (modify to test different scenarios)
test_input = np.array([[1, 0, 1, 0]])  # Example: Process allocation state

# Predict deadlock
prediction = model.predict(test_input)

if prediction[0] == 1:
    print("🔴 Deadlock Predicted!")
else:
    print("🟢 No Deadlock Detected.")
