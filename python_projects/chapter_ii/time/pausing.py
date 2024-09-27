import datetime, time

while datetime.datetime.now() < datetime.datetime(2024, 9, 21, 13, 45):
    time.sleep(10)

print('Time passed')