import re
from datetime import datetime
from db_connect import insert_alert

def parse_snort_alerts(log_file_path):
    with open(log_file_path, 'r') as file:
        lines = file.readlines()

    for i in range(len(lines)):
        line = lines[i]
        if "[**]" in line and "Priority:" in line:
            try:
                # Extract alert message
                message = re.search(r'\[.*?\] (.*?) \[Priority', line).group(1).strip()

                # Extract timestamp from previous line
                timestamp_line = lines[i - 1]
                timestamp_str = timestamp_line.strip().split()[0]  # e.g., "03/23-22:15:34.990251"
                timestamp = datetime.strptime(timestamp_str, "%m/%d-%H:%M:%S.%f")
                timestamp = timestamp.replace(year=datetime.now().year)

                # Extract IP addresses from the next line
                ip_line = lines[i + 1]
                src_ip, dest_ip = re.findall(r'(\d+\.\d+\.\d+\.\d+)', ip_line)

                # Insert into DB
                insert_alert(timestamp, src_ip, dest_ip, message)

            except Exception as e:
                print("⚠️ Failed to parse alert:", e)
