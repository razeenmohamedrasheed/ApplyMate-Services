import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from src.config.constants import SENDER_EMAIL

class GenerateMail:
    app_password = " "
    
    @staticmethod
    def send_email(receiver_email: str):
        subject = "Registration Success"
        body = """\
            Hi there,

            We're excited to let you know that your account has been successfully created!

            Thank you for joining us — we're thrilled to have you on board. You can now log in and start exploring all the features and benefits available to you.

            If you have any questions or need assistance, feel free to reach out to our support team at any time.

            Welcome aboard!

            Best regards,  
            Team ApplyMate
            """
        # Create the email message
        msg = MIMEMultipart()
        msg["From"] = SENDER_EMAIL
        msg["To"] = receiver_email
        msg["Subject"] = subject

        msg.attach(MIMEText(body, "plain"))

        try:
            with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
                server.login(SENDER_EMAIL, GenerateMail.app_password)
                server.sendmail(SENDER_EMAIL, receiver_email, msg.as_string())
                print("success")
        except Exception as e:
            print(e)



