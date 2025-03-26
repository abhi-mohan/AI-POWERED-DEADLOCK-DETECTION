import tkinter as tk
from tkinter import filedialog, messagebox
import pandas as pd
import joblib

# Load the trained model
MODEL_PATH = "/content/deadlock_predictor.pkl"  # Update if needed
model = joblib.load(MODEL_PATH)

def predict_deadlock():
    try:
        file_path = filedialog.askopenfilename(title="Select CSV File", filetypes=[("CSV files", "*.csv")])
        if not file_path:
            return
        
        # Load input data
        new_data = pd.read_csv(file_path)
        
        # Ensure feature names match
        new_data = new_data[model.feature_names_in_]

        # Predict deadlock
        prediction = model.predict(new_data)
        result = "🔴 Deadlock Detected!" if prediction[0] == 1 else "✅ No Deadlock."
        
        messagebox.showinfo("Result", result)

    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {str(e)}")

# Create GUI window
root = tk.Tk()
root.title("Deadlock Detector")
root.geometry("400x200")

# Add widgets
label = tk.Label(root, text="Deadlock Detection System", font=("Arial", 14))
label.pack(pady=10)

btn = tk.Button(root, text="Select CSV & Predict", command=predict_deadlock, font=("Arial", 12), bg="lightblue")
btn.pack(pady=10)

exit_btn = tk.Button(root, text="Exit", command=root.quit, font=("Arial", 12), bg="red")
exit_btn.pack(pady=5)

root.mainloop()
