# 📖 AI-Powered Deadlock Detection - Usage Guide  

This document provides **detailed instructions** on how to use the **AI-Powered Deadlock Detection** system.  

---

## 🎯 1️⃣ Running the Tkinter Desktop GUI  

To launch the **desktop-based GUI**, use:  

```bash
python gui/gui.py
```

### 📌 Features:
✅ Enter process-resource allocation details  
✅ Click **"Detect Deadlock"** to analyze system state  
✅ View results in a user-friendly table format  
✅ Error messages if invalid input is provided  

### 🔹 Example Input Format:  

```
Processes: P1, P2, P3  
Resources: R1, R2, R3  
Allocation:  [ [1, 0, 1], [2, 1, 0], [0, 1, 1] ]  
Request:  [ [0, 1, 1], [1, 0, 0], [2, 1, 1] ]  
Available: [3, 2, 2]  
```

The system will evaluate the resource allocation and determine if a deadlock exists.  

---

## 🌐 2️⃣ Running the Flask Web Interface  

To use the web-based version, run:  

```bash
python gui/app.py
```

Then, open your browser and visit:  
👉 **http://127.0.0.1:5000/**  

### 📌 Features:
✅ Enter process-resource allocation data via web form  
✅ Click **"Check Deadlock"** to analyze system state  
✅ View deadlock detection results & recommendations  
✅ Responsive UI with CSS and JavaScript support  

---

## 📂 3️⃣ Understanding the Project Structure  

```
AI-POWERED-DEADLOCK-DETECTION/
│── gui/             # GUI implementations  
│   ├── app.py       # Flask-based web GUI  
│   ├── gui.py       # Tkinter-based desktop GUI  
│   ├── templates/   # HTML files for Flask GUI  
│   ├── static/      # CSS & JS for Flask web interface  
│── data/            # Sample input datasets for AI model  
│── logs/            # Logs system activities (app.log)  
│── model/           # AI model files for deadlock detection  
│── requirements.txt # Required dependencies  
│── README.md        # Main documentation  
│── INSTALLATION.md  # Installation instructions  
│── USAGE.md         # This file (Usage Guidelines)  
```

---

## 📌 4️⃣ Interpreting Deadlock Detection Results  

After entering resource allocation details and clicking **"Detect Deadlock"**, the system will return:  

✅ **"No Deadlock Detected"** → Safe state  
❌ **"Deadlock Detected!"** → Unsafe state  

If a deadlock is detected, the system will:  
- Identify the affected processes  
- Suggest resource reallocation to resolve the issue  
- Log details in **app.log** for debugging  

---

## 🛠️ 5️⃣ Troubleshooting  

| Issue                      | Solution |
|----------------------------|----------|
| Web GUI not loading        | Ensure `app.py` is running properly |
| Tkinter GUI not opening    | Install Tkinter (see **Installation Guide**) |
| Flask not installed        | Run `pip install flask` |
| Port 5000 busy             | Change port in `app.py`: `app.run(port=5001)` |
| Errors in resource input   | Ensure valid process-resource matrices |

---

🚀 **Now you’re ready to detect deadlocks efficiently! Happy coding! 🎉**
