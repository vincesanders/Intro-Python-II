def print_game_state(player):
    print(player.room.art)
    print(f'{player.name}, {player.room}')
    if len(player.room.items) is 0:
        print('This room is empty.')
    else:
        for item in player.room.items:
            print(item)
    if len(player.items) > 0:
        for item in player.items:
            print(f'You are holding a {item.name}')
    else:
        print('You are holding nothing.')
def handle_direction_input(user_input, player):
    if 'south' in user_input:
        direction = 's_to'
    elif 'north' in user_input:
        direction = 'n_to'
    elif 'east' in user_input:
        direction = 'e_to'
    elif 'west' in user_input:
        direction = 'w_to'
    else:
        direction = ''
    if hasattr(player.room, direction):
        player.room = getattr(player.room, direction)
    elif user_input == '9':
        print(f'Thanks for playing, {player.name}!')
    else:
        print(f'{player.name}, you can\'t go that way.')
def handle_item_input(user_input, player, items):
    if 'get' in user_input or 'pick up' in user_input:
        inputs = user_input.rsplit(' ')
        if 'get' in user_input:
            item = inputs[inputs.index('get') + 1]
        else:
            item = inputs[inputs.index('up') + 1]
        if len(player.items) < 2:
            player.get_item(items[item]) #TODO validation to ensure item is in room
            items[item].on_take()
            player.room.remove_item(items[item])
        else:
            print('You can only have two items. if you want to pick up this item, you will have to drop one of the items you are holding.')
    elif 'drop' in user_input or 'put down' in user_input:
        inputs = user_input.rsplit(' ')
        if 'drop' in user_input:
            item = inputs[inputs.index('drop') + 1]
        else:
            item = inputs[inputs.index('down') + 1]
        if len(player.items) <= 0:
            print('You don\'t have any items to drop.')
        else:
            player.drop_item(items[item])
            items[item].on_drop()
            player.room.add_item(items[item])