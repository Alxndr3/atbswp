import re


def password_detector():
    while True:
        password = input('Insert Password: ')
        if len(password) < 8:
            print('Password needs to be greater than 8 character')
            continue
        pw_regex_1 = re.compile(r'([A-Z]+[a-z]+([0-9]|\W)+)|'
                                r'([A-Z]+([0-9]|\W)+[a-z]+)|'
                                r'([a-z]+[A-Z]+([0-9]|\W)+)|'
                                r'([a-z]+([0-9]|\W)+[A-Z]+)|'
                                r'(([0-9]|\W)+[a-z]+[A-Z]+)|'
                                r'(([0-9]|\W)+[A-Z]+[a-z]+)')
        res = pw_regex_1.search(password)
        if res is None:
            print('Password needs to have uppercase, lowercase characters and numbers.')
            continue
        else:
            print('Password accepted')
        break


password_detector()
