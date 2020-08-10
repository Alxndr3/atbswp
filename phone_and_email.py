#! python3
# phone_and_email.py - Finds phone numbers and email addresses on the clipboard.
import pyperclip
import re

phone_regex = re.compile(r'''(
    (\(?(\d)?\d\d\)?)?    # area code
    (\s|-|\.)?       # separtor
    (\d?\d{4})       # first 4 digits if celphone first 3 if not
    (\s|-|\.)?       # separtor
    (\d{4})          # last 4 digits 
    )''', re.VERBOSE)

email_regex = re.compile(r'''(
    (\S+@\S+)           # user_name + @ + domain_name
    (\.\w?\w?\w\w){1,2} # .com or .br or whatever
    )''', re.VERBOSE)

# TODO: Find matches in clipboard text.
clip = pyperclip.paste()
found_phones = phone_regex.findall(clip)
all_results = []
for phones in found_phones:
    print(phones[0])
    all_results.append(phones[0])
if not found_phones:
    print('No phone number found.')
found_emails = email_regex.findall(clip)
for emails in found_emails:
    print(emails[0])
    all_results.append(emails[0])
if not found_emails:
    print('No email address found')

# TODO: Copy results to the clipboard.
pyperclip.copy(str(all_results))

