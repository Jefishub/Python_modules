from datetime import date, datetime, timedelta


now = datetime.now()
print(now)

tomorrow_delta = timedelta(days=+1)
print(tomorrow_delta)

date_tomorrow = now + timedelta(days=3)
print(date_tomorrow)

ini_time_for_now = datetime.now()

print("Initial date", str(ini_time_for_now))

date_future = ini_time_for_now +  timedelta(days=730)

print(date_future)


now = datetime.now()
print(now)
print(type(now))

year = now.strftime('%Y')
print("year:",year)

month = now.strftime('%m')
print("Month:", month)

month_b = now.strftime('%b')
print("Month:", month_b)

month_B = now.strftime('%B')
print("Month:", month_B)

day = now.strftime('%d')
print("Day:",day)


timestamp = 1528797322
date_time = datetime.fromtimestamp(timestamp)

print("Date time object:", date_time)

d1 = date_time.strftime('%m/%d/%Y, %H:%M:%S')
print("Output 2:", d1)

d2 = date_time.strftime('%d %b %Y')
print("Output 2:", d2)

d3 = date_time.strftime('%d %B %Y')
print("Output 2:", d3)

d = date_time.strftime('%I%p')
print("Output 2:", d)