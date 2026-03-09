import re
import json
from collections import defaultdict
from geoip_checker import check_country
from email_alerts import send_alert

log_file = "sample_logs.txt"
alert_file = "alerts.json"

failed_logins = defaultdict(int)
alerts = []

# Regex to extract IP address
ip_pattern = r'\b(?:[0-9]{1,3}\.){3}[0-9]{1,3}\b'

# Read log file
with open(log_file, "r") as file:
    logs = file.readlines()

# Scan logs for failed logins
for line in logs:

    if "Failed password" in line:

        ip_match = re.search(ip_pattern, line)

        if ip_match:
            ip = ip_match.group()
            failed_logins[ip] += 1

            # Check country of IP
            try:
                check_country(ip)
            except:
                pass


# Detect brute force attempts
for ip, count in failed_logins.items():

    if count >= 3:

        alert = {
            "type": "Brute Force Attempt",
            "ip_address": ip,
            "failed_attempts": count,
            "severity": "High",
            "mitre_technique": "T1110"
        }

        alerts.append(alert)

        # Print attack in terminal
        print(f"[ALERT] Brute force detected from IP: {ip} ({count} failed attempts)")

        # Send email alert
        try:
            send_alert(f"Brute force attack detected from IP: {ip} ({count} failed attempts)")
        except:
            pass


# Save alerts to JSON
with open(alert_file, "w") as file:
    json.dump(alerts, file, indent=4)


print("\nLog Analysis Complete By https://github.com/prabhsecure.")
print("Total Alerts Generated:", len(alerts))