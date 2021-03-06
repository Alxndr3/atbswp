#! /usr/bin/bash
# form-filler.py - Automatically fills in the form.


import pyautogui

form_data = [{'name': 'Alice', 'fear': 'eavesdroppers', 'source': 'wand', 'robocop': 4, 'comments': 'Tell Bob I said hi.'}, 
            {'name': 'Bob', 'fear': 'bees', 'source': 'amulet', 'robocop': 4, 'comments': 'n/a'}, 
            {'name': 'Carol', 'fear': 'puppets', 'source':'crystal ball', 'robocop': 1, 'comments': 'Please take the puppets out of the break room.'}, 
            {'name': 'Alex Murphy', 'fear': 'ED-209', 'source': 'money', 'robocop': 5, 'comments': 'Protect the innocent. Serve the public trust. Uphold the law.'}, ]

pyautogui.PAUSE = 0.5
print('Ensure that the browser window is active and the form is loaded!')

for person in form_data:
    print('>>> 5-SECOND PAUSE TO LET USER PRESS CTRL-C <<<')
    pyautogui.sleep(5)

    print('Entering %s info...' % (person['name']))
    pyautogui.write(['\t', '\t'])

    # Wait until the form page has loaded. 
    # Fill out the Name Field. 
    pyautogui.write(person['name'] + '\t')

    # Fill out the Greatest Fear(s) field. 
    pyautogui.write(person['fear'] + '\t')

    # Fill out the Source of Wizard Powers field. 
    if person['source'] == 'wand':
        pyautogui.write(['down'], 0.5)
        pyautogui.press('enter')
        pyautogui.write(['\t'], 0.5)
    elif person['source'] == 'amulet':
        pyautogui.write(['down', 'down'], 0.5)
        pyautogui.press('enter')
        pyautogui.write(['\t'], 0.5)
    elif person['source'] == 'crystal ball':
        pyautogui.write(['down', 'down', 'down'], 0.5)
        pyautogui.press('enter')
        pyautogui.write(['\t'], 0.5)
    elif person['source'] == 'money':
        pyautogui.write(['down', 'down', 'down', 'down'], 0.5)
        pyautogui.press('enter')
        pyautogui.write(['\t'], 0.5)

    # Fill out the RoboCop field. 
    if person['robocop'] == 1:
        pyautogui.write([' ', '\t', '\t'], 0.5)
    elif person['robocop'] == 2:
        pyautogui.write(['right', '\t', '\t'], 0.5)
    elif person['robocop'] == 3:
        pyautogui.write(['right', 'right', '\t', '\t'], 0.5)
    elif person['robocop'] == 4:
        pyautogui.write(['right', 'right', 'right', '\t', '\t'], 0.5)
    elif person['robocop'] == 5:
        pyautogui.write(['right', 'right', 'right', 'right', '\t', '\t'], 0.5)

    # Fill out the Additional Comments field. 
    pyautogui.write(person['comments'] + '\t')

    # Click Submit button by pressing enter. 
    pyautogui.sleep(0.5) # Wait for the button to activate.
    pyautogui.press('enter')

    # Wait until form page has loaded. 
    print('Submit form.')
    pyautogui.sleep(5)

    # Click the Submit another response link.
    pyautogui.write(['\t', '\n'])



