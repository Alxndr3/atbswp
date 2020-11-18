#! /usr/bin/env python3
import ezsheets
import os
from sys import argv


if len(argv) < 2:
    print("""Type the name of the spread sheet you'd like to upload and convert as an argument.""")
else:
    if argv[1] not in os.listdir():
        print('File not found.')
    else:
        print('Uploading file...')
        ezsheets.upload(argv[1])
        print('Downloading s% as CSV' % (argv[1]))
        file_ = str(argv[1].split('.')[0])
        ss = ezsheets.Spreadsheet(file_)
        ss.downloadAsCSV()
        print('Downloading s% as PDF' % (argv[1]))
        ss.downloadAsPDF()
        print('Downloading s% as HTML' % (argv[1]))
        ss.downloadAsHTML()
