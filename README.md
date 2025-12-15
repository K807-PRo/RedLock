# 🔐 RedLock — Educational Python Project (Open Source)

⚠️ **EDUCATIONAL PURPOSES ONLY** ⚠️

RedLock is an **open‑source Python project** that simulates a *lock‑screen / ransomware‑style* graphical interface **for learning and cybersecurity awareness**. It does **not** encrypt files and is **not real malware**. The goal is to understand GUI behavior, Windows file handling, permissions, and packaging Python apps into executables.

---

## 📌 Features

* Full‑screen **Tkinter GUI** (borderless, always on top)
* **Key‑based unlock** logic
* Demonstrates **Windows Startup folder** behavior (user‑level)
* Safe **file copy & delete** operations with permission handling
* Threaded logic to keep the GUI responsive
* Can be packaged as a **Windows `.exe`** using PyInstaller

---

## 🧠 Educational Goals

* Learn **Python GUI development** with Tkinter
* Understand **Windows paths & environment variables**
* Practice **file system operations** safely
* Handle **PermissionError** correctly
* Learn how Python apps are **packaged to EXE**
* Raise awareness about **social‑engineering lock screens**

---

## 🛠️ Technologies

* **Python 3**
* **Tkinter**
* `os`, `sys`, `shutil`
* `threading`
* **Windows OS**
* **PyInstaller** (for EXE build)

---

## 📂 Project Structure

```
RedLock/
 ├─ build/
 ├─ dist/
 │   └─ redlock.exe
 ├─ redlock.py
 ├─ redlock.spec
 └─ README.md
```

RedLock/
├─ redlock.py
├─ README.md
└─ .gitignore

```

---

## 🔑 Default Unlock Key

For educational testing purposes, the default unlock key used in this project is:

```

11.11.11.11

````

> ⚠️ This key is **hard‑coded for learning and demonstration only**. Do **NOT** use real passwords or secrets in production code.

---

## ▶️ How It Works (High‑Level)

1. The script checks the **user Startup folder**.
2. If the executable is not present, it copies itself there (user‑level, educational).
3. A **full‑screen red GUI** is displayed.
4. The user enters a **key**.
5. If the key is correct:
   - The program attempts to remove a predefined test file.
   - Permission errors are caught and displayed.
6. The application closes after unlock.

> ℹ️ No encryption is performed. No personal files are touched.

---

## 🚀 Run the Project (Python)

### Requirements
- Windows
- Python 3.9+

### Run
```bash
python redlock.py
````

---

## 🧱 Build `.exe` (Windows)

### 1) Install PyInstaller

```bash
pip install pyinstaller
```

### 2) Build (GUI — no console)

```bash
pyinstaller --onefile --noconsole redlock.py
```

### 3) Output

The executable will be located in:

```
dist/redlock.exe
```

### (Optional) Add Icon

```bash
pyinstaller --onefile --noconsole --icon=icon.ico redlock.py
```

---

## ⚠️ Important Warnings

* ❌ Do **NOT** use this code to harm systems or users
* ❌ Do **NOT** deploy without explicit permission
* ❌ Do **NOT** modify for malicious intent

This repository is shared **strictly for educational and demonstration purposes**.

---

## 📜 License

**MIT License** — Open Source.

You are free to study, modify, and share this project **for educational use**.

---

## 🔗 Repository

GitHub: [https://github.com/K807-PRo/RedLock.git](https://github.com/K807-PRo/RedLock.git)

---

> "To defend against threats, you must first understand how they work."
