#!/usr/bin/env python3
# stopwatch.py - A simple stopwatch program.


import time


# Display the program's instructions.
print('Press Enter to begin. Afterward, press Enter to "click" the stopwatch. '
      'Press Ctrl-C to quit.')
input()                     # Press Enter to begin.
print('Started.')
start_time = time.time()    # get the first lap's start time.
last_time = start_time
lap_num = 1

# Start tracking the lap time.
try:
    while True:
        input()
        lap_time = round(time.time() - last_time, 2)
        total_time = round(time.time() - start_time, 2)
        print('Lap #%s: %s (%s)' % (lap_num, total_time, lap_time), end='')
        lap_num += 1
        last_time = time.time() # reset the last time
except:
    # Handle the Ctrl-C exception to keep its error message from displaying.
    print('\nDone')

