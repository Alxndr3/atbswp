import shelve

'''
shelf_file = shelve.open('mydata')
cats = ['Zophie', 'Pooka', 'Simon']
shelf_file['cats'] = cats
shelf_file.close()
'''
shelf_file = shelve.open('mydata')
print(type(shelf_file))
print(shelf_file['cats'])
shelf_file.close()

shelf_file = shelve.open('mydata')
print(list(shelf_file.keys()))
print(list(shelf_file.values()))
