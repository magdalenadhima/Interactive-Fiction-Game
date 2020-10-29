import random


'''
Final Project: Interactive Fiction/Text-Based Adventure Game called 'Haunted House'
Create interactive fiction game where there will be rooms and player will need use exploration and puzzle-solving to reach the game's goal and win.
Author: Magdalena Dhima
'''
 
# data setup
rooms = {

    # courtyard
    'courtyard': {'name': 'a courtyard room',
                  
    'ways_to_move': {'north': {'door': 'extravagant door', 'room': 'front'},
                     'south': {'door': 'gate', 'room': 'street'}}, 
    
    'contents': {'big rock': 'fixed', 'statue': 'fixed', 'moss': 'unfixed', 'plant': 'unfixed',
                 'dog': 'unfixed', 'extravagant door': 'fixed', 'gate': 'fixed'}, 
        
    'non_players': {'dog' : {'response': 'barks.', 'wants': 'bone', 'give': 'wand',
                             'deedResponce': '\nThe dog goes, fetches a stick and puts it into your hands. You see it\'s a wand.'}}, 
            
    'devices': {'extravagant door': {'status': 'closed', 'condition': 'unlocked'},
                'gate': {'status': 'closed', 'condition': 'locked'}},

'text': """You are standing on an old soft pink-bricked pathway. There are many 
cracks. Moss and other plants have started to grow over the pathway. This is a 
overgrown courtyard with old, broken foul and sickening statues scattered 
around. Behind a big rock, you glimpse a dog. To the north you see an 
extravagant door, decorated with spine-chilling faces, leading into a tall
wooden house. To the south is a gate that leads to a street area."""},


    # front hall
    'front': {'name': 'a front hall', 
    
    'ways_to_move' : {'down': {'door': 'floor door', 'room': 'dungeon'},
                      'south': {'door': 'extravagant door', 'room': 'courtyard'},
                      'north': {'door': 'pink door', 'room': 'bedroom'},
                      'west': {'door': 'green door', 'room': 'living'},
                      'east': {'door': 'silver door', 'room': 'kitchen'}}, 
    
    'contents': {'silver door': 'fixed', 'green door': 'fixed', 'pink door': 'fixed',
                 'floor door': 'fixed', 'oil lamp': 'fixed', 'oil lamp': 'fixed', 'oil lamp': 'fixed',
                 'oil lamp': 'fixed'},
              
    'non_players': {}, 
    
    'devices': {'pink door': {'status': 'closed', 'condition': 'unlocked', 'contents': 'bone'},
                'silver door': {'status': 'closed', 'condition': 'locked', 'key': 'silver key'},
                'green door': {'status': 'closed', 'condition': 'unlocked'},
                'floor door': {'status': 'closed', 'condition': 'unlocked'},
                'extravagant door': {'status': 'open', 'condition': 'unlocked'}},

'text': """The front hall is very big. It has a big old dusty carpet with 4 oil 
lamps, high on the walls, glimmering in the rather dim room. You see that the 
front hall extends west to a green door that says 'The Living Room.' To the 
east, you can see a silver door that says 'Kitchen,' and directly to the north 
of you, an 'unlabeled' pink door. You also notice that under you, in the floor 
there's a basement hatch (a floor door).  """},


    # dungeon
    'dungeon': {'name': 'a dungeon room', 

    'ways_to_move': {'up': {'door': 'floor door', 'room': 'front'}}, 
    
    'contents': {'cat food': 'unfixed', 'chain': 'fixed', 'table': 'fixed', 'pipet': 'unfixed',
                 'glass': 'fixed', 'potion rack': 'fixed', 'spoon': 'unfixed', 'zombie': 'unfixed',
                 'floor door': 'fixed'}, 
    
    'non_players': {'zombie': {'response': 'grunts.'}}, 
    
    'devices': {'floor door': {'status': 'open', 'condition': 'unlocked'}},

'text': """You are standing in the middle of a small room. Beside you, you can 
see a table with a old test tube rack on it. On the floor you see spilt 
potions, broken glass stabbed into the floor and some dark stains on the 
floor. The room gives you a shiver. You can also see a zombie in the back of 
the room sleeping. On the roof of the room, you see the basement hatch. """},


    # living room
    'living': {'name': 'a living room', 

    'ways_to_move': {'east': {'door': 'green door', 'room': 'front'}}, 

    'contents': {'pearl necklace': 'unfixed', 'bookshelf': 'fixed', 'cloth': 'fixed', 'couch': 'fixed',
                 'scorpion': 'unfixed', 'witch': 'unfixed', 'drape': 'fixed', 'green door': 'fixed'},
    
    'non_players': {'scorpion': {'response': 'doesn\'t reply.'},
                    'witch' : {'response': 'shouts \"where is my wand!?\"', 'wants': 'wand', 'give': 'tiny key',
                               'deedResponce': '\nThe witch takes out a tiny key from her pocket and hands it over to you.'}}, 
    
    'devices': {'green door': {'status': 'open', 'condition': 'unlocked'},
                'drape': {'status': 'open'}, 'window': {'status': 'open'}},

'text': """The temperature in the living room is a few degrees lower than the 
rest of the house and you can see your breath. At the back of the room you see 
a see-through drape being blown by a slight breeze coming in through an open
window. You see a forest through the window. In the room you see an old white
couch. The cloth that covers the couch lies next to the couch on the floor. A
giant scorpion is sitting on it. You can also see an old empty bookshelf. To
the east is a green door. """},
         

    # kitchen
    'kitchen': {'name': 'a kitchen', 
    
    'ways_to_move': {'west': {'door': 'silver door', 'room': 'front'}}, 
    
    'contents': {'cat food': 'unfixed', 'maid': 'unfixed', 'stove': 'fixed', 'dough roller': 'unfixed',
                 'fridge': 'fixed', 'the scream': 'fixed', 'silver door': 'fixed'}, 
    
    'non_players': {'maid': {'response': 'glares.'}}, 
    
    'devices': {'silver door': {'status': 'open', 'condition': 'unlocked', 'key': 'silver key'},
                'fridge': {'status': 'closed', 'condition': 'unlocked', 'contents': ['bone', 'fork']},
                'stove': {'status': 'closed', 'condition': 'locked'}},

'text': """You are in the kitchen. You first see a fridge, there are pools and stains of 
blood all over it. You can smell fire. The smell of smoke is filling up your 
lungs. You see bursting flames inside of the stove. You also notice a picture 
picture frame of the scream staring at you from above the stove. It's lit on 
fire but it's not burning into ashes. In the back of the room, there's a sad 
looking maid. To the west is a silver door. """},


    # bedroom
    'bedroom': {'name': 'a bedroom', 
    
    'ways_to_move': {'north': {'door': 'decaying door', 'room': 'stairway'},
                     'south': {'door': 'pink door', 'room': 'front'}}, 
    
    'contents': {'sheet': 'fixed', 'bed': 'fixed', 'painting': 'fixed', 'carpet': 'fixed',
                 'doll': 'unfixed', 'vanity': 'fixed', 'holdable mirror': 'unfixed', 'chest': 'fixed',
                 'decaying door': 'fixed', 'pink door': 'fixed'}, 
    
    'non_players': {'doll': {'response': 'angrily whispers, \"I want my music box.\"', 'wants': 'music box', 'give': 'blue locket',
                             'deedResponce': '\nThe doll pulls out-from the inside of one of her eye sockets-a blue locket and throws it into your hands.'}}, 
    
    'devices': {'decaying door': {'status': 'close', 'condition': 'unlocked'},
                'pink door': {'status': 'open', 'condition': 'unlocked'},
                'chest': {'status': 'closed', 'condition': 'locked', 'contents': ['music box'], 'key': 'tiny key'}},

'text': """You are standing near a king sized bed has been covered in a 
thick coating of dust. The sheet of the bed appears to have been stained with 
blood. You glimpse something move. On the head of the bed, you see a doll with 
missing eyes that gives you the impression of being scanned. On the wall behind 
the bed, you see a painting of a sad family. Beside the bed, you spot a chest 
sitting on an old stained wood vanity. To the north is a decaying door. To the 
south, a pink door. """},


    # stairway
    'stairway': {'name': 'a stairway', 
    
    'ways_to_move': {'up': {'room': 'attic'},
                     'south': {'door': 'decaying door', 'room': 'bedroom'}}, 
    
    'contents': {'silver key': 'unfixed', 'decaying door': 'fixed'}, 

    'non_players': {},
    
    'devices': {'decaying door': {'status': 'open', 'condition': 'unlocked'}},

'text': """You are standing on bottom of a creaky staircase. You discern a 
termite-infestation because the wooden contraptions are rotting and a few 
stairs have parts missing. Going straight up the stairs leads into to the 
attic. To the south is the bedroom. """},


    # attic
    'attic': {'name': 'a attic', 
    
    'ways_to_move': {'down': {'room': 'stairway'}}, 
    
    'contents': {'elf': 'unfixed', 'ghost': 'fixed'}, 
    
    'non_players': {'elf' : {'response': 'mumbles, \"I\'ve been waiting for you. Give me my blue locket.\"', 'give': 'empty flask', 'wants': 'blue locket',
                             'deedResponce': '\nThe gloomy looking elf makes appear a empty flask into your hands with the flick of his hand.'}, 'ghost': {'response': 'yells boo!'}},

'text': """You enter what seems to be a deserted and empty wooden room. But then 
you see a ghost materialize right in front of your very eyes. You see 
what seems to be a gloomy elf dressed in rags. The attic has stairs 
leading down and out of the attic. """},

    
    # street
    'street': {'name': 'a street', 
    
    'ways_to_move': {'north': {'door': 'gate', 'room': 'courtyard'}}, 
    
    'contents': {'cat': 'unfixed'}, 
    
    'non_players': {'cat': {'response': 'meows.', 'wants': 'cat food'}},
    
    'devices': {'gate': {'status': 'open', 'condition': 'unlocked'}},

'text': """You have been teleported out. You are standing on a dark and gloomy 
street. It’s very foggy. Beside you, you can just make out a street sign saying 
“Godwinson's Hollow”. To the north of you, you can make out the open gates to 
the courtyard of blood-curdling tall wooden house. You are happy because you
have escaped with a potion in hand. """},



# drinkable devices to find in the haunted house and what they do
'drinkableDevices': {'sky-blue potion': 'You are suddenly invisible and you feel powerful',
                     'coal-black potion': 'You see a really bright light. It\'s very blinding. A man is in front of you.',
                     'golden potion': 'You are surrounded by glittering gold. You are rich!'},



# descriptions of room items that make health drop when item touched
'losingItems': {'cat': {'points': 5, 'statement': 'Cat scratches your hands.'},
                'elf': {'points': 5, 'statement': 'The elf kicks your foot.'},
                'maid': {'points': 5, 'statement': 'The maid slaps you.'},
                'moss': {'points': 10, 'statement': 'That\'s poisonous and has given you a rash.'},
                'glass': {'points': 10, 'statement': 'The glass has entered and cut your skin.'},
                'scorpion': {'points': 50, 'statement': 'The scorpion has stung your hand and you feel the poison on the inside of your hand.'},
                'zombie': {'points': 100, 'statement': 'You\'re hand got bitten off.'},
                'dog': {'points': 20, 'statement': 'The dog has fleas and fleas have now infested your body.'},
                'witch': {'points': 200, 'statement': 'The witch screams, \"FOOL!" \n You hear her curse you. \n You see a green flash of light. \n You see your body lying dead on the floor.'},
                'doll': {'points': 10, 'statement': 'The doll bites your fingers.'}},
  


# game commands
  'help' : """
//////////////////////////////////////
  !At any time for help print: help!
!At any time to quit print: q or quit!
//////////////////////////////////////


 Possible game commands:

-To move print: {direction}
... The possible directions to move are: north, south, east, west, up, down
-To get health print: health
-To look at inventory print: inventory
-To look at room print: look
-To pick something up print: get {name of object}
-To drop something from your inventory print: drop {name of object}
-To unlock something print: unlock {name of door}
-To lock something print: lock {name of door}
-To open something print: open {name of item/device}
-To close something print: close {name of item/device} or close
-To talk to a non-player character print: say hi to {name of creature/character}
-To give something away to a non-player character print: give
{name of non-player character} {name of item}
-To quit print: q or quit
-To get help print: help
-To drink something print: drink {name of drink}


* Note that; it is not possible to pick up many items in one turn. 
For example, when entering a command, you will need to type in; get 
chain, instead of; get chains.

* Make sure that words in commands have 1 space in between *
""",



# objective of player in the haunted house rooms
  'objective': """
  Objective:
In the game, you are in a haunted house in Godwinson’s Hollow. The game will 
contain a total of 9 rooms for you to explore. You are in the haunted house 
to get one of the following: a sky blue potion-which will make you invincible 
but invisible forever, a coal black potion-which will kill you and send you 
to heaven, or a golden potion-which will create a lifetime supply of gold. 
You have heard that a ghost in the haunted house has the items you seek. When 
you get a magical potion, you will need to drink it in order to win. During 
your quest to get a magical item, if you pick up a dangerous item or if you 
insult a non-player character, you will lose health points or lose the game.
You will lose if you lose all 200 health points, so take care of them! """,



# what the haunted house incorporates
  'incorporates': """What you will find in the game:
In the haunted house, you will find that there will be items to be picked
up and to be kept in your inventory. You will see doors-with some of them 
being locked-that will lead to rooms. You will find that there will be items 
that will sometimes need opening. You will find that you will lose points if 
you do something bad. You will find that there will be non-player characters 
in these rooms and that these players can want something from you, when you
say hi to them. Sometimes, they will give you something in return for the
good deed of giving what they want. Finally, if you receive a drinkable
magical potion; drink it."""}



