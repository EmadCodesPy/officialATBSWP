import time, pyperclip

print('Press ENTER to begin. Afterwards, press ENTER to "Click" the stopwatch. Press Ctrl-C to quit.')
input()
print('Started.')
startTime = time.time()
lastTime = startTime
lapNum = 1

try:
    while True:
        input()
        lapTime = round(time.time() - lastTime, 2)
        totalTime = round(time.time() - startTime, 2)
        output = 'Lap #%s: %s (%s)' % (str(lapNum).rjust(2), str(totalTime).rjust(6), str(lapTime).rjust(7))
        pyperclip.copy(output)
        print(output, end='')
        lapNum += 1
        lastTime = time.time()
except KeyboardInterrupt:
    print('\nDone')
