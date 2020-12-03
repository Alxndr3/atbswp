#!/usr/bin/bash python3
# pdf_decryptor.py - Access a directory and its subdirectories searching for
# encrypted pdf then asks for its password and saves it in a new directory.
import os
import PyPDF2


dir_to_search = '.'
for dir_path, dir_list, file_names in os.walk(dir_to_search):
    for file_name in file_names:
        if file_name.endswith('.pdf'):
            with open(os.path.join(dir_path, file_name), 'rb') as pdf_file:
                pdf_reader = PyPDF2.PdfFileReader(pdf_file)
                if pdf_reader.isEncrypted:
                    pdf_pass = str(input(f"Type password for {file_name}: "))
                    try:
                        pdf_reader.decrypt(pdf_pass)
                        pdf_writer = PyPDF2.PdfFileWriter()
                        for page_num in range(pdf_reader.numPages):
                            page_obj = pdf_reader.getPage(page_num)
                            pdf_writer.addPage(page_obj)

                        with open(f'{os.path.join(".")}, decrypted_{file_name}', 'wb') as decrypted_pdf:
                            pdf_writer.write(decrypted_pdf)
                            print('to aqui')
                    except:
                        print("Password didn't match!")
                        continue

