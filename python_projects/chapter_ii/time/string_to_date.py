import datetime

a = datetime.datetime.strptime('October 21, 2015', '%B %d, %Y')
print(a)
b = datetime.datetime.strptime('2015/10/21 16:29:00', '%Y/%m/%d %H:%M:%S')
print(b)
c = datetime.datetime.strptime('October of \'15', '%B of \'%y')
print(c)
d = datetime.datetime.strptime('November of \'63', '%B of \'%y')
print(d)