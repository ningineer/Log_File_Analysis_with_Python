# Log File Analysis with Python

## Overview
This project is a Python-based log file analysis tool designed to automate log file parsing and identify critical patterns or events. Ideal for monitoring, security audits, and troubleshooting, this tool can quickly scan log files for important information such as errors, warnings, and specific event patterns.

## Features
- **Automated Log Parsing:** Quickly reads and processes log files.
- **Customizable Filters:** Allows filtering by keywords or log levels (e.g., ERROR, WARNING).
- **Anomaly Detection:** Detects patterns, such as failed login attempts, suspicious access times, or unauthorized access attempts.
- **Export Options:** Saves analyzed data into a report for easy reference.

## Getting Started

### Prerequisites
- **Python 3.x** installed on your system.
- Basic familiarity with log file structures and Python scripting.

### Installation
1. Clone this repository:
   ```bash
   git clone https://github.com/your-username/log-file-analysis-python.git

2. Navigate into the project directory:
   ```bash
   cd log-file-analysis-python

3. Install any required dependencies:
   ```bash
   pip install -r requirements.txt

## Usage
1. Place the log file you want to analyze into the project directory.
2. Run the script with your log file as an argument:
   ```bash
   python log_analysis.py example_log.txt

3. View the results in the console, or check the output file in the `output/` directory for a detailed report.

## Script Explanation
- Imports: The re module for regex filtering and datetime to timestamp the output file.
- Paths: Defines paths for the input log (example_log.txt) and the output file, which will be named with the current timestamp.
- parse_logs():
   - Searches each line of the log file for specific keywords (e.g., "ERROR" or "WARNING").
   - Writes matched lines to an output file for easy review.
   - Optionally prints matches to the console.
- Main Execution: Calls parse_logs() if the script is run directly, allowing it to be reused in other scripts if imported.
