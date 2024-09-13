import pyperclip

concatenated_list = []

items = pyperclip.paste()
items = items.split('\n')
for item in items:
    concatenated_list.append(f'* {item}')


concatenated_list = '\n'.join(concatenated_list)
print(concatenated_list)