#! /usr/bin/env python3
# chore_assigment_emailer.py - Assigns randomily chores to people and sends
# emails awarening them on threi duties.

import smtplib
from os import environ
from random import choice


# Log in to email account.
EMAIL_ADDRESS = environ.get("EMAIL_ADDRESS")
EMAIL_PASS = environ.get("EMAIL_PASS")
smtp_obj = smtplib.SMTP('smtp.gmail.com', 587)
smtp_obj.ehlo()
smtp_obj.starttls()
smtp_obj.login(EMAIL_ADDRESS, EMAIL_PASS)

chores = ['dishes', 'bathrom', 'vacuum', 'walk dog']
people = {'Alice': 'alice@example.com', 'Bob': 'bob@example.com', 'Eve':
        'eve@example.com', 'Alexandre': 'alxndr3@gmail.com'}

for name, email  in people.items():
    random_chore = choice(chores)
    chores.remove(random_chore)

    body = f'Subject: Duty of the day\nHi {name} your chore today is {random_chore}'

    print(f'Sending email to {name}:\n{body}') 
    sendmail_status = smtp_obj.sendmail(EMAIL_ADDRESS, email, body)

    if sendmail_status != {}:
        print('There was a problem sending email to %s: %s' % (email, sendmail_status))

