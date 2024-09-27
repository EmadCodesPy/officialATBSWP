import datetime, time

currentDatetime = datetime.datetime.now()
print(currentDatetime)
dt = datetime.datetime(2024, 1, 1, 18, 30, 0, 0)
print(dt.year,  dt.month, dt.day)
print(dt.hour, dt.minute, dt.second)

#fromtimestamp gets the date from the unix epoch
td = datetime.datetime.fromtimestamp(time.time())
print(td)
print(td > dt)