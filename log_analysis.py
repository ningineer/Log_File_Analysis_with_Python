import re
from datetime import datetime

# Specify input and output files
log_file_path = "example_log.txt"  # Input log file
output_file_path = f"filtered_log_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"  # Timestamped output file

def parse_logs(log_file_path, output_file_path):
    """Parse the log file and filter for specific keywords."""
    keywords = ["ERROR", "WARNING"]  # Keywords to search for in the log file
    pattern = re.compile('|'.join(keywords))  # Compile pattern for faster matching

    with open(log_file_path, 'r') as log_file, open(output_file_path, 'w') as output_file:
        for line in log_file:
            if pattern.search(line):  # Check if line contains any keyword
                output_file.write(line)  # Write matched line to output file
                print(f"Match found: {line.strip()}")  # Print matched line to console (optional)

    print(f"\nFiltered log saved to: {output_file_path}")

if __name__ == "__main__":
    parse_logs(log_file_path, output_file_path)
