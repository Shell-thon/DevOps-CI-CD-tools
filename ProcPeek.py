import smtplib
from email.message import EmailMessage

def send_email(body):
    msg = EmailMessage()
    msg.set_content(body)
    msg["Subject"] = "Cron Job Output"
    msg["From"] = "you@example.com"
    msg["To"] = "you@example.com"

    with smtplib.SMTP("localhost") as s:
        s.send_message(msg)

send_email("✅ Backup complete at 3AM.")
