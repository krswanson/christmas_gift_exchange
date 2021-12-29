# Christmas Gift Exchange

An app in development for my family's yearly secret Santa random drawing.  It will create the matches and send emails/texts with people's Christmas matches, possibility of adding a website too. 

## Generating matches

```sh
cd python
python save_matches.py
````
When prompted, enter the year it is for (currently, you need a previous year file for it to work such as matches_2021.json).  It will generate new matches based on the previous year's data and the exceptions in Relationships.json and save it to a new .json file.

## Sending emails/texts

Use the emails.json file to store the email addresses (or phone numbers with carrier domains, see: https://dev.to/mraza007/sending-sms-using-python-jkd ) to use for each person.

When ready to send the batch of emails, do:

```sh
python send_emails.py
```
Again, entering the current year (corresponding to the match file) to use.

You will also need to input the password for the sender email; for sending from a gmail account, generate and use an app password:
https://support.google.com/accounts/answer/185833


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
