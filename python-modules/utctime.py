
# print(help(map))

import time
import datetime

epoch = time.time()

today = datetime.datetime.utcnow()
start_time = datetime.datetime(1970, 1, 1)
print(today)

print(datetime.date.fromtimestamp(epoch))

days = epoch // (24 * 60 * 60)
d_re = epoch - days * 24 * 60 * 60
hours = d_re // (60 * 60)
h_re = d_re - hours * (60 * 60)
minutes = h_re // 60
m_re = h_re - minutes * 60
seconds = m_re

print(epoch)
print(today - start_time)
print(days)
print(hours)
# print(d_re)
print(minutes)
print(seconds)