# ghost movements in the house that user will notice
ghostMovements = ["You hear a continuous echo.",
                  "You feel a sense of dread grasp you.",
                  "You suddenly feel cold.",
                  "You look up and see a thick mist.",
                  "The mist seems to be following you and moaning.",
                  "The mist disappears.",
                  "You think you hear something directly overhead of you.",
                  "The noise you heard turns into a scraping noise, like something being dragged along the floor.",
                  "The noise you heard stops.",
                  "You see the mist you saw earlier but now it's darker, and red.",
                  "You hear a moan increasing in pitch and volume and it's coming closer!",
                  "Now you hear a dreadful silence.",
                  "All the sudden you see a mist fly right through you and you hear a glass shattering high pitched screech!",
                  "All sound is gone. It's DEAD silent."]



health = 200  # starting health

directions = ['north', 'south', 'east', 'west', 'up', 'down']  # ways to move

current_room = rooms['courtyard']  # starting room

cat_current_room = rooms['street']   # starting cat room

carrying = ['pants']   # starting inventory

ghostMessage = 0  # starting ghost message count

quit_ = False  # make variable quit False




# waits for user input after printing result
def wait():
    input('\nPress enter to continue...\n') # user enters anything and game continues



# will get input from user and return it
def getInput():

    # get user input
    return input('\n> ').strip()



