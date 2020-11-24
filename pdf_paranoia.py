#!/usr/bin/env python3
# pdf_paranoia.py - Access a directory and all it's subdirectories searching
# for pdf files and encrypts them.
import os
import PyPDF2
import sys
from time import sleep

if len(sys.argv) < 3:
    print('Insert a password for pdf encryption and the path to directory to be searched')
else:
    for folder_name, subfolders, filenames in os.walk(sys.argv[2]):
        for filename in filenames:
            if filename.endswith('.pdf'):
                with open(folder_name + '/' + filename, 'rb') as pdf_file:
                    pdf_reader = PyPDF2.PdfFileReader(pdf_file)
                    pdf_writer = PyPDF2.PdfFileWriter()
                    for page_num in range(pdf_reader.numPages):
                        pdf_writer.addPage(pdf_reader.getPage(page_num))
                    pdf_writer.encrypt(sys.argv[1])
                    with open(folder_name + '/' + filename + '_encrypted.pdf', 'wb') as result_pdf:
                        pdf_writer.write(result_pdf)


                try:
                    with open(filename + '_encrypted.pdf', 'rb') as pdf_file_r:
                        pdf_reader_r = PyPDF2.PdfFileReader(pdf_file_r)
                        if pdf_reader_r.isEncrypted:
                            pdf_reader_r.decrypt(sys.argv[1])
                            pdf_obj = pdf_reader_r.getPage(0)
                except:
                    print('It has failed!')
                else:
                    #os.remove(folder_name + '/' + filename)
                    print(f"Deleting...{folder_name + '/' + filename}")
