#! python3
# backup_to_zip1.py - Copies an entire folder and its contents into a zip file whose filename increments
import re
import os
import zipfile


def backupToZip(folder):
    # Backup the entire contents of "folder" into ZIP file.
    folder = os.path.abspath(folder) # make sure folder is absolute
    # Figure out the filename this code should use based on what files already exist.
    number = 1
    while True:
        zip_filename = os.path.basename(folder) + '_' + str(number) + '.zip'
        if not os.path.exists(zip_filename):
            break
        number += 1
    # Create the zip file
    print('Creating %s...' %(zip_filename))
    backup_zip = zipfile.ZipFile(zip_filename, 'w')
    # Walk the entire folder tree and compress the files in each folder.
    for folder_name, sub_folder, file_names in os.walk(folder):
        print('Adding files in %s...' %(folder_name))
        # Add the current folder to the ZIP file.
        backup_zip.write(folder_name)
        # Add all the files in this folder to the ZIP file.
        for filename in file_names:
            new_base = os.path.basename(folder) + '_'
            if filename.startswith(new_base) and filename.endswith('.zip'):
                continue # don't backup the backup the backup zip files
            backup_zip.write(os.path.join(folder_name, filename))
    backup_zip.close()
    print('Done.')


backupToZip('delicious')


