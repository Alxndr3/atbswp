import re


def strip_like(string, separator):
    strip_regex = re.compile(rf'[a-zA-Z]+')
    new_string = str()
    print(strip_regex.findall(string))
    for x in strip_regex.findall(string):
        new_string += x + separator
    print(new_string)

strip_like('alexandre  cardoso ', '-')
