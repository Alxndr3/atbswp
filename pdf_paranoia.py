#!/usr/bin/env python3
# pdf_paranoia.py - Access a directory and all it's subdirectories searching
# for pdf files and encrypts them.
import os
import PyPDF2
import sys

if len(sys.argv) < 3:
    print('Insert a password for pdf encryption and the path to directory to be searched')
else:
    print(sys.argv[1])
    print(sys.argv[2])
    try:
        for folder_name, subfolders, filenames in os.walk(sys.argv[2]):
            print(sys.argv[2])
            for filename in filenames:
                if filename.endswith('.pdf'):
                    print(filename)
                    with open(filename, 'rb') as pdf_file:
                        pdf_reader = PyPDF2.PdfFileReader(pdf_file)
                        pdf_writer = PyPDF2.PdfFileWriter()
                        for page_num in range(pdf_reader.numPages):
                            pdf_writer.addPage(pdf_reader.getPage(page_num))

                        pdf_writer.encrypt(sys.argv[1])
                        with open(filename + '_encrypted.pdf', 'wb') as result_pdf:
                            pdf_writer.write(result_pdf)

    except FileNotFoundError:
        print(filename + ' is already encrypted.')
        sys.exit()
