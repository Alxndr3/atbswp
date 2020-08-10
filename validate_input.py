while True:
    print('Enter your age:')
    age = input()
    if age.isdecimal():
        break
    print('Please enter a number for your age.')
while True:
    password = input('Select a new password (letters and number only):')
    if password.isalnum():
        break
    print('Passwords can only have letter and numbers')


