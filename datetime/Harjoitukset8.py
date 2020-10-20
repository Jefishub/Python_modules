"""
Write a Python program to find the date of the first Monday of a given week.
Sample Year and week : 2020, 28

Mon Jul 13 00:00:00 2020
"""

import time
print(time.asctime(time.strptime('2020 28 1', '%Y %W %w')))
