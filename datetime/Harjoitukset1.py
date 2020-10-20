from datetime import datetime, timedelta

now = datetime.now()

print("Current date and time:" , now)

year = now.strftime('%Y')
print("Current year:", year)

month = now.strftime('%B')
print("Month of year:", month)

week = now.strftime("%W")
print("Week number of the year:", week)

week_day = now.strftime('%w')
print("Weekday of the week", week_day)

day_of_year = now.strftime('%j')
print("Day of year:", day_of_year)

day_of_month = now.strftime('%d')
print("Day of the month:", day_of_month)

day_of_week = now.strftime('%A')
print("Day of week:", day_of_week)