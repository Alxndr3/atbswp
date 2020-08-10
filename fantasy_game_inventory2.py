stuff = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}
dragon_loot = ['ruby', 'gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']


def add_to_inventory(inventory, added_items):
    for i in added_items:
        if i not in inventory:
            stuff[i] = 0
        for k, v in stuff.items():
            if i == k:
                stuff[k] = stuff[k] + 1

    print('Inventory:')
    for k, v in stuff.items():
        print(v, k)


add_to_inventory(stuff, dragon_loot)
