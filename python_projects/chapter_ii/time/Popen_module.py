import subprocess

chromeProc = subprocess.Popen("C:\Program Files\Google\Chrome\Application\chrome.exe")
print(chromeProc.poll() == None)
chromeProc.wait()
print('Done')
print(chromeProc.poll())