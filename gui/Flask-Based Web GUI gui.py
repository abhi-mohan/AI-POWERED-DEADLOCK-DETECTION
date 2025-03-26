from flask import Flask, render_template, request
import pandas as pd
import joblib

app = Flask(__name__)

# Load the trained model
MODEL_PATH = "/content/deadlock_predictor.pkl"
model = joblib.load(MODEL_PATH)

@app.route("/", methods=["GET", "POST"])
def index():
    result = None

    if request.method == "POST":
        file = request.files["file"]
        if file:
            new_data = pd.read_csv(file)
            new_data = new_data[model.feature_names_in_]
            prediction = model.predict(new_data)
            result = "🔴 Deadlock Detected!" if prediction[0] == 1 else "✅ No Deadlock."

    return render_template("index.html", result=result)

if __name__ == "__main__":
    app.run(debug=True)
