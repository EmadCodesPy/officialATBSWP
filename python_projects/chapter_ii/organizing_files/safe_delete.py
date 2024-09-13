import send2trash

spamFile = open('spam.txt', 'a')
spamFile.write('This is a spam file to be sent2trash')
spamFile.close()
send2trash.send2trash('spam.txt') #Sends file to the trash so that is can be restored later