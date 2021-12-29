import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from create_matches import get_json_file

year = input("Which Christmas year is this for? ")
try:
	matches = get_json_file("matches_" + year + ".json")
except FileNotFoundError:
	print("No data file found for", year)
	print("Use save_matches.py to create one")
	exit(0)
emails = get_json_file("emails.json")

password = input("Type your password and press enter: ")
sender_email = "krswanson95008@gmail.com"  # Enter your address
messages = []
for name in matches.keys():
	match = matches[name]
	receiver_email = "4085687250@vtext.com" #emails[name] # "kristin.l.swanson@att.net"
	
	message = MIMEMultipart("alternative")
	message["Subject"] = "Your person for Christmas " + year
	message["From"] = "Christmas Gift Exchange <" + sender_email + ">"
	message["To"] = receiver_email

	# Create the plain-text and HTML version of your message
	text = """\
Hello {0},

This year you will be buying for: {1}
""".format(name, match)
	html = """\
	<html>
	  <body>
	    <p>Hello {0},<br>
	       This year you will be buying for: {1}<br>
	    </p>
	  </body>
	</html>
	""".format(name, match)
	
	# Turn these into plain/html MIMEText objects
	part1 = MIMEText(text, "plain")
	part2 = MIMEText(html, "html")

	# Add HTML/plain-text parts to MIMEMultipart message
	# The email client will try to render the last part first
	message.attach(part1)
	message.attach(part2)
	messages.append(message)

port = 465  # For SSL
smtp_server = "smtp.gmail.com"

# Create secure connection with server and send email
context = ssl.create_default_context()
with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
	server.login(sender_email, password)
	for message in messages:
		receiver_email = message["To"]
		server.sendmail(
			sender_email, receiver_email, message.as_string()
		)
		print("Email sent to", receiver_email)
		break