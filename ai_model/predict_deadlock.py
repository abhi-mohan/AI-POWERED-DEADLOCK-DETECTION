import pandas as pd
import joblib

# Load trained model
model = joblib.load("/content/deadlock_predictor.pkl")

# Example new data for prediction
new_data = pd.DataFrame({
    "alloc_R1": [1], "alloc_R2": [0], "alloc_R3": [2],
    "max_R1": [3], "max_R2": [2], "max_R3": [2],
    "avail_R1": [1], "avail_R2": [0], "avail_R3": [1]
})

# Ensure column order matches training data
new_data = new_data[model.feature_names_in_]

# Predict Deadlock
prediction = model.predict(new_data)
print("🔴 Deadlock Detected!" if prediction[0] == 1 else "✅ No Deadlock.")
