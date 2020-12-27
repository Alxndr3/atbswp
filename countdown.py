#! /usr/bin/env python3
# countdown.py - A simple countdown script.

from time import sleep
from subprocess import Popen
import sys

if len(sys.argv) < 2:
    print("Usage: countdown.py time_in_seconds_to_cowtdown")
    sys.exit()


def countdown(how_long):
    for c in range(how_long, 0, -1):
        print(c)
        sleep(1)
    Popen(["/usr/bin/dragon", "./alarm.wav"])


countdown(int(sys.argv[1]))
