import re
password = input("Enter string to test: ")
if re.match(r'[A-Za-z0-9@#$%^&+=]{8,}', password):
    print('Match')
else:
    print('No match')
