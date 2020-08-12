#! python3
# backup_to_zip1.py - Copies an entire folder and its contents into a zip file whose filename increments
import re
import os
import zipfile


def backupToZip(folder):
   bak_num = 0
   zip_file = folder.split('/')[-1]
   zipfile_pattern = re.compile(rf'({zip_file})(\d)?(\.zip)')
   for filename in os.listdir(f'{folder}/..'):
       if zipfile_pattern.search(filename):
           if int(zipfile_pattern.findall(filename)[0][1]) > bak_num:
                bak_num = int(zipfile_pattern.findall(filename)[0][1])
           print(bak_num)
       else:
           continue
   with zipfile.ZipFile(f'{zip_file}{bak_num + 1}.zip', 'w') as folder_bak:
       folder_bak.write(folder, compress_type=zipfile.ZIP_DEFLATED)

#backupToZip(str(input('Folder path: ')))
backupToZip('/home/alexandre/PycharmProjects/atbswp/delicious')


