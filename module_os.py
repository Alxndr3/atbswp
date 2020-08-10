import os


# Check one directory total size
# This program checks only files, not folders
total_size = 0
directory = '/home/alexandre/Downloads'
for filename in os.listdir(directory):
    total_size += os.path.getsize(os.path.join(directory, filename))
    print(filename)
print(total_size)

print(os.path.exists('/home/alexandre'))
print(os.path.exists('/home/alexandre/bla'))
print(os.path.isdir('/home/alexandre'))
print(os.path.isfile('/home/alexandre'))
print(os.path.isdir('/usr/bin/kcalc'))
print(os.path.isfile('/usr/bin/kcalc'))
# Check whether or not a usb flash driver is connected to the computer
print(os.path.exists('/media/alexandre/d-live 10.4.0 kd i386'))


