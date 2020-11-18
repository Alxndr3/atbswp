import ezsheets


ss = ezsheets.Spreadsheet('1jDZEdvSIh4TmZxccyy0ZXrH-ELlrwq8_YYiZrEOB4jg')

for x in range(2, len(ss[0].getColumn(1))):
    if ss[0].getRow(x)[0] == '':
        print("Done!")
        break
    if int(ss[0].getRow(x)[0]) * int(ss[0].getRow(x)[1]) == int(ss[0].getRow(x)[2]):
       pass
    else:
        print(x)

