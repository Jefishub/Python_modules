from datetime import datetime, timedelta
"""
Write a Python program to subtract four days from current date.
The output below is just an example

Output:
Current Date : 2020-08-01
4 days before Current Date : 2020-07-28
"""

now = datetime.now()
past_day = now - timedelta(days = 4)

print("Current Date:", now.strftime('%Y-%m-%d'))
print("4 days before Current Date:", past_day.strftime('%Y-%m-%d'))