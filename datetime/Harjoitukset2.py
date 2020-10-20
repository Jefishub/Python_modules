from datetime import datetime, timedelta

"""
Write a Python program to convert a string to datetime.
The input string example:
'Jul 1 2019 5:43PM'
"""

now = datetime.now()

my_date = now.strftime('%b %d %Y %H:%M%p')
print(my_date)