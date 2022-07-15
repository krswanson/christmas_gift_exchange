import smtplib, ssl
import copy
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from create_matches import get_json_file
from create_messages import *

year = input("Which Christmas year is this for? ")
try:
	matches = get_json_file("matches_" + year + ".json")
except FileNotFoundError:
	print("No data file found for", year)
	print("Use save_matches.py to create one")
	exit(0)
emails = get_json_file("emails.json")

group = input("Who do you want to send to? (all/[first names]): ")
group = group.split()
password = input("Type your password and press enter: ")

sender_email = "taber.christmas.gift.exchange@gmail.com"  # Enter your address
messages = []
for name in matches.keys():
	# Only create email for desired group of people
	if "all" not in group and name not in group:
		continue
	match = matches[name]
	receiver_email = emails[name] # "kristin.l.swanson@att.net"

	message = MIMEMultipart("alternative")
	message["Subject"] = "Your person for Christmas " + year
	message["From"] = "Christmas Gift Exchange <" + sender_email + ">"

	# Create the plain-text and HTML version of your message
	text, html = match_messages(name, match)
	#text, html = test_messages(name)

	# Turn these into plain/html MIMEText objects
	part1 = MIMEText(text, "plain")
	part2 = MIMEText(html, "html")

	# Add HTML/plain-text parts to MIMEMultipart message
	# The email client will try to render the last part first
	message.attach(part1)
	message.attach(part2)

	# Send to multiple places for same person if needed
	if type(receiver_email) is list:
		for email in receiver_email:
			m_copy = copy.deepcopy(message)
			m_copy["To"] = email
			messages.append(m_copy)
	else:
		message["To"] = receiver_email
		messages.append(message)

port = 465  # For SSL
smtp_server = "smtp.gmail.com"

# Create secure connection with server and send email
context = ssl.create_default_context()
print("\n This may take a few moments...\n")
with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
	server.login(sender_email, password)
	for message in messages:
		receiver_email = message["To"]
		server.sendmail(
			sender_email, receiver_email, message.as_string()
		)
		print(" Message sent to", receiver_email)
print("\n", len(messages), "message(s) sent")