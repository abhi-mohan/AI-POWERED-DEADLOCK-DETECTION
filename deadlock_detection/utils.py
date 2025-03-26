import numpy as np

def preprocess_input(raw_data):
    """
    Convert raw process-resource data into a structured format.
    
    :param raw_data: Raw input data (list of lists or dict format)
    :return: Processed numpy array ready for model prediction
    """
    return np.array(raw_data).reshape(1, -1)

def display_result(prediction):
    """
    Convert model output to a user-friendly message.
    
    :param prediction: Model's output (0 or 1)
    :return: Readable status message
    """
    return "🔴 Deadlock Detected!" if prediction == 1 else "✅ No Deadlock Detected"
