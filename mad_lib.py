import re

adj = re.compile(r'ADJECTIVE(.)?')
noun = re.compile(r'NOUN(.)?')
adv = re.compile(r'ADVERB(.)?')
verb = re.compile('VERB(.)?')
wildcard = re.compile(r'(.)?')

file_path = str(input('Type in absolute path to file: '))
new_file_path = file_path + '_new'
new_text = list()
with open(file_path) as file:
    file_content = file.readlines()
    file.close()
with open(new_file_path, 'w') as new_file:
    for line in file_content:
        content_split = line.split()
        for y in content_split:
            dot = False
            for z in y:
                if wildcard.search(z):
                    dot = True
                    character = z
            if adj.search(y):
                if dot:
                    new_text.append(str(input('Type in an adjective: ') + character))
                else:
                    new_text.append(str(input('Type in an adjective: ')))
            elif noun.search(y):
                if dot:
                    new_text.append(str(input('Type in an noun: ') + character))
                else:
                    new_text.append(str(input('Type in an noun: ')))
            elif adv.search(y):
                if dot:
                    new_text.append(str(input('Type in an adverb: ') + character))
                else:
                    new_text.append(str(input('Type in an adverb: ')))
            elif verb.search(y):
                if dot:
                    new_text.append(str(input('Type in an verb: ') + character))
                else:
                    new_text.append(str(input('Type in an verb: ')))
            elif y:
                new_text.append(y)
            string = ' '.join(new_text)
        print(string)
        new_file.write(string)
        new_file.write('\n')
        new_text.clear()

