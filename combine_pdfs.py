#!/usr/bin/env python3
# combine_pdfs.py - Combines all de PDFs in the current working directory into a single PDF.

import os
import PyPDF2


# Get all the PDF filenames.
pdf_files = list()
for filename in os.listdir('.'):
    if filename.endswith('.pdf'):
        pdf_files.append(filename)

pdf_files.sort(key = str.lower)

pdf_writer = PyPDF2.PdfFileWriter()

# Loop through all the PDF files.
for file_ in pdf_files:
    pdf_file = open(file_, 'rb')
    pdf_reader = PyPDF2.PdfFileReader(pdf_file)
    # Loop through all the pages (exept the first) and add them.
    for page_num in range(1, pdf_reader.numPages):
        page_obj = pdf_reader.getPage(page_num)
        pdf_writer.addPage(page_obj)
# Save the resulting PDF to a file.
pdf_output_file = open('new_merged_pdf.pdf', 'wb')
pdf_writer.write(pdf_output_file)

pdf_file.close()
pdf_output_file.close()
