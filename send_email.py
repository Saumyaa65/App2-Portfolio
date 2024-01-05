import os
import smtplib, ssl

def send_email(subject, raw_message, user_email):
    host="smtp.gmail.com"
    port=465

    username="keepstudying65@gmail.com"
    password= os.getenv("PASSWORD")

    receiver="saumyaagarwal65@gmail.com"
    context=ssl.create_default_context()
    message=f"""\
Subject: {subject}
From: {user_email}
{raw_message}
"""

    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(username, password)
        server.sendmail(username,receiver,message)