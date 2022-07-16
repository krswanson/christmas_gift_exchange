from EmailSender import EmailSender

sender = EmailSender("settings.json")
group = sender.input_group()
messages = sender.create_messages(group)
sender.send_messages(messages)
