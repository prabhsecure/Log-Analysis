# SOC Log Analyzer

Beginner-friendly SOC project that analyzes logs and detects brute force attacks.

## Features

- Detect multiple failed login attempts
- Generate JSON alerts
- Real-time log monitoring
- Suspicious country detection
- Email alert system
- MITRE ATT&CK mapping
- Windows Event Log parsing

## Requirements

pip install watchdog
pip install geoip2
pip install pywin32

## Run

python log_analyzer.py

## Project Structure

SOC-Log-Analyzer
│
├── log_analyzer.py
├── realtime_monitor.py
├── geoip_checker.py
├── email_alerts.py
├── windows_event_parser.py
├── sample_logs.txt
├── alerts.json
└── README.md