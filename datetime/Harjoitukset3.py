from datetime import datetime
"""
Write a Python program to get the current time in Python
Sample Format : 15:17:49.078205
"""

now = datetime.now()

my_time = now.strftime('%H:%M:%S.%f')
print(my_time)