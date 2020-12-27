#!/usr/bin/env python3
# stopwatch.py - A simple stopwatch program.


import pyperclip
import time


# Display the program's instructions.
print('Press Enter to begin. Afterward, press Enter to "click" the stopwatch. '
      'Press Ctrl-C to quit.')
input()                     # Press Enter to begin.
print('Started.')
start_time = time.time()    # get the first lap's start time.
last_time = start_time
lap_num = 1
tlist = list()

# Start tracking the lap time.
try:
    while True:
        input()
        lap_time = round(time.time() - last_time, 2)
        total_time = round(time.time() - start_time, 2)
        trun = "Lap #%s: %s (%s)" % (str(lap_num).rjust(2), str(total_time).rjust(5), str(lap_time).rjust(5))
        print(trun, end='')
        tlist.append(trun)
        lap_num += 1
        last_time = time.time() # reset the last time
except:
    # Handle the Ctrl-C exception to keep its error message from displaying.
    print('\nDone')
    pyperclip.copy(str(tlist))

