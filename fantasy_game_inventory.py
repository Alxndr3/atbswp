stuff = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}


def display_inventory(stuff):
    total_stuff = 0
    print('Inventory:')
    for k, v in stuff.items():
        print(f'{v} {k}')
        total_stuff += v
    print()
    print(f'Total number of items: {total_stuff}')


display_inventory(stuff)
