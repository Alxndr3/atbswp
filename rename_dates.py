#!/usr/bin/env python3
# rename_dates.py - Renames filenames with American MM-DD-YYYY date format to European DD-MM-YYYY date format
import os
import re
import shutil


us_style_date = re.compile(r'([0-1][0-9])?-([0-3][0-9])?-(\d){4}')
for file in os.listdir(os.chdir('./delicious')):
   usd = us_style_date.search(file)
   if usd:
      usd_list = usd.group().split('-')
      file_list = file.split(usd.group())
      esd = usd_list[1] + '-' + usd_list[0] + '-' + usd_list[2]
      new_name = file_list[0] + esd + file_list[1]
      shutil.move(file, new_name)
