from datetime import datetime, date
"""
Write a Python program to convert the date to datetime (midnight of the date)
in Python. Example input 2020-08-01 20:30:00

Sample Output:
2020-08-01 00:00:00
"""

dt = date.today()
print(datetime.combine(dt,datetime.min.time()))