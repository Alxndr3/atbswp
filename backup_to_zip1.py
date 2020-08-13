#! python3
# backup_to_zip1.py - Copies an entire folder and its contents into a zip file whose filename increments
import re
import os
import zipfile


def backupToZip(folder):
   bak_num = 0
   zip_file = folder.split('/')[-1]
   zipfile_pattern = re.compile(rf'({zip_file}_)(\d)?(\.zip)')
   for zip_name in os.listdir(f'{folder}/..'):
       if zipfile_pattern.search(zip_name):
           if int(zipfile_pattern.findall(zip_name)[0][1]) > bak_num:
                bak_num = int(zipfile_pattern.findall(zip_name)[0][1])
       else:
           continue
   with zipfile.ZipFile(f'{zip_file}_{bak_num + 1}.zip', 'w') as folder_bak:
       for folder_name, sub_folder, file_names in os.walk(folder):
           print(folder_name)
           folder_bak.write(folder_name)
           for filename in file_names:
               print(filename)
               folder_bak.write(os.path.join(folder_name, filename))

#backupToZip(str(input('Folder path: ')))
backupToZip('/home/alexandre/PycharmProjects/atbswp/delicious')


