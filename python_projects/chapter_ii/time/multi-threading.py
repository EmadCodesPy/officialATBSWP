import threading, time

print('Start of program.')

def takeANap():
    time.sleep(5)
    return True

threadObj = threading.Thread(target=takeANap)
threadObj.start()

print('End of program.')
