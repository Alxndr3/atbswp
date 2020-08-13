import os
import re
import shutil


def copy_by_extension(from_folder, to_folder, extension):
    """
    copy_by_extension.py - searches a folder or folder tree and copies files with a certain extension to another
    chosen folder.
    :param from_folder: Path to folder which files must be copied from.
    :param to_folder: Path to folder which files must be copied to.
    :param extension: Extension of the files. Eg. (.txt .pdf)
    :param tree: Y to search folder tree or N to search only the parent folder.
    :return: List of copied files.
    """
    extension_ = re.compile(r'(.*?)(%s)' %(extension))
    for folder, sub_folder, file_name in os.walk(from_folder):
        try:
            for files in file_name:
                if extension_.search(files):
                    print('Copying %s/%s' %(folder, files))
                    print('To %s/%s' %(to_folder, files))
                    shutil.copy(folder + '/' + files, to_folder)
        except shutil.SameFileError:
            print('Same file found: %s' % (file_name[0]))
            break


copy_by_extension('/home/alexandre/PycharmProjects/atbswp/delicious',
                  '/home/alexandre/PycharmProjects/atbswp/bacon',
                  '.jpg')
#copy_by_extension('/home/alexandre/Downloads', 'delicious','.pdf', 'n')

