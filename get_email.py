import ezsheets


ss = ezsheets.Spreadsheet('Name_Email')
sheet = ss[0]
for x in sheet.getColumn(3):
    if x != '':
        print(x)
