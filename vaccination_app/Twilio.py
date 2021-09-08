import os
#install twilio package:
from twilio.rest import Client

# Find these values at https://twilio.com/user/account
# To set up environmental variables, see http://twil.io/secure
account_sid = os.environ['TWILIO_ACCOUNT_SID']
auth_token = os.environ['TWILIO_AUTH_TOKEN']

client = Client(account_sid, auth_token)

client.api.account.messages.create(
    to="+12316851234", # your number
    from_="+18722405726", # My Twilio Account Number
    body="Hello there!")