# 🚀 AI-Powered Deadlock Detection - Installation Guide

This document provides a step-by-step guide to setting up and running the **AI-Powered Deadlock Detection** system.

---

## 🛠️ Prerequisites

Before you begin, ensure you have the following installed on your system:

- ✅ **Python 3.7+** (Check by running `python --version`)
- ✅ **pip** (Python package manager)
- ✅ **Git** (For cloning the repository, optional)
- ✅ **Tkinter** (For GUI functionality, see Step 4 for installation)

### 🔍 **Checking Your System Setup**

Run the following commands to verify you have everything installed:

```bash
python --version  # Check Python version
pip --version     # Check if pip is installed
git --version     # Check if Git is installed (optional)
```

---

## 📥 Step 1: Clone the Repository

Use Git to clone the project to your local machine:

```bash
git clone https://github.com/abhi-mohan/AI-POWERED-DEADLOCK-DETECTION.git
cd AI-POWERED-DEADLOCK-DETECTION
```

If you don’t have Git, you can download the repository as a ZIP file from GitHub and extract it manually.

---

## 🛠️ Step 2: Set Up a Virtual Environment (Recommended)

To avoid dependency conflicts, create a virtual environment:

```bash
python -m venv venv
```

Activate the virtual environment:

- **Windows:**

  ```bash
  venv\Scripts\activate
  ```

- **Mac/Linux:**

  ```bash
  source venv/bin/activate
  ```

If you see `(venv)` in your terminal prompt, the environment is active.

---

## 📦 Step 3: Install Required Dependencies

Run the following command to install all necessary libraries:

```bash
pip install -r requirements.txt
```

This installs:

- Flask (for the web-based GUI)
- Tkinter (for the desktop GUI)
- Numpy, Pandas (for data processing)
- Other required dependencies for deadlock detection

---

## 🖥️ Step 4: Install Tkinter (If Not Already Installed)

Tkinter is required for the desktop GUI.

- **For Ubuntu/Debian:**

  ```bash
  sudo apt-get install python3-tk
  ```

- **For Mac (if missing):**

  ```bash
  brew install python-tk
  ```

- **For Windows:** Tkinter comes pre-installed with Python.

To test if Tkinter is installed, run:

```bash
python -m tkinter
```

If a small window appears, Tkinter is correctly installed.

---

## 🎯 Step 5: Running the Application

### Running the Tkinter Desktop GUI

```bash
python gui/gui.py
```

This opens a desktop application where you can enter process-resource allocation details and detect deadlocks.

### Running the Flask Web Interface

```bash
python gui/app.py
```

Then, open your browser and visit:

👉 [http://127.0.0.1:5000/](http://127.0.0.1:5000/)

This launches a web-based interface for deadlock detection.

---

## 🛠️ Troubleshooting

| Issue                      | Possible Solution                                   |
|----------------------------|-----------------------------------------------------|
| `flask` module not found   | Run `pip install flask`                            |
| `tkinter` ImportError      | Install Tkinter (see Step 4)                       |
| `requirements.txt` missing | Run `git pull origin main` to update repo         |
| Port 5000 already in use   | Change port in `app.py`: `app.run(port=5001)`     |
| Virtual env not activating | Use `source venv/bin/activate` (Mac/Linux) or `venv\Scripts\activate` (Windows) |

🚀 Installation complete! Now, refer to the **Usage Guidelines (`USAGE.md`)** to start using the system.

---

## 📌 **Next Steps**

Refer to [`USAGE.md`](USAGE.md) for detailed instructions on how to use the system.

