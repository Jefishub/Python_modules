"""
Write a Python program to convert Year/Month/Day to Day of Year.

Output: 214
import datetime
today = datetime.datetime.now()
# YOUR CODE HERE
print(day_of_year)
"""

import datetime
today = datetime.datetime.now()
day_of_year = (today - datetime.datetime(today.year, 1, 1)).days + 1
print(day_of_year)