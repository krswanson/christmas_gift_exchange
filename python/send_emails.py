import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

#port = 465  # For SSL
#smtp_server = "smtp.gmail.com"
sender_email = "krswanson95008@gmail.com"  # Enter your address
receiver_email = "kristin.l.swanson@att.net"  # Enter receiver address
password = input("Type your password and press enter: ")

message = MIMEMultipart("alternative")
message["Subject"] = "Test"
message["From"] = "Christmas Gift Exchange <" + sender_email + ">"
message["To"] = receiver_email

# Create the plain-text and HTML version of your message
text = """\
Hi,
This is plain text
"""
html = """\
<html>
  <body>
    <p>Hi,<br>
       How are you?<br>
       This is html
    </p>
  </body>
</html>
"""

# Turn these into plain/html MIMEText objects
part1 = MIMEText(text, "plain")
part2 = MIMEText(html, "html")

# Add HTML/plain-text parts to MIMEMultipart message
# The email client will try to render the last part first
message.attach(part1)
message.attach(part2)

# Create secure connection with server and send email
context = ssl.create_default_context()
with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
    server.login(sender_email, password)
    server.sendmail(
        sender_email, receiver_email, message.as_string()
    )