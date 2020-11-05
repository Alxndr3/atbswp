#! /bin/env python3
import openpyxl
import sys


if len(sys.argv) < 4:
    print("You should insert three argumens")
else:
    n = int(sys.argv[1])
    m = int(sys.argv[2])
    xl_file = sys.argv[3]

    wb = openpyxl.load_workbook(xl_file)
    sheet = wb.active

    for r in range(m):
        sheet.insert_rows(n)

    wb.save('new_' + xl_file) 
