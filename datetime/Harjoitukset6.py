from datetime import datetime, timedelta
"""
Write a Python program to print yesterday, today, tomorrow.
Example output is below, do it for the current date.

Output:
Yesterday : 2020-07-31
Today : 2020-08-01
Tomorrow : 2020-08-02
"""

now = datetime.now()
yesterday = now - timedelta(days = 1)
tomorrow = now + timedelta(days = 1)

print("Yesterday:", yesterday.strftime('%Y-%m-%d'))
print("Today:", now.strftime('%Y-%m-%d'))
print("Tomorrow:", tomorrow.strftime('%Y-%m-%d'))