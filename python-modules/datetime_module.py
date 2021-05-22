
import datetime
# import os
import inspect

print(datetime.__file__)
print(inspect.getfile(datetime.date))
d = datetime.date(2016, 12, 7)
tday = datetime.date.today()
print(tday)
print(tday.day)
print(tday.year)
print(tday.month)
print(d)

# MOnday 0 Sunday 6
print(tday.weekday())
# MOnday 1 Sunday 7
print(tday.isoweekday())

tdelta = datetime.timedelta(days=7)

print(tday + tdelta)
print(tday - tdelta)

bday = datetime.date(2021, 9, 24)

till_bday = bday - tday

print(till_bday)
print(till_bday.total_seconds())

# datetime.date datetime.time datetime.datetime

t = datetime.time(9, 30, 45, 100000)

print(t.hour)

dt = datetime.datetime(2016, 7, 27, 12, 20, 48, 100000)

print(dt.date())
print(dt.time())
print(dt.year)

print(dt + tdelta)

tdelta = datetime.timedelta(hours=23)

print(dt + tdelta)

dt_today = datetime.datetime.today()
dt_now = datetime.datetime.now()
dt_utcnow = datetime.datetime.utcnow()

print(dt_today)
print(dt_now)
print(dt_utcnow)

import pytz

# dt = datetime.datetime(2016, 7, 27, 12, 30, 45, tzinfo=pytz.UTC)

print(dt)

dt_utcnow = datetime.datetime.now(tz=pytz.UTC)

print(dt_utcnow)


import re

for tz in pytz.all_timezones:
    if re.match('.*Shang.*', tz):
        print(tz)

dt_sh = dt_utcnow.astimezone(pytz.timezone('Asia/Shanghai'))

print(dt_sh)

dt_local = datetime.datetime.now()

print(dt_local)


dt_mtn = datetime.datetime.now(tz=pytz.timezone('US/Mountain'))

print(dt_mtn.strftime('%B %d, %Y'))

dt_str = 'July 26, 2016'

dt = datetime.datetime.strptime(dt_str, '%B %d, %Y')

print(dt)
