# Log File Analyzer

A beginner-friendly Python project that reads application log files, counts event types, and identifies errors through a desktop GUI or terminal interface.

## Features

- Desktop interface built with Tkinter
- Analyze application log files
- Count DEBUG, INFO, WARNING, ERROR, and CRITICAL events
- Display error details
- Save analysis reports as text files
- Terminal-based analysis using Python

## Requirements

- Python 3
- Tkinter (usually included with standard Windows Python installations)

No third-party Python packages are required.

## How to Run

### Desktop GUI

```bash
python app.py
```

Click **Open & Analyze Log**, select a `.log` or `.txt` file, and review the results. Use **Save Report** to export the analysis.

### Terminal Version

```bash
python main.py
```

Make sure `application.log` is present in the project folder if your terminal script uses that default filename.

## Project Structure

```text
log-file-analyzer/
├── app.py
├── main.py
├── application.log
├── README.md
├── .gitignore
└── screenshots/
```

## What I Learned

- Reading text files with Python
- Searching log messages using regular expressions
- Counting event types
- Creating a GUI with Tkinter
- Saving reports to files
- Using Git and GitHub

## Future Improvements

- Filter logs by date or severity
- Add charts for event counts
- Search for specific messages
- Export reports to CSV

## License

This project is available under the MIT License.