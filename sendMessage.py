import os
from twilio.rest import Client

ACCOUNT_SID = os.environ.get('ACCOUNT_SID')
AUTH_TOKEN = os.environ.get('AUTH_TOKEN')
FROM = os.environ.get('FROM')

client = Client(ACCOUNT_SID, AUTH_TOKEN)

def sendMessage(senderId, message):
    
    res1 = client.messages.create(
           body="Your message is : " + message,
           from_=FROM,
           to=f'whatsapp:+{senderId}'
       )