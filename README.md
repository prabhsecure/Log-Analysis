# SOC Log Analyzer

A Python-based SOC tool that analyzes system logs and detects suspicious login activity such as  brute-force attacks and multiple failed login attempts.

This project demonstrates log analysis, threat detection, and SOC automation, which are common tasks performed by Security Operations Center (SOC) analysts.

## Features

- Detect multiple failed login attempts
- Generate JSON alerts
- Real-time log monitoring
- Suspicious country detection
- Email alert system
- MITRE ATT&CK mapping
- Windows Event Log parsing
## create Environment
python -m venv/venv

source venv/bin/activate


## Requirements

pip install watchdog

pip install geoip2


## Run

python log_analyzer.py

## Project Structure

SOC-Log-Analyzer
│
├── log_analyzer.py
├── geoip_checker.py
├── email_alerts.py
├── sample_logs.txt
├── alerts.json
└── README.md
