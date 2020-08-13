import zipfile
import os


os.chdir('delicious')
#with zipfile.ZipFile('example.zip') as example_zip:
#    # Reading zip files
#    print(example_zip.namelist())
#    spam_info = example_zip.getinfo('spam.txt')
#    print(spam_info)
#    print(spam_info.file_size)
#    print(spam_info.compress_size)
#    print('Compressed file is %sx smaller!' % round(spam_info.file_size / spam_info.compress_size, 2))
#    # Extracting zip file
#    example_zip.extractall()
#    example_zip.extractall('./example_folder')
#    example_zip.extract('spam.txt', './single_file')

# Creating zip files
with zipfile.ZipFile('new.zip', 'w') as new_zip:
    new_zip.write('cats', compress_type=zipfile.ZIP_DEFLATED)
# Appending files to zip file
with zipfile.ZipFile('new.zip', 'a') as new_zip:
    new_zip.write('.credentials', compress_type=zipfile.ZIP_DEFLATED)
open_zip = zipfile.ZipFile('new.zip')
print(open_zip.namelist())