# print possible game commands
def help_(command):

    if command[0:4] == 'help':   # if first 4 characters in command spell help
        print(rooms['help'])   # print possible game commands
        wait()

    else:
        return False



# gather objects 
def getItems(command, health):

    item = command[4:]   # make item equal to characters that come after get in command

    if item in current_room['contents']:   # if item in player's room
        
        if current_room['contents'].get(item) == 'unfixed':  # if it's value is unfixed
            
            if item in rooms['losingItems']:   # if item in losing items list
                losingPoints = rooms['losingItems'][item]['points']  # get points to lose
                health -= losingPoints   # subtract the item's points from player's health

                print('-{} health'.format(losingPoints))   # print health points lost
                print("")
                print(rooms['losingItems'][item]['statement'])   #  print statement why points were lost
                return health   # return health to change it throughout program

            else:
                current_room['contents'].pop(item)   # remove item from room contents
                carrying.append(item)  # add item to player's inventory
                print('taken')

        else:
            print('\nThat is fixed in place.')

            if item in rooms['losingItems']:   # if item in losing items
                losingPoints = rooms['losingItems'][item]['points']  # get points of item
                health -= losingPoints   # remove points from user's health

                # messages
                print('-{} health'.format(losingPoints))  # how many points lost
                print("")
                print(rooms['losingItems'][item]['statement'])   # why health was lost
                return health   # return health to change it throughout program
            
    else:
        # item not in room
        print("\nI don't see that here.")
            

        
