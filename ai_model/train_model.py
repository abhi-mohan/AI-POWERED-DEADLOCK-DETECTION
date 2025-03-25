import pandas as pd
import joblib
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import accuracy_score

# Load Dataset
dataset_path = "/content/data/deadlock_dataset.csv"  # Ensure this path is correct
df = pd.read_csv(dataset_path)

# Encode categorical data if any
encoder = LabelEncoder()
df = df.apply(encoder.fit_transform)

# Split dataset into training & testing sets
X = df.drop(columns=["Deadlock"])  # Features
y = df["Deadlock"]  # Target variable

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train the model
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Evaluate the model
y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print(f"✅ Model trained with accuracy: {accuracy:.2f}")

# Save trained model
model_path = "/content/deadlock_predictor.pkl"
joblib.dump(model, model_path)
print(f"💾 Model saved as '{model_path}'")
