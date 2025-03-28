import numpy as np
import pandas as pd
from sklearn.tree import DecisionTreeClassifier
import joblib

# Sample training dataset (features: process allocation patterns, label: deadlock/no deadlock)
data = {
  "P1_R1": [1, 0, 1, 0, 1, 0],
  "P1_R2": [0, 1, 1, 0, 0, 1],
  "P2_R1": [1, 0, 0, 1, 1, 0],
  "P2_R2": [0, 1, 0, 1, 0, 1],
  "Deadlock": [1, 0, 1, 0, 1, 0],  # 1 = Deadlock, 0 = No Deadlock
}

df = pd.DataFrame(data)

# Features (X) and Labels (y)
X = df.drop(columns=["Deadlock"])
y = df["Deadlock"]

# Train Decision Tree Model
model = DecisionTreeClassifier()
model.fit(X, y)

# Save the trained model
joblib.dump(model, "deadlock_model.pkl")

print("✅ AI Model Trained and Saved Successfully!")
