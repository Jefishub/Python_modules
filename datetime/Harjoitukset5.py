from datetime import datetime, timedelta
"""
Write a Python program to convert unix timestamp string to readable date.
Sample Unix timestamp string : 1596155682

Output:
2020-07-31 03:34:42
"""

timestamp1 = 1528797322
timestamp2 = 1596155682
date_time1 = datetime.fromtimestamp(timestamp1)
date_time2 = datetime.fromtimestamp(timestamp2)

print(date_time1)
print(date_time2)