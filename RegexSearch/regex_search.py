# regex_search.py - open all .txt files in a directory and searches any line that matches a user-supplied regex
import re
import os


count_line = 0
regex_found = list()
# Insert directory to be searched and change to it, insert regex to be found and
path_file = str(input('Insert absolute path file: '))
regex_search = str(input('Insert your regex: '))
regex = re.compile(rf'(.)*{regex_search}(.)*')
os.chdir(path_file)
# List, open, read each line of each file from current directory and check if regex is present
for files in os.listdir():
    print(files)
    with open(files) as open_file:
        for line in open_file.readlines():
            count_line += 1
            if regex.search(line):
                print('String found in line %d' % count_line)
    open_file.close()
    count_line = 0
