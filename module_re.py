import re

'''
phone_number_regex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
mo = phone_number_regex.search('My number is 415-555-4242.')
print('Phone number found: ', mo.group())
'''
'''
phone_number_regex = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
mo = phone_number_regex.search('My number is 415-555-4242.')
print(mo.group(0))
print(mo.group(1))
print(mo.group(2))
print(mo.groups())
area_code, main_number = mo.groups()
print(area_code)
print(main_number)
'''
'''
phone_number_regex = re.compile(r'(\(\d\d\d\))-(\d\d\d-\d\d\d\d)')
mo = phone_number_regex.search('My number is (415)-555-4242.')
print(mo.group())
'''
'''
hero_regex = re.compile(r'Batman|Tina Fey')
mo1 = hero_regex.search('Batman and Tina Fey')
print(mo1.group())
mo2 = hero_regex.search('Tina Fey and Batman')
print(mo2.group())
'''
'''
bat_regex = re.compile(r'Bat(man|mobile|copter|bat)')
mo = bat_regex.search('Batmobile lost a wheel')
print(mo.group())
print(mo.group(1))
'''
'''
bat_regex = re.compile(r'Bat(wo)?man')
mo1 = bat_regex.search('The Adventures of Batman')
print(mo1.group())
mo2 = bat_regex.search('The Adventures of Batwoman')
print(mo2.group())
'''
'''
phone_regex = re.compile(r'(\d{3}-)?\d{3}-\d{4}')
mo1 = phone_regex.search('My number is 415-555-4242')
print(mo1.group())
mo2 = phone_regex.search('My number is 555-4242')
print(mo2.group())
'''
'''
bat_regex = re.compile(r'Bat(wo)*man')
mo1 = bat_regex.search('The Adventures of Batman')
print(mo1.group())
mo2 = bat_regex.search('The Adventures of Batwoman')
print(mo2.group())
mo3 = bat_regex.search('The Adventures of Batwowowowoman')
print(mo3.group())
'''
'''
bat_regex = re.compile(r'Bat(wo)+man')
mo1 = bat_regex.search('The Adventures of Batwoman')
print(mo1.group())
mo2 = bat_regex.search('The Adventures of Batwowowoman')
print(mo2.group())
mo3 = bat_regex.search('The Adventures of Batman')
print(mo3 is None)
'''
'''
ha_regex = re.compile(r'(Ha){3}')
mo1 = ha_regex.search('HaHaHa')
print(mo1.group())
mo2 = ha_regex.search('Ha')
print(mo2 is None)
'''
'''
# Greedy and Non-greedy
greedy_ha_regex = re.compile(r'(Ha){3,5}')
mo1 = greedy_ha_regex.search('HaHaHaHaHa')
print(mo1.group())
nongreedy_ha_regex = re.compile(r'(Ha){3,5}?')
mo2 = nongreedy_ha_regex.search('HaHaHaHaHa')
print(mo2.group())
'''
'''
# The findall() method
phone_num_regex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
mo1 = phone_num_regex.search('Cell: 415-555-9999 Work: 212-555-0000')
print(mo1.group())
mo2 = phone_num_regex.findall('Cell: 415-555-9999 Work: 212-555-0000')
print(mo2)
phone_num_regex = re.compile(r'(\d\d\d)-(\d\d\d)-(\d\d\d\d)')
mo3 = phone_num_regex.findall('Cell: 415-555-9999 Work: 212-555-0000')
print(mo3)
'''
'''
xmas_reges = re.compile(r'\d+\s\w+')
print(xmas_reges.findall('12 drummers, 11 pipers, 10 lords, 9 ladies, 8 maids, '
                   '7 swans, 6 geese, 5 rings, 4 birds, 3 hens, 2 doves, 1 partridge'))
'''
'''
# Making your own Character classes
vowel_regex = re.compile(r'[aeiouAEIOU]')
print(vowel_regex.findall('RoboCop eats baby food. BABY FOOD'))
consonant_regex = re.compile(r'[^aeiouAEIOU]')
print(consonant_regex.findall('RoboCop eats baby food. BABY FOOD'))
'''
'''
begins_with_hello = re.compile(r'^Hello')
print(begins_with_hello.search('Hello World'))
print(begins_with_hello.search('He said Hello') is None)

ends_with_number = re.compile(r'\d$')
print(ends_with_number.search('Your number is 42'))
print(ends_with_number.search('Your number is forty two.') is None)

whole_string_is_num = re.compile(r'^\d+$')
print(whole_string_is_num.search('1234567890'))
print(whole_string_is_num.search('12345x67890') is None)
print(whole_string_is_num.search('12345 67890') is None)
'''
'''
# The Wildcard Character
at_regex = re.compile(r'.at')
print(at_regex.findall('The cat in the hat sat on the flat mat 1at at'))
'''
'''
# Maching Every Character with Dot-Star
name_regex = re.compile(r'First Name: (.*) Last Name: (.*)')
mo = name_regex.search('First Name: Alexandre Last Name: Cardoso')
print(mo.group(1))
print(mo.group(2))
'''
'''
non_greedy_regex = re.compile(r'<.*?>')
mo = non_greedy_regex.search('<To serve man> for dinner.>')
print(mo.group())
greedy_regex = re.compile(r'<.*>')
mo = greedy_regex.search('<To serve man> for dinner.>')
print(mo.group())
'''
'''
no_new_line_regex = re.compile(r'.*')
print(no_new_line_regex.search('Serve the public trust.\nProtect the innocent.\nUphold the law.').group())
new_line_regex = re.compile(r'.*', re.DOTALL)
print(new_line_regex.search('Serve the public trust.\nProtect the innocent.\nUphold the law.').group())
'''
'''
# Case Insentive
robocop = re.compile(r'robocop', re.I)
print(robocop.search('RoboCop is part man, part machine, all cop').group())
print(robocop.search('ROBOCOP protects the innocent').group())
print(robocop.search('Al, why does your programing book talk abou robocop so much?').group())
'''
'''
# sub() method
names_regex = re.compile(r'Agent \w+')
print(names_regex.sub('CENSORED', 'Agent Alice gave the secret documents to Agent Bob'))
'''
'''
agent_names_regex = re.compile(r'Agent (\w)\w*')
print(agent_names_regex.sub(r'\1****', 'Agent Alice told Agent Carol that Agent Eve Knew Agent Bob was a double agent'))
'''

'''
20. How would you write a regex that matches a number with commas for every three digits? [
It must match the following: 
'42' 
'1,234' 
'6,368,745' 
but not the following: 
'12,34,567' (which has only two digits between the commas) 
'1234' (which lacks commas)
'''
# coma_regex = re.compile(r'(\d{1,3},?)(\d{3})*,?')
name_regex = re.compile(r'(Alice|Bob|Carol|BOB) (pets|pets|throws|EATS) ([aA]pples|CATS|cats|baseball|FOOTBALLS)')
print(name_regex.search('BOB EATS CATS').group())
