"""
import pprint


cats = [{'name': 'Zophie', 'desc': 'chubby'}, {'name': 'Pooka', 'desc': 'fluffy'}]
pprint.pprint(cats)

file_object = open('my_cats.py', 'w')
file_object.write('cats = ' + pprint.pformat(cats) + '\n')
file_object.close()
"""
import my_cats


print(my_cats.cats)
print(my_cats.cats[0])
print(my_cats.cats[0]['name'])
