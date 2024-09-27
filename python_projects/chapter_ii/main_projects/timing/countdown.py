import time, subprocess

timeLeft = 5
    
for i in range(timeLeft):
    print(timeLeft)
    timeLeft -= 1
    time.sleep(1)

subprocess.Popen(['start', 'B:\\Unreleased\\I\'m Better Ft. Sampha.mp3'], shell=True)