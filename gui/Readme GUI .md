📌 GUI Module - Deadlock Detection
This folder contains the GUI implementation for the Deadlock Detector. The GUI allows users to input process-resource allocations and detect deadlocks using the trained AI model.

🚀 Installation
Ensure you have Python 3.7+ installed. Then, install the required dependencies using:

bash
Copy
Edit
pip install flask tkinter
If tkinter is not included in your Python distribution, install it separately:

For Ubuntu/Debian:

bash
Copy
Edit
sudo apt-get install python3-tk
For Mac (if missing):

bash
Copy
Edit
brew install python-tk
For Windows, Tkinter comes pre-installed with Python.

📂 Files in gui/
app.py → Flask-based GUI for web-based interaction

gui.py → Tkinter-based desktop GUI

templates/ → Contains HTML files for Flask GUI

static/ → Stores CSS & JS for the web interface

🎯 How to Run
1️⃣ Run the Tkinter GUI
bash
Copy
Edit
python gui.py
2️⃣ Run the Flask Web Interface
bash
Copy
Edit
python app.py
Then, open your browser and go to:
👉 http://127.0.0.1:5000/

🛠️ Troubleshooting
Flask not found? → Run pip install flask

Tkinter error? → Ensure Python is installed with Tkinter support

Port 5000 already in use? → Change the port in app.py (e.g., app.run(port=5001))
