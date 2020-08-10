import re


def split_like(string, separator):
    new_string = list()
    z = str()
    str_regex = re.compile(fr'(\w+)({separator})')
    foo = str_regex.findall(string)
    for x in foo:
        for i in x:
            if i != separator:
                z += i
        new_string.append(z)
        z = ''
    print(foo)
    print(new_string)


split_like('bla-ble-bli-blow', '-')

