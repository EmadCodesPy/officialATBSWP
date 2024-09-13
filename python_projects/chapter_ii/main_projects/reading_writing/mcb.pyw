import shelve, sys, pyperclip

arg1 = sys.argv[1]
name = ' '.join(sys.argv[2:])

completeDb = shelve.open('/users/emad/desktop/python_projects/chapter_ii/main_projects/mcb')


cb = pyperclip.paste()

if arg1 == 'save':
    with shelve.open('/users/emad/desktop/python_projects/chapter_ii/main_projects/mcb') as db:
        db[name] = cb
elif arg1 == 'list':
    with shelve.open('/users/emad/desktop/python_projects/chapter_ii/main_projects/mcb') as db:
        print(dict(db))
elif arg1 == 'remove':
    with shelve.open('/users/emad/desktop/python_projects/chapter_ii/main_projects/mcb') as db:
        db.pop(name)
elif arg1 == 'clear':
    with shelve.open('/users/emad/desktop/python_projects/chapter_ii/main_projects/mcb') as db:
        db.clear()
elif arg1 in completeDb:
    value = completeDb[arg1]
    pyperclip.copy(value)

completeDb.close()