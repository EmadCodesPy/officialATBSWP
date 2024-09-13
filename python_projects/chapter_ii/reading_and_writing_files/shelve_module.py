import shelve
#this saves python variables to the hard drive in binary format (check mydata.db)



with shelve.open('cats') as db:
    cats = ['Leo', 'Prada', 'Dormamu']
    db['cats'] = cats
    dogs = ['josh', 'allen', 'brook']
    db['dogs'] = dogs

with shelve.open('cats') as db:
    print(dict(db))