
import tkinter as tk
from tkinter import filedialog, messagebox
from collections import Counter
from pathlib import Path
import re

root = tk.Tk()
root.title("Log File Analyzer")
root.geometry("850x600")
root.configure(bg="#111827")

log_lines = []
log_file = Path("application.log")

title = tk.Label(
    root,
    text="LOG FILE ANALYZER",
    font=("Segoe UI", 24, "bold"),
    bg="#111827",
    fg="#38bdf8"
)
title.pack(pady=20)

subtitle = tk.Label(
    root,
    text="Analyze application logs and find errors",
    font=("Segoe UI", 11),
    bg="#111827",
    fg="white"
)
subtitle.pack()

output = tk.Text(
    root,
    height=20,
    width=90,
    bg="#1f2937",
    fg="#e5e7eb",
    font=("Consolas", 10),
    relief="flat"
)
output.pack(padx=20, pady=20, fill="both", expand=True)


def analyze_file():
    global log_lines

    filename = filedialog.askopenfilename(
        title="Choose a log file",
        filetypes=[("Log files", "*.log"), ("Text files", "*.txt"), ("All files", "*.*")]
    )

    if not filename:
        return

    try:
        with open(filename, "r", encoding="utf-8") as file:
            log_lines = file.readlines()
    except OSError as error:
        messagebox.showerror("File Error", str(error))
        return

    counts = Counter()
    errors = []
    unrecognized = 0

    for line in log_lines:
        match = re.search(
            r"\b(DEBUG|INFO|WARNING|ERROR|CRITICAL)\b",
            line,
            re.IGNORECASE
        )

        if match:
            level = match.group(1).upper()
            counts[level] += 1

            if level in ("ERROR", "CRITICAL"):
                errors.append(line.strip())
        elif line.strip():
            unrecognized += 1

    output.delete("1.0", tk.END)
    output.insert(tk.END, "LOG ANALYSIS REPORT\n")
    output.insert(tk.END, "=" * 45 + "\n\n")
    output.insert(tk.END, f"File: {filename}\n")
    output.insert(tk.END, f"Total lines: {len(log_lines)}\n")
    output.insert(tk.END, f"Unrecognized lines: {unrecognized}\n\n")

    output.insert(tk.END, "EVENT COUNTS\n")
    output.insert(tk.END, "-" * 30 + "\n")

    for level in ["DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"]:
        output.insert(tk.END, f"{level:<12}: {counts[level]}\n")

    output.insert(tk.END, "\nERROR DETAILS\n")
    output.insert(tk.END, "-" * 30 + "\n")

    if errors:
        for error in errors:
            output.insert(tk.END, error + "\n")
    else:
        output.insert(tk.END, "No errors found!\n")

    output.insert(tk.END, "\nAnalysis complete!\n")


def save_report():
    report = output.get("1.0", tk.END).strip()

    if not report:
        messagebox.showwarning("No Report", "Analyze a log file first.")
        return

    filename = filedialog.asksaveasfilename(
        title="Save report",
        defaultextension=".txt",
        filetypes=[("Text files", "*.txt")]
    )

    if filename:
        with open(filename, "w", encoding="utf-8") as file:
            file.write(report)

        messagebox.showinfo("Saved", "Report saved successfully!")


buttons = tk.Frame(root, bg="#111827")
buttons.pack(pady=10)

tk.Button(
    buttons,
    text="Open & Analyze Log",
    command=analyze_file,
    bg="#0284c7",
    fg="white",
    font=("Segoe UI", 11, "bold"),
    padx=15,
    pady=10,
    relief="flat"
).pack(side="left", padx=10)

tk.Button(
    buttons,
    text="Save Report",
    command=save_report,
    bg="#16a34a",
    fg="white",
    font=("Segoe UI", 11, "bold"),
    padx=15,
    pady=10,
    relief="flat"
).pack(side="left", padx=10)

root.mainloop()
