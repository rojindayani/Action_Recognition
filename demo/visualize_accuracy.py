import matplotlib.pyplot as plt
from datetime import datetime
import re

# Read log data from a file (replace 'log_file.txt' with your log file path)
log_data = []
with open('log_file.txt', 'r') as file:
    log_data = file.readlines()

# Extract the relevant data (time and top1_acc)
timestamps = []
top1_acc_values = []

for log_entry in log_data:
    match = re.search(r'top1_acc: ([0-9.]+),', log_entry)
    if match:
        top1_acc = float(match.group(1))
        parts = log_entry.split()
        timestamp = datetime.strptime(parts[0] + ' ' + parts[1], '%Y-%m-%d %H:%M:%S,%f')
        timestamps.append(timestamp)
        top1_acc_values.append(top1_acc)

# Create a line chart
plt.figure(figsize=(12, 6))
plt.plot(timestamps, top1_acc_values, marker='o', linestyle='-')
plt.title('Top-1 Accuracy Over Time')
plt.xlabel('Time')
plt.ylabel('Top-1 Accuracy')
plt.grid(True)

# Format x-axis for better readability (optional)
plt.gcf().autofmt_xdate()

# Show the plot
plt.tight_layout()
plt.show()
