#!/usr/bin/env python3 # remove_csv_reader.py - Removes de header from all CSF files in the current
# working directory.
import csv
import os


os.makedirs('headerRemoved', exist_ok=True)

for csv_filename in os.listdir('.'):
    if not csv_filename.endswith('.csv'):
        continue

    print(f'Removing header from {csv_filename}...')

    # Read CSV Files
    with open(csv_filename) as csv_file:
        csv_reader = csv.reader(csv_file)

        # Create new CSV file object.
        with open(f'./headerRemoved/{csv_filename}', 'w', newline='') as output_file:
            output_writer = csv.writer(output_file)

            # Write content to new file skipping first row.
            for row in csv_reader:
                if csv_reader.line_num != 1:
                    output_writer.writerow(row)

