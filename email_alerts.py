import smtplib
from email.mime.text import MIMEText

def send_alert(message):

    sender = "youremail@gmail.com"
    receiver = "socalerts@gmail.com"
    password = "your_app_password"

    msg = MIMEText(message)
    msg['Subject'] = "SOC Alert: Suspicious Activity Detected"
    msg['From'] = sender
    msg['To'] = receiver

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
        server.login(sender, password)
        server.sendmail(sender, receiver, msg.as_string())