import datetime

d = datetime.datetime.now()

print(d.strftime('%y.%m.%d time is %H:%M'))

date_str = '02.12 and year 2025'
input_date = datetime.datetime.strptime(date_str, '%d.%m and year %Y')
print(input_date)
print(input_date.year, input_date.day)

result = d - input_date
print(result.microseconds)
print(result.days)

delta_date = d - datetime.timedelta(days=7)
delta_date = d - datetime.timedelta(days=3)

print(d, delta_date)

from datetime import date, datetime

today = date.today()
current_month_start = today.replace(day=1)
current_month_start = today.replace(day=1, month=1)
print(current_month_start)
