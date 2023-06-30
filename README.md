# Christmas Gift Exchange

An app in development for my family's yearly secret Santa random drawing.  It will create the matches and send emails/texts with people's Christmas matches, possibility of adding a website too. 

## Setting up settings.json

This is where you set the specifics of your situation, for simplicity, all values are strings.

**year** - the year you are generating matches for

**years_back** - the number of years back you want to exclude previous matches (0 if no previous years)

**message_type** - options are: "match", "reminder", and "test"

**sender** - the email address you want to send from

**password** - the sender email password (or app password, see Sending emails below)

**relationships_file** - the name of the json file with the keys being the names of the people to include in the drawing, with the values being a list of people they should not be matched with (which can be an empty list)

**contacts_file** - name of the json file with the keys being the names of the people and the values being either a string or list of strings of their email or text message addresses (see Sending emails/texts for more details)

## Generating matches

```sh
cd python
python save_matches.py
````
Using the year and other information from the settings.json file, it will generate new matches based on any previous years' data and the exceptions in the relationships_file and save it to a new .json file.  If your years_back is greater than 0, be sure to have appropriate matches_yyyy.json files for each previous year.

## Sending emails/texts

Use your contacts_file to store the email addresses (or phone numbers with carrier domains, see: https://dev.to/mraza007/sending-sms-using-python-jkd ) to use for each person.

Set the settings.json file with your information, 
choosing "test", "match", or "reminder" for the message_type

The password when sending from a gmail acount should be an app password, to generate and use an app password you need 2 step verification on, then go to:
Manage your Google accout > Security > 2-Step-Verification > App Passwords

When ready to send the batch of emails, do:

```sh
python send_emails.py
```

When prompted, either type simply `all`, or to send to one or more specific people, type each name, sparated by commas.



## Website install

```sh
cd christmas_gift_exchange
npm install
npm run build
npm start
```
Then go to: http://localhost:4005/

### Development

```sh
npm install
npm run devStart
```

To stop, in addition to doing ctrl-c on the process, run:
```sh
npm run devStop
```
to stop the server.
