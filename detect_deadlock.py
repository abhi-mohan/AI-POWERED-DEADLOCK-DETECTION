import joblib
import numpy as np

# Load trained model
MODEL_PATH = "/content/deadlock_predictor.pkl"  # Update this path if needed
model = joblib.load(MODEL_PATH)

def detect_deadlock(process_resource_matrix):
    """
    Detects if a deadlock is present based on the input matrix.
    
    :param process_resource_matrix: 2D list or numpy array representing process-resource allocation
    :return: "🔴 Deadlock Detected!" or "✅ No Deadlock Detected"
    """
    input_data = np.array(process_resource_matrix).reshape(1, -1)  # Reshape for model prediction
    prediction = model.predict(input_data)

    return "🔴 Deadlock Detected!" if prediction == 1 else "✅ No Deadlock Detected"

# Example usage
if __name__ == "__main__":
    sample_data = [[1, 0, 1, 0, 0, 1, 0, 0]]  # Modify as per your dataset format
    result = detect_deadlock(sample_data)
    print(result)
