# 🖥️ Log File Analyzer

A beginner-friendly Python project that analyzes application log files, counts event types, and identifies errors using a desktop GUI or terminal interface.

## ✨ Features

- 🪟 Desktop GUI built with Tkinter
- 📂 Open and analyze `.log` and `.txt` files
- 📊 Count `DEBUG`, `INFO`, `WARNING`, `ERROR`, and `CRITICAL` events
- 🚨 Display error and critical event details
- 💾 Save analysis reports as text files
- 💻 Terminal-based analysis using Python

## 🛠️ Technologies Used

- **Python 3**
- **Tkinter** — desktop graphical interface
- **Regular Expressions (`re`)** — detect log event types
- **Counter** — count event categories
- **Git & GitHub** — version control and project hosting

## 📁 Project Structure

```text
log-file-analyzer/
├── app.py
├── main.py
├── application.log
├── README.md
├── .gitignore
└── report.txt
```

- `app.py` — desktop graphical interface
- `main.py` — terminal-based analyzer
- `application.log` — sample log file
- `README.md` — project documentation
- `.gitignore` — files Git should ignore
- `report.txt` — generated analysis report, if present

## ⚙️ Requirements

- Python 3 installed on your computer
- Tkinter available in your Python installation

No third-party Python packages are required.

## 🚀 How to Run

### 1. Clone the repository

```bash
git clone https://github.com/vrushabhakamdi-dev/log-file-analyzer.git
cd log-file-analyzer
```

### 2. Launch the desktop GUI

```bash
python app.py
```

Click **Open & Analyze Log**, select your log file, and review the results. Click **Save Report** to export the analysis.

### 3. Run the terminal version

```bash
python main.py
```

Make sure `application.log` is in the project folder if your terminal script expects that filename.

## 📋 Example Log Entries

```text
2026-10-10 09:03:20 INFO Application started
2026-10-10 09:03:25 WARNING High memory usage
2026-10-10 09:03:30 ERROR Database connection failed
```

The analyzer identifies event types, counts them, and displays error details.

## 🎯 What I Learned

- Reading and processing files with Python
- Using regular expressions
- Counting and categorizing log events
- Building desktop applications with Tkinter
- Generating text reports
- Using Git and GitHub

## 🔮 Future Improvements

- Filter logs by date and severity
- Add charts and visual analytics
- Search for specific log messages
- Export reports to CSV
- Add advanced log filtering

## 👨‍💻 Author

**Vrushabh Kamdi**

GitHub: [@vrushabhakamdi-dev](https://github.com/vrushabhakamdi-dev)

## 📄 License

This project is open source. A license has not yet been specified.