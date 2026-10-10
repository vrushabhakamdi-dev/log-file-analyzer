from pathlib import Path
import re
from collections import Counter

# File locations
BASE_DIR = Path(__file__).resolve().parent
LOG_FILE = BASE_DIR / "application.log"
REPORT_FILE = BASE_DIR / "report.txt"

# Event types we want to count
EVENT_TYPES = ["DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"]


def analyze_log(file_path):
    """Read a log file and collect statistics."""
    counts = Counter()
    error_messages = []
    invalid_lines = 0
    total_lines = 0

    # Recognize severity labels without case sensitivity
    pattern = re.compile(
        r"\b(DEBUG|INFO|WARNING|ERROR|CRITICAL)\b",
        re.IGNORECASE
    )

    try:
        with file_path.open("r", encoding="utf-8", errors="replace") as file:
            for line in file:
                total_lines += 1
                cleaned_line = line.strip()

                if not cleaned_line:
                    continue

                match = pattern.search(cleaned_line)
                if match:
                    # Normalize to uppercase for consistent counting
                    event_type = match.group(1).upper()
                    counts[event_type] += 1

                    # Collect errors and critical messages for quick review
                    if event_type in ("ERROR", "CRITICAL"):
                        error_messages.append(cleaned_line)
                else:
                    invalid_lines += 1

    except FileNotFoundError:
        print(f"[-] Error: Could not find log file at {file_path}")
        return None
    except Exception as e:
        print(f"[-] An unexpected error occurred: {e}")
        return None

    return {
        "total_lines": total_lines,
        "recognized_events": sum(counts.values()),
        "invalid_lines": invalid_lines,
        "counts": counts,
        "error_messages": error_messages
    }


def create_report(data):
    """Format analysis data into a readable report structure."""
    if not data:
        return ""

    counts = data["counts"]
    total_events = data["recognized_events"]

    # Find the most frequent event type safely
    if total_events > 0:
        most_common_type, most_common_count = counts.most_common(1)[0]
        frequent_str = f"{most_common_type} ({most_common_count})"
    else:
        frequent_str = "None"

    # Build report lines
    report_lines = [
        "=" * 42,
        "          LOG FILE ANALYZER",
        "=" * 42,
        f"Total lines read: {data['total_lines']}",
        f"Recognized events: {total_events}",
        f"Unrecognized non-empty lines: {data['invalid_lines']}",
        "",
        "EVENT COUNTS",
        "-" * 25,
    ]

    for event in EVENT_TYPES:
        report_lines.append(f"{event:<10} : {counts[event]}")

    report_lines.extend([
        f"Most frequent event type: {frequent_str}",
        "",
        "ERROR DETAILS",
        "-" * 25,
    ])

    if data["error_messages"]:
        report_lines.extend(data["error_messages"])
    else:
        report_lines.append("No errors or critical events found.")

    report_lines.append("")
    return "\n".join(report_lines)


def main():
    """Coordinate the log analysis workflow."""
    print("[*] Starting Log File Analyzer...")

    # Run analysis
    analysis_data = analyze_log(LOG_FILE)

    if analysis_data is None:
        return

    # Generate report text
    report_content = create_report(analysis_data)

    # Print report to terminal
    print("\n" + report_content)

    # Save report to report.txt
    try:
        REPORT_FILE.write_text(report_content, encoding="utf-8")
        print(f"Report saved to: {REPORT_FILE.name}")
    except Exception as e:
        print(f"[-] Failed to save report file: {e}")


if __name__ == "__main__":
    main()