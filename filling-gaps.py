#!/bin/env python3
# filling-gaps.py - Finds all files with a given prefix, such as
# spam001.txt , spam002.txt , and so on, in a single folder and
# locates any gaps in the numbering (such as if there is a
# spam001.txt and spam003.txt but no spam002.txt ).
from sys import argv
import os
import re
import shutil


# Check if num of params is the number necessary.
if len(argv) < 1:
    print('Folder to check files.')
else:
    directory = '/home/alexandre/PycharmProjects/atbswp/delicious'
    os.chdir(directory)
    prefix = re.compile(r'(bacon)(\d\d\d)(.txt)?')
    # List files in folder with the given prefix.
    file_list = list()
    # Create a list of all files that contains the prefix
    for files in os.listdir(directory):
        if prefix.findall(files):
            file_list.append(files)
            file_list.sort()

    previous_file = file_list[0]
    previous_file = int(prefix.findall(previous_file)[0][1]) - 1
    # Loop through the list of files to be checked
    for file in file_list:
        extension = prefix.findall((file))
        # Keep track if the current file is no a gap in relation to the previous one
        if previous_file + 1 < int(prefix.findall(file)[0][1]):
            new_num = prefix.findall(file)[0]
            new_name = new_num[0]
            len_num = len(new_num[1])
            new_name = list()
            new_name.append(new_num[0])
            new_name.append(previous_file + 1)
            new_str = str()
            # zfill allows to fill the string with zeros
            # New name to the file
            new_str = new_name[0] + str(new_name[1]).zfill(len_num) + extension[0][2]
            # Rename the current file to the name of the gaping file
#            print(f'Renaming {file} to {new_str}')
#            shutil.move(file, new_str)
            # If you want to create a new file in the gaping one rather renaming the leading one comment the
            # two previous lines and uncomment the two next ones
            shutil.move(directory, new_str)
        previous_file += 1
