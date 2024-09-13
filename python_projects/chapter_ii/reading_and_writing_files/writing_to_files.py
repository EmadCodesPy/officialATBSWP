steakFile = open('/users/emad/desktop/steak.txt', 'w')  #opens file in write mode
steakFile.write('Hello world!\n')
steakFile.close()
steakFile = open('/users/emad/desktop/steak.txt', 'a') #opens file in append mode
steakFile.write('Steak is delicious!')
steakFile = open('/users/emad/desktop/steak.txt')
content = steakFile.read()
steakFile.close()
print(content)