# print user's health
def printHealth():

    if command == 'health':  # if command is health
        print('\n You\'re health is at {}.'.format(health))   # print health

    else:
       return False



# get rid of objects
def dropItems(command):

    if command.split()[0] == 'drop':   # if commands first word is drop
        item = command[5:]   # make the characters following drop, the item

        if item in carrying:

            # append that item in player's room contents as unfixed
            current_room['contents'].setdefault(item, 'unfixed')

            carrying.remove(item)  # remove that item from inventory
            print('dropped')

        else:
            # item not in inventory
            print("\nYou aren't carrying that.")

    else:
       return False



# print user's inventory
def viewInventory(command):

    if command == 'inventory':   # if command is inventory

        if len(carrying) == 0:   # if inventory empty
            print('\nYou aren\'t carrying anything.')

        else:
            carrying.sort()  # sort inventory in alphabetical order
            print(', '.join(carrying))   # print inventory nicely to user by printing the list in one line

    else:
       return False



# talking to non-player characters
def chat(command):

    if command[0:10] == 'say hi to ':   # if command starts with 'say hi to'
        npc = command[10:]   # make the characters after 'say hi to' the name of the non-player character

        if npc in current_room['non_players']:   # if non-player character in player's room

            # print non-player character response by fetching response from character's dictionary
            print("\nThe {} {}".format(npc, current_room['non_players'][npc]['response']))

        else:
            # non-player character not in room
            if npc not in current_room['contents']:
                print('\nYou do not see {} in current room.'.format(npc))
            else:
                print('\nNothing.')

    else:
        return False



