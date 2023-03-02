import smtplib
import imghdr
from email.message import EmailMessage
import os

password = os.environ.get("PASSWORD")
sender_mail = "saurabhpython1@gmail.com"
receiver_mail = "saurabhpython1@gmail.com"


def send_email(image_path):
    email_message = EmailMessage()
    email_message["Subject"] = "Movement Detected"
    email_message.set_content("Someone was caught on cam!")

    with open(image_path, "rb") as file:
        content = file.read()
    email_message.add_attachment(content, maintype="image", subtype=imghdr.what(None, content))

    gmail = smtplib.SMTP("smtp.google.com", 587)
    gmail.ehlo()
    gmail.starttls()
    gmail.login(sender_mail, password)
    gmail.sendmail(sender_mail, receiver_mail, email_message.as_string())
    gmail.quit()
