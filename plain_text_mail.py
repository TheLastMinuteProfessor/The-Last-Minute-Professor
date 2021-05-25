"""
For Code Explanation, visit https://youtu.be/7ZSSTyse8FI
"""
import getpass, smtplib, ssl
sender_email = "thelastminuteprofessor@gmail.com"
receiver_email = "thelastminuteprofessor@gmail.com" 
password = getpass.getpass(prompt='Password for Mail-ID: ')
message = """Subject: Mail Sent from Python
Having a time of Happy Learning with the Last Minute Professor."""
with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=ssl.create_default_context()) as server:
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email, message)
    