# opening devices
def openDevice(command):

    if command.split()[0] == 'open':   # if first word in command is open
        device = command[5:]   # the proceeding characters after open will represent device

        if device in current_room['devices']:  # if device in player's room
            
            if current_room['devices'][device].get('condition') == 'unlocked':  # if it is unlocked
                
                if current_room['devices'][device].get('status') == 'closed':  # and it is closed
                    current_room['devices'][device]['status'] = 'open'   # make device's status open
                    print('opened')

                
                    # if there are contents in the device
                    if 'contents' in current_room['devices'][device]:  # else, it could be a door

                        # loop printing contents of device
                        while True:
                            contents = []  # empty list to add contents of device

                            if current_room['devices'][device]['contents']:  # if items in device's contents
                                print("\nIn the {} you see: ".format(device))  # print items

                                # append device's contents to list 'contents'
                                for item in current_room['devices'][device]['contents']:
                                    contents.append(item)
                                
                                contents.sort()  # sort list
                                print(', '.join(contents))   # print content nicely in one line to user
                            
                            else:
                                print('\nThe {} is empty.'.format(device))    # say it's empty


                            # loop getting command
                            while True:
                                s = getInput()   # get input with function
                                request = s.lower()  # call input request and make it all lowercase characters
                
                                if request != '':  # if request was given
                                    if len(request.split()) >= 2 and request.split()[0] != 'close':  # request at least two words long:
                                        
                                        if request.split()[0] == 'get':  # if request is to get something 
                                            item = request[4:]  # make next characters, the item
                                            
                                            # if item in device contents
                                            if item in current_room['devices'][device]['contents']:
                                                carrying.append(item)  # append item to player's inventory
                                                current_room['devices'][device]['contents'].remove(item)   # remove item from device's contents
                                                print('taken')
                                            
                                            else:
                                                print("\nI don't see that in the {}.".format(device))

                                        # if request is to drop item, tell user it's impossible
                                        elif request.split()[0] == 'drop':   # if commands first word is drop
                                            item = command[5:]   # make the characters following drop, the item

                                            if item in carrying:
                                                print('\nThe item appears immediately back into your inventory. You hear an eerie voice saying, \"the {} only accepts items from master.\"'.format(device))
                                                
                                            else:
                                                print("\nYou aren't carrying that.")

                                        else:
                                            # invalid request
                                            print('\nI don\'t understand that command.\n\nYou have a chest opened and in operation. Close the chest to leave it or to do something else.')
                                    
                                    # requests that are at least a word long below

                                    elif request == 'close {}'.format(device) or request == 'close':   # if request is to close device
                                        current_room['devices'][device]['status'] = 'closed'   # make device closed
                                        print('closed')
                                        return 'room'
                                    
                                    elif request == 'look':
                                        break  # go back to printing room contents
                                    
                                    elif request == 'inventory': 
                                        viewInventory(request)  # call function that views inventory
                                    
                                    elif request[0:4] == 'help':   # call function that prints possible commands and help
                                        help_(request)

                                    elif request== 'q' or request== 'quit':
                                        return 'fool'   # return fool because that causes game to stop

                                    else:
                                        # invalid request
                                        print('\nI don\'t understand that command.\n\nYou have a chest opened and in operation. Close the chest to leave it or to do something else.')

                                else:
                                    # empty string
                                    print('I beg your pardon.')
                else:
                    # device not closed
                    print('\nThat\'s already open.')
            else:
                # device not unlocked
                print('\nThat\'s locked.')
        
        elif device in current_room['contents']:    # if item exists in room but not openable
            print("\nYou cannot open that.")
        
        else:
            # device not in room
            print("\nI don't see that here.")
    else:
       return False



# closing devices
def close(command):

    if command.split()[0] == 'close':  # if first word of command is close
        device = command[6:]   # make proceeding characters device

        if device in current_room['devices']:  #  if device in player's room
            if current_room['devices'][device].get('status') == 'open':  # if status is open
                current_room['devices'][door]['status'] = 'closed'   # make the status closed
                print('closed.')

            else:
                # device not opened
                print("\nThat's already closed.")
        
        elif device in current_room['contents']:   # if device in room contents but not closeable
            print("\nThat\'s not closeable.")

        else:
            # device not in room
            print("\nI don't see that here.")
    else:
       return False

       
       
