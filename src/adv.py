from room import Room
from player import Player
from item import Item

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance", "North of you, the cave mount beckons.",
    '''                 _________      
             ___/#########\___         
          __/#################\__      
        _/#######################\_    
       /###########################\   
      /#############################\   
     /###############################\ 
    |################__##############| 
    |###############/  \#############| 
    |#############__\  /__###########| 
    |############/        \##########| 
    |###########|          |#########| 
    |###########|  |    |  |#########| 
    '''),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty passages run north and east.""",
    '''
 _____________________________________________
|.'',                                     ,''.|
|.'.'',                                 ,''.'.|
|.'.'.'',                             ,''.'.'.|
|.'.'.'.'',                         ,''.'.'.'.|
|.'.'.'.'.'',                       |.'.'.'.'.|
|.'.'.'.'.'.'';                 ;===|.'.'.'.'.|
|.'.'.'.'.'.'..',             ,'|:::|.'.'.'.'.|
|.'.'.'.'.'.'.''.|, _______ ,|.'|---|.'.'.'.'.|
|.'.'.'.'.'.'.''.|'|???????|'|.'|:::|.'.'.'.'.|
|,',',',',',','',|'|???????|'|,'|---|,',',',',|
|.'.'.'.'.'.'.''.|'|???????|'|.'|:::|.'.'.'.'.|
|.'.'.'.'.'.'.','    /###\   ','|---|.'.'.'.'.|
|.'.'.'.'.'.','     /#####\    ':===|.'.'.'.'.|
|.'.'.'.'.','      /################|.'.'.'.'.|
|.'.'.'.','       /#########\       ','.'.'.'.|
|.'.'.','        /###########\        ','.'.'.|
|.'.','         /#############\         ','.'.|
|.','          /###############\          ','.|
|;____________/#################\____________;|
    '''),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling into the darkness. Ahead to the north, a light flickers in the distance, but there is no way across the chasm.""",
    '''
##############  ) ##############
#############  ,'  #############
############   ;(,   ###########
########### ..,(.)_   ##########
###########   / | \   ##########
################################
#############|######|###########
--------------------------------
.'.'.'.'.'.'.'.'.'.'.'.'.'.'.'.'
.'.'.'.'._'.'.'.__.'.'.'_..'.'.'
.'.'.'.'/ \.'.'/  \.'.'/.\.'.'.'
.'.'.'.'|.|.'__\  /__.'|.|'.'.'.
--------|-|-/        \-|-|------
###########|          |#########
###########|  |    |  |#########
    '''),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west to north. The smell of gold permeates the air.""",
    '''
 ____________________________________________
|.'',                                     ,''|
|.'.'',                                 ,''.'|
|.'.'.'',                             ,''.'.'|
|.'.'.'.'',                         ,''.'.'.'|
|.'.'.'.'.'.',                     ,''.'.'.'.|
|.'.'.'.'.'.'.'.',                ,''.'.'.'.'|
|.'.'.'.'.'.'.'.'.'.'.,           ',''.'.'.'.|
|.'.'.'.'.'.'.''.'.'.'.'|, ______|'.'.'.'.'.'|
|.'.'.'.'.'.'.''.'.'.'.'|'|??????|'.'.'.'.'.'|
|,',',',',',',',',',',',|'|??????|,',',',',',|
|.'.'.'.'.'.'.''.'.'.'.'|'|??????|.'.'.'.'.'.|
|.'.'.'.'.'.'.'.'.'.'.'      /###|',','.'.'.'.|
|.'.'.'.'.'.'.'.'.''       /#####|','.'.'.'.'.|
|.'.'.'.'.'.'.'.'        /####### ','.'.'.'.'|
|.'.'.'.'.'.'         /#########/  ','.'.'.'.|
|.'.'.'.'.'        /############|   ','.'.'.'|
|.'.'.'.'        /##############|     ','.'.'|
|.'.'.         /################|        ','.|
|;____________/#################|___________;|
    '''),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure chamber! Sadly, it has already been completely emptied by earlier adventurers. The only exit is to the south.""",
    '''
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/______/_
'''),
}


# Link rooms together
# points to possible directions
room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

#
# Main
#
### while loop based on user input
# Make a new player object that is currently in the 'outside' room.
name = input('What is your name? ')
player = Player(name, room['outside'])
# Write a loop that:
userInput = ' '
while userInput != "9":
    # * Prints the current room name
    # * Prints the current description (the textwrap module might be useful here).
    # * Waits for user input and decides what to do.
    print(player.room.art)
    print(f'{player.name}, {player.room}')
    userInput = input('where do you want to go? (press 9 to quit): ').lower()
    if 'south' in userInput:
        direction = 's_to'
    elif 'north' in userInput:
        direction = 'n_to'
    elif 'east' in userInput:
        direction = 'e_to'
    elif 'west' in userInput:
        direction = 'w_to'
    else:
        direction = ''
    if hasattr(player.room, direction):
        player.room = getattr(player.room, direction)
    elif userInput == '9':
        print(f'Thanks for playing, {player.name}!')
    else:
        print(f'{player.name}, you can\'t go that way.')

# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.
