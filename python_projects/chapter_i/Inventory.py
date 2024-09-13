inventory = {'Sword': 1, 'Torch': 42, 'Diamond': 64, 'Steak': 53}

def Display_inventory(param):
    print('Inventory:')
    total = 0
    for k,v in inventory.items():
        print(str(k)+' '+str(v))
        total = total + v
    print('Total number of items is: ' + str(total))

Display_inventory(inventory)

print(' ')

dragonloot = ['Diamond', 'dagger', 'Diamond', 'Diamond', 'ruby']

def addToInventory(inventory, addItems):
    for item in addItems:
        if item in inventory:
            inventory[item] += 1
            pass
        else:
            inventory[item] = 1
    return inventory
print(Display_inventory((addToInventory(inventory, dragonloot))))