# unlocking devices
def unlock(command):

    if command.split()[0] == 'unlock':   # if 1st word in command unlock
        device = command[7:]   # make characters after unlock device

        if device in current_room['devices']:  # if device in player room's devices
            if current_room['devices'][device].get('condition') == 'locked':   # if device's condition locked
                if current_room['devices'][device].get('key') in carrying:   # if device's key in player's inventory
                    current_room['devices'][device]['condition'] = 'unlocked'  # make device's condition unlock
                    print('unlocked')

                else:
                    # user missing key
                    print('\nYou don\'t have the right key.')
            else:
                # device not locked
                print('\nThat\'s already unlocked.')
        
        elif device in current_room['contents']:   # if device not in room's devices but in contents
            print("\nThat\'s not a locked item.")
        
        else:
            # device not in room
            print("\nI don't see that here.")
    else:
       return False

        

# locking devices
def lock(command):

    if command.split()[0] == 'lock':   # if 1st word in command lock
        device = command[5:]   # make characters after lock device

        if device in current_room['devices']:  # if device in player room's devices
            if current_room['devices'][device].get('condition') == 'unlocked':   # if device's condition unlocked
                if current_room['devices'][device].get('status') == 'open':   # if device's status open

                    current_room['devices'][door]['status'] = 'closed'   # make device's condition closed
                    print('(First closing the {}.)'.format(device))  # print that device is being closed first
              
                if current_room['devices'][device].get('key') in carrying:   # if device's key in player's inventory

                    current_room['devices'][device]['condition'] = 'locked'  # make device's condition locked
                    print('locked')

                else:
                    # user missing key
                    print('\nYou don\'t have the key.')
            else:
                # device not unlocked
                print('\nThat\'s already locked.')
        
        elif device in current_room['contents']:   # if device not in room's devices but in contents
            print("\nThat\'s not a lockable item.")
        
        else:
            # device not in room
            print("\nI don't see that here.")
    else:
       return False



# giving items to non-player characters
def give(command):

    if command.split()[0] == 'give':   # if 1st word in command is give
        npc = command.split()[1]   # make 2nd word non-player character

        if npc in current_room['non_players']:   # if non-player character in player's room
            item = command[len(npc)+6:]  # make item the characters proceeding non-player character in command

            if item in carrying:   # if item in inventory
                
                if current_room['non_players'][npc].get('wants') == item:  # if non-player character wants that item
                    carrying.remove(item)  # remove given item from player's inventory
                    print('given')

                    if current_room['non_players'][npc].get('give', False) != False:   # if non-player character will give something in return
                        item_in_return = current_room['non_players'][npc]['give']  # get the item in return
                        carrying.append(item_in_return)  # append that item in player's inventory
                        
                        # print non-player character response to deed/how they give you another item in return
                        print(current_room['non_players'][npc]['deedResponce'])


                        if 'empty flask' in carrying:  # if non-player character (the ghost) gave an empty flask

                            patience = 4  # make ghost's starting patience with user 4

                            # loop printing ghost's message
                            while True:
                                print("""
The ghost makes appear a sky-blue potion, a coal-black potion and a 
golden potion in the air on top of him. The ghost asks, "which potion 
do you want to fill your flask with? You must chose quickly. I don't 
like waiting!":

0. Say nothing
1. Say sky-blue potion
2. Say coal-black potion
3. Say golden potion

                                """)

                                # get choice
                                choice = input('> ')
                                print()


                                # if user didn't chose a potion or ghost's patience with user ran out
                                if choice == '0' or patience == 0:
                                    print('You have insulted the spirits, you will not be asked to get the items again.')
                                    return 'fool'  # return that user was a fool and failed the game
                                    break

                                # for user's potion choice, append new potion and remove empty flask into/from inventory and end loop/function:

                                elif choice == '1':
                                    carrying.append('sky-blue potion')
                                    carrying.remove('empty flask')

                                    print('You\'re given sky-blue potion.\n\nYou now have a sky-blue potion in your inventory.')
                                    break
      
                                elif choice == '2':
                                    carrying.append('coal-black potion')
                                    carrying.remove('empty flask')
                                    
                                    print('You\'re given coal-black potion.\n\nYou now have a coal-black potion in your inventory.')
                                    break
  
                                elif choice == '3':
                                    carrying.append('golden potion')
                                    carrying.remove('empty flask')

                                    print('You\'re given golden potion.\n\nYou now have a golden potion in your inventory.')
                                    break
                                
                                else:  # if user's command invalid
                                    print("What!?")
                                    patience -= 1   # subtract 1 from ghost's patience

                else:
                  # print what non-player character wants and that they don't take what player tried to give them
                  print("\nThe {} {}\nThe {} doesn\'t take it.".format(npc, current_room['non_players'][npc]['response'], npc))
            else:
                # item not in inventory
                print('\nYou aren\'t carrying that.')
        else:
            # non-player character not in room
            print("\nI don't see that {} person here.".format(npc))
    else:
        return False



