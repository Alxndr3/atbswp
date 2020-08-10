import re


def password_detector():
    while True:
        password = input('Insert Password: ')
        if len(password) < 9:
            print('Password needs to be greater than 8 character')
            continue
        pw_regex_1 = re.compile(r'([A-Z])+')
        pw_regex_2 = re.compile(r'([a-z])+')
        pw_regex_3 = re.compile(r'([0-9]|\w)+')
        res1 = pw_regex_1.search(password)
        res2 = pw_regex_2.search(password)
        res3 = pw_regex_3.search(password)
        if res1 is None or res2 is None or res3 is None:
            print('Password needs to have uppercase, lowercase characters and numbers.')
            continue
        else:
            print('Password accepted')
        break


password_detector()
