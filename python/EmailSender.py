import smtplib, ssl
import copy
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from create_matches import get_json_file
from create_messages import *

class EmailSender():
	def __init__(self, settings_file):
		settings = get_json_file(settings_file)
		self.year = settings["year"]
		self.message_type = settings["message_type"]
		self.sender_email = settings["sender"]
		self.password = settings["password"]
		self.emails = get_json_file(settings['contacts_file'])

		try:
			self.matches = get_json_file("matches_" + self.year + ".json")
		except FileNotFoundError:
			print("No data file found for", self.year)
			print("Use save_matches.py to create one")
			exit(1)

	def input_group(self):
		print("\nPreparing to send", self.message_type, "messages for Christmas", self.year)
		group = input("Who do you want to send to? (all/[names separted by commas]): ")
		return [name.strip() for name in group.split(',')]

	def create_messages(self, group):
		messages = []
		for name in self.matches.keys():
			# Only create email for desired group of people
			if "all" not in group and name not in group:
				continue
			match = self.matches[name]
			receiver_email = self.emails[name]

			message = MIMEMultipart("alternative")
			message["Subject"] = "Your person for Christmas " + self.year
			message["From"] = "Christmas Gift Exchange <" + self.sender_email + ">"

			# Create the plain-text and HTML version of your message
			text, html = create_messages(self.message_type, name, match)

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
		return messages
		
	def send_messages(self, messages):
		port = 465  # For SSL
		smtp_server = "smtp.gmail.com"

		# Create secure connection with server and send email
		context = ssl.create_default_context()
		print("\n This may take a few moments...\n")
		with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
			server.login(self.sender_email, self.password)
			for message in messages:
				receiver_email = message["To"]
				server.sendmail(
					self.sender_email, receiver_email, message.as_string()
				)
				print(" Message sent to", receiver_email)
		print("\n", len(messages), "message(s) sent")