#  drinking devices
def drink(command):

    if command.split()[0] == 'drink':   # if 1st word in command is drink
        device = command[6:]   # make characters after drink device

        if device in carrying:
            if device in rooms['drinkableDevices']:  # if device in part of game's drinkable devices
                print('Potion is sipped')
                print("")

                print(rooms['drinkableDevices'][device])   # print what happens when device is drunk
                return 'won'   # return that goal has been met and user won
            
            else:
                # device not drinkable
                print("\nThat\'s not drinkable.")
        else:
            # device not in inventory
            print("\nYou aren\'t carrying that.")
    else:
        return False



# moving the cat around the house
def cat(cat_current_room):

        ways_to_go = []
    
        for direction in cat_current_room['ways_to_move']:   # for possible directions in cat's current room
            ways_to_go.append(direction)   # add them in 'ways to go' list

        direction = random.choice(ways_to_go)  # chose a random direction from list

        catRoom = cat_current_room['ways_to_move'][direction]['room']

        if cat_current_room == current_room:   # if cats room was the same as player's current room
            
            # print message saying cat is leaving
            print("\nA cat has entered the {} area.".format(catRoom))

        cat_current_room['non_players'].pop('cat')   # remove cat room's non-player characters
        cat_current_room['contents'].pop('cat')  # remove cat from room's contents

        cat_current_room = rooms[catRoom]  # switch cat's current room

        # add cat to new room non-player characters and contents
        cat_current_room['non_players'].setdefault('cat', {'response': 'meows.', 'wants': 'cat food'})
        cat_current_room['contents'].setdefault('cat', 'unfixed')
        
        
        # if cat's new room is the same as player's
        if cat_current_room == current_room:
            print("\nA old looking cat has joined you.")   # tell them the cat has joined in
            
        return cat_current_room  # return cat's current room to change the room throughout program





"""
Main Menu Below
"""

if __name__ == '__main__':

    # intro
    print("""

█░░█ █▀▀█ █░░█ █▀▀▄ ▀▀█▀▀ █▀▀ █▀▀▄   █░░█ █▀▀█ █░░█ █▀▀ █▀▀
█▀▀█ █▄▄█ █░░█ █░░█ ░░█░░ █▀▀ █░░█   █▀▀█ █░░█ █░░█ ▀▀█ █▀▀
▀░░▀ ▀░░▀ ░▀▀▀ ▀░░▀ ░░▀░░ ▀▀▀ ▀▀▀░   ▀░░▀ ▀▀▀▀ ░▀▀▀ ▀▀▀ ▀▀▀
          
           .-.      
          (o o)     
     Boo! | O \ 
           \   \    
            `~~~'       
    """)

    # loop menu to user
    while True:
        print("""
    Enter a number to choose one of the following options:
    0. Play the Haunted House game
    1. Read what the interactive adventure game has in store for you
    2. Read the objective of game and how to win or lose
    3. Read the possible game commands (MOST IMPORTANT)
    4. Exit
        """)


        # get choice
        choice = input('> ')
        print()

        # give user the instructions to the game
        if choice == '0':
            # repeat key information of game
            print("\nYou are determined to find one of the magical potions.\n\nYou have 200 health.\n\nYou teleport yourself into a haunted house location.")
            break   # breaks menu loop and starts game

        elif choice == '1':
            print(rooms['incorporates'])   # print what the game/rooms incorporates
      
            wait()
      
        elif choice == '2':
            print(rooms['objective'])  # print the game objective
        
            wait()
    
        elif choice == '3':
            print(rooms['help'])  # print game commands and helpful points
      
            wait()
    
        elif choice == '4':
            print ('Goodbye!')
            quit_ = True   # so the game won't enter the game loop later on
            break   # finishes loop
      
        else:
            print('Input is invalid.')



'''
Haunted House Game Below
'''

