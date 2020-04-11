import calendar
import datetime
import time

print(calendar.weekheader(3))
print()

print(calendar.firstweekday())
print()

print(calendar.month(2020,4,))

print(calendar.monthcalendar(2020,4))

print(calendar.calendar(2020))

day_of_the_week = calendar.weekday(2020, 4, 11)
print(day_of_the_week)

how_many_leap_days = calendar.leapdays(2000,2021)
print(how_many_leap_days)
