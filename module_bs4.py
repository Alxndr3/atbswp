import bs4
import requests

# Create Beautifulsoup Object from HTML
# res = requests.get("https://nostarch.com")
# res.raise_for_status()
# no_starch_soup = bs4.BeautifulSoup(res.text, features="html.parser")
# print(type(no_starch_soup))

# res = requests.get("https://nostarch.com/automatestuff2")
# res.raise_for_status()
# with open('nostarch', 'wb') as nostart_file:
#    for chunck in res.iter_content(100000):
#        nostart_file.write(chunck)
# with open('nostarch') as example_file:
#    example_soup = bs4.BeautifulSoup(example_file, features='html.parser')
# print(type(example_soup))
# for i in example_soup.select('input[name="form_id"C]'):
#    print(i)

# Finding an Element with the select() Method
# with open('example.html') as example_file:
#    example_soup = bs4.BeautifulSoup(example_file.read(), features="html.parser")
#    elements = example_soup.select('#author')
#    print(type(elements))
#    print(len(elements))
#    print(type(elements[0]))
#    for x in range(len(elements)):
#        print(elements[x].getText())
#        print()
#        print(str(elements[x]))
#        print()
#        print(elements[x].attrs)

# Getting Data from an Element's Attributes
soup = bs4.BeautifulSoup(open('example.html'), features="html.parser")
span_elem = soup.select('span')[0]
print(str(span_elem))
print(span_elem.get('id'))
print(span_elem.get('some_non_existent_addr') is None)
print(span_elem.attrs)

