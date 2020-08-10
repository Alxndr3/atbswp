'''
# reading a file as a single big string
hello_file = open('/home/alexandre/PycharmProjects/atbswp/hello.txt', 'r')
hello_content = hello_file.read()
print(hello_content)
'''
'''
# Read each line of a file as it was a list
sonnet_file = open('/home/alexandre/PycharmProjects/atbswp/sonnet29.txt', 'r')
print(sonnet_file.readlines())
'''
# create a new file with the w as second argument, close it, reopen it in a 'append' mode write again on it,
# close it, save its content as a variable and print it in the terminal
bacon_file = open('bacon.txt', 'w')
bacon_file.write('Hello Bacon!\n')
bacon_file.close()
bacon_file = open('bacon.txt', 'a')
bacon_file.write('Bacon is not a vegetable.')
bacon_file = open('bacon.txt')
content = bacon_file.read()
bacon_file.close()
print(content)


