
# alert_system.py

import logging
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Configure logging
logging.basicConfig(filename='/mnt/data/TIGTA_Automation_Suite/ReportingTools/Logs/alert.log',
                    level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')

def send_alert(recipient_email, subject, message):
    """
    Sends an email alert to the specified recipient.
    Args:
        recipient_email (str): The email address of the recipient.
        subject (str): The subject of the email.
        message (str): The body of the email.
    Returns:
        bool: True if the email is sent successfully, False otherwise.
    """
    try:
        # Email configuration
        sender_email = "your_email@example.com"
        sender_password = "your_password"

        # Create the email
        msg = MIMEMultipart()
        msg['From'] = sender_email
        msg['To'] = recipient_email
        msg['Subject'] = subject
        msg.attach(MIMEText(message, 'plain'))

        # Send the email
        server = smtplib.SMTP('smtp.example.com', 587)
        server.starttls()
        server.login(sender_email, sender_password)
        server.send_message(msg)
        server.quit()

        logging.info(f"Alert sent to {recipient_email} with subject: {subject}")
        print(f"Alert sent to {recipient_email} with subject: {subject}")
        return True

    except Exception as e:
        logging.error(f"Error in sending alert: {e}")
        print(f"Error: {e}")
        return False

# Example usage
if __name__ == "__main__":
    send_alert("recipient@example.com", "Urgent: Compliance Issue", 
               "A compliance issue has been detected and requires immediate attention.")
