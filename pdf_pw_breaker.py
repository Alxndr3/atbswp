#!/usr/bin/env python3
import PyPDF2
import sys


if len(sys.argv) < 3:
    print("Insert file path and dictionary path as arguments.")
else:
    with open(sys.argv[2], 'r') as dictionary:
        pdf_reader = PyPDF2.PdfFileReader(open(sys.argv[1], 'rb'))
        for word in dictionary.readlines():
            if pdf_reader.decrypt(word.rstrip('\n')) == 1:
                print('Pass found')
                print(word)
                break
            if pdf_reader.decrypt(word.lower().rstrip('\n')) == 1:
                print('Pass found')
                print(word.lower())
                break
            else:
                pass

