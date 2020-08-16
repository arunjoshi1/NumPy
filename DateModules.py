import datetime
from datetime import date, timezone, tzinfo
import pytz
from pytz import utc

d = datetime.date.today()
print(d)

# weekday and isoweek day
print(d.weekday())
print(d.isoweekday())

# time delta
timeDelta = datetime.timedelta(days=7)
print(d + timeDelta)
print('today {d} , after week {nextWeek}'.format(d=d, nextWeek=d + timeDelta))

bDay = datetime.date(year=2020, day=20, month=9)
print((bDay - d).days)

# pytz package
utcNow = datetime.datetime(2020, 8, 16, 17, 32, 10, tzinfo=pytz.UTC)
print(f'utc now :{utcNow}')
indiaTime = utcNow.astimezone(pytz.timezone('Asia/Kolkata'))
print(f'indian time :{indiaTime}')