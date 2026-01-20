import smtplib
from email.message import EmailMessage
import os

# ==============================
# CONFIGURATION
# ==============================
SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 465

SENDER_EMAIL = os.getenv("SENDER_EMAIL")
SENDER_PASSWORD = os.getenv("SENDER_PASSWORD")
RECEIVER_EMAIL = os.getenv("RECEIVER_EMAIL")

# ==============================
# CREATE EMAIL
# ==============================
msg = EmailMessage()
msg["Subject"] = "Daily Python Reminder"
msg["From"] = SENDER_EMAIL
msg["To"] = RECEIVER_EMAIL

msg.set_content(
    """
Hi,

This is an automated email sent using Python.

Your SMTP automation is working perfectly

Keep building cool automations

— Python Automation Bot
"""
)

# ==============================
# SEND EMAIL
# ==============================
try:
    print("Connecting to SMTP server...")
    with smtplib.SMTP_SSL(SMTP_SERVER, SMTP_PORT) as server:
        print("Authenticating credentials...")
        server.login(SENDER_EMAIL, SENDER_PASSWORD)

        print("Sending email...")
        server.send_message(msg)

    print("Email sent successfully ✔")

except Exception as e:
    print("Error occurred:", e)
