import datetime, time

#delta time is a duration of time rather than a moment

delta = datetime.timedelta(days=11, hours=10, minutes=9, seconds=8)
print(delta.days, delta.seconds, delta.microseconds)
print(delta.total_seconds())
print(str(delta))
print('')

dt = datetime.datetime.now()
thousandDays = datetime.timedelta(days=1000)
endDate = dt + thousandDays
print(endDate)
print('')

td = datetime.datetime.now()
thirtyYears = datetime.timedelta(days=365*30)
print(td-thirtyYears)
print(td-(2*thirtyYears))