# start game and continue game while quit variable is equal False
while quit_ == False:

    # display current location
    print('\nYou are in {}: '.format(current_room['name']))   # print the current room's name
    print(current_room['text'])  # print the room's text/description


    cat_current_room = cat(cat_current_room)   # show cat movements


    if current_room['contents']:   # if room has contents
        print('\nIn the room there are: {}'.format(', '.join(current_room['contents'])))   # display room contents


    # loop getting command from user
    while True:

        command = getInput()   # get input with function and call it command
        command = command.lower()  # make command all lowercase characters

   
        # movement
        if command in directions:  # if command a direction
          
            if command in current_room['ways_to_move']:  # if command in ways to move for room

                if 'door' in current_room['ways_to_move'][command]:  # if a door in the direction
                    door = current_room['ways_to_move'][command]['door']   # get name of door

                    if current_room['devices'][door].get('condition') != 'locked':  # if door for the room unlocked
                        if current_room['devices'][door].get('status') == 'closed':  # if door closed

                            current_room['devices'][door]['status'] = 'open'   # open it
                            print('(First opening {}.)'.format(door))  # tell user door it is first being opened
                    
                        # change the player's current room and print next room information
                        current_room = rooms[current_room['ways_to_move'][command]['room']]
                        break
                
                    else:
                        print("\nThat\'s locked.")

                else:
                    # change the player's current room and print next room information
                    current_room = rooms[current_room['ways_to_move'][command]['room']]
                    break
                    
            else:
                # bad movement
                print("You can't go that way.")


        # quiting            
        elif command == 'q' or command == 'quit':

            # exit game message
            print('\n\nGoodbye!')

            # quit game
            quit_ = True    # make quit true to break the loop that prints room
            break  # breaks the loop that gets command 


        # looking  
        elif command == 'look':
            break  # print room information again by breaking getting command loop

        
        # call rest of functions that check command 
        # False will be added in 'functionResults' if command wasn't for that function purpose
        # None will be added in 'functionResults' if command was for the function
        elif command != '':
            functionResults = []   # set an empty list to store game functions response


            # call functions for one word commands first
            functionResults.append(viewInventory(command))
            functionResults.append(help_(command))
            functionResults.append(printHealth())


            # check if command is at least 2 words long so functions won't crash when expecting a second word
            if len(command.split()) >= 2:
                
                # the getItem function will return points instead of None and False
                # this part will take care of that problem
                if command.split()[0] == 'get':   # if command is to get an item
                    
                    functionResults.append(None)   # append None in function results
                    newPoints = getItems(command, health)  # get new player's health points after getting item
            
                    if newPoints != None:  # if new player's points changed (and were given)
                        health = newPoints   # make them the player's health

                        if health <= 0:  # if health have fallen below 1
                            print('You\'re dead X_X\nYou have no more health. You have lost. \n\nGoodbye.')
                            quit_ = True   # make 'quit_' True to quit game loop
                            break  # break getting command loop to quit game


                # call the rest of the functions at least 2 words long:
                functionResults.append(dropItems(command))
                functionResults.append(openDevice(command))
                functionResults.append(unlock(command))
                functionResults.append(lock(command))
                functionResults.append(close(command))
                functionResults.append(drink(command))


                # for at least 3 words long commands, check if user want to give something
                if len(command.split()) >= 3:
                    functionResults.append(give(command))
                
                # for atleast 4 words long commands, check if user want to talk to non-player character
                if len(command.split()) >= 4:
                    functionResults.append(chat(command))


            # from all these functions, if a function had no returned because function went through
            # print what happened after act was done
            if None in functionResults:
                
                if ghostMessage < 14:  # if ghost message number a possible number for how many ghost movements exist
                    print("")
                    print(ghostMovements[ghostMessage])   # print message for that number
                    
                    ghostMessage += 1  # add 1 to ghost message number to change it to the next
                    
                else:
                    ghostMessage = 0   # make ghost message number 0 to restart the message cycle
                    
                cat_current_room = cat(cat_current_room)   # show new cat movements

            # special returned values for game functions below

            # room description needs reprinting
            elif 'room' in functionResults:
                break  # print room information again

            # won
            elif 'won' in functionResults:   # if user drank potion

                if 'coal-black potion' not in carrying:    # if player does not have potion that kills
                    print("")
                    print(rooms['street']['text'])   # bring user to street because they escaped

                else:
                    print("\nYou wonder if your dead.")  # give them a hint that potion has killed them

                # the user has achieved the goal of game and has won
                # end game
                print("\nThe game has ended.")
                quit_ = True
                break

            # quit/lose
            elif 'fool' in functionResults:  # if user didn't get a potion

                # end game message
                print("\nGoodbye. \n\nYou have lost.")

                # end all looping
                quit_ = True
                break

            else:
                # bad command
                print("\nI don't understand that command.")

        else:
            # no command
            print('I beg your pardon?')
      
