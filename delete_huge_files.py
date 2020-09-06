import os
import shutil


search_folder = str(input('Folder to search: '))
size_file = int(input('File size in MB: '))
for folder, sub_folder, files in os.walk(search_folder):
    for file in files:
        file_size = os.path.getsize(folder + '/' + file)
        if file_size > size_file * 1000000:
            print('Deleting: %s'  %(file))
            os.unlink(folder + '/' + file)
