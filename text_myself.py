#! /usr/bin/bash python3
# text_myself.py - Defines the textmyself() function that texts a message
# passed to it as a string.

from os import environ
from twilio.rest import Client

# Presset values:
account_sid = environ.get("TWILIO_SID")
account_token = environ.get("TWILIO_TOKEN")
my_number = "+5541996459349"
twilio_number = "+19204826002"

def text_myself(message):
    twilio_cli = Client(account_sid, account_token)
    twilio_cli.messages.create(body=message, from_=twilio_number, to=my_number)

