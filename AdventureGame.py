# This is a text based adventure game I made for a class, you have to escape an abandoned mansion

done = False

inventory = []

import time

CurrentRoomID = 0

ROOMS = []
room = ["Entry Hall\nYou are past the front door of the mansion.",1,None,None,None,"You search the entry hall, looking in the closets full of coats",[]]
list.append(ROOMS,room)

room = ["Main Hall\nYou are in the main hall, you see a long red carpet in the center and plenty of bookshelves near the walls.",4,2,0,3,"You search the hall, looking under the carpet and on the bookshelves",["Red Book"]]
list.append(ROOMS,room)

room = ["East Bedroom\nYou are in one of the bedrooms, you see a large bed and a lot of paintings adorning the walls.",None,None,None,1,"You search the bedroom, looking under the bed",["Sock"]]
list.append(ROOMS,room)

room = ["West Bedroom\nYou are in one of the bedrooms, you see a large bed and a bookshelf with rare books and golden trinkets on it.",None,1,None,None,"You search the bedroom, looking under the bed and on the shelves",["Staircase Key"]]
list.append(ROOMS,room)

room = ["Dining Hall\nYou are in the dining hall, you see a long table with lit candles on it and a lot of food.",None,5,1,None,"You search the dining hall for anything useful",[]]
list.append(ROOMS,room)

room = ["Floor 1 Staircase\nYou see a staircase leading to the second floor. However, it is locked.",None,None,None,4,"You search the stairwell for anything useful",[],None]
list.append(ROOMS,room)

room = ["Floor 2 Staircase\nYou are on the 2nd floor and you see a staircase leading down",None,None,None,7,"You search the stairwell for anything useful",[],5]
list.append(ROOMS,room)

room = ["Hall 2.1\nYou are in the large hall on the second floor. It's pretty empty.",None,6,8,9,"You search the place... and as is to be expected...",[]]
list.append(ROOMS,room)

room = ["Hall 2.2\nYou are in the large hall on the second floor. It's pretty empty.",7,10,11,9,"You search the place... and as is to be expected...",[]]
list.append(ROOMS,room)

room = ["Gallery\nYou are in the gallery, many paintings and sculptures adorn it's architecture.",None,7,12,None,"You search the galley, checking behind the paintings...",[]]
list.append(ROOMS,room)

room = ["Bathroom\nYou are in the bathroom, you see a bath tub, a sink and a toilet, as to be expected.",None,None,None,8,"You search the bathroom, checking everywhere...",["Soap"]]
list.append(ROOMS,room)

room = ["Livng room\nYou are in the living room, you see a pool table, an old TV and a couch.",8,None,13,None,"You search the living room, checking between the couch cushions...",["Twenty cents and a paperclip"]]
list.append(ROOMS,room)

room = ["Kitchen\nYou are in the kitchen, you see all sorts of cooking appliances.",9,None,None,None,"You search the kitchen, looking inside the fridge...",["Jug of spoiled milk"]]
list.append(ROOMS,room)

room = ["Master Bedroom\nYou are in the master bedroom, you see a large bed in the very center and expensive artworks on the walls",11,None,None,None,"You search the bedroom, checking under the bed...",["Front door key"]]
list.append(ROOMS,room)

IDTODIRECTION = ["north","east","south","west"]

def GetRoomInformation(Id):
    Room = ROOMS[Id]
    
    print()
    print(Room[0])
    
    Word1 = "is a hallway"
    String = ""
    
    Count = 0
    
    for i in range(1,5):
        if Room[i] != None:
            Count += 1
            
            if Count >= 2:
                Word1 = "are hallways"
                String += f", {IDTODIRECTION[i-1]}"
            else:
                String += IDTODIRECTION[i-1]
    
    time.sleep(.4)
    
    print(f"\nThere {Word1} {String}.")
    
GetRoomInformation(0)

def GoToRoom(DirectionID,CRID):
    CurRoom = ROOMS[CRID]
    
    if CurRoom[DirectionID] != None:
        x = CurRoom[DirectionID]
        GetRoomInformation(x)
        return x
    else:
        print("\nYou walked into a wall and hit your head.")
        return CRID

def SearchRoom(roomid):
    Message = ROOMS[roomid][5]
    print()
    print(Message,end="...\n")
    
    time.sleep(1)
    
    itemsFound = ""
    count = 0
    
    if len(ROOMS[roomid][6]) == 0:
        print("You found nothing.")
        return
    else:
        for item in ROOMS[roomid][6]:
            count += 1
            
            inventory.append(item)
            ROOMS[roomid][6].pop(count-1)
            
            if count > 1:
                itemsfound += f", {item}"
            else:
                itemsFound += item
                
    print(f"You have found: {itemsFound}")

def UseItem(item,room,ItemID):
    if room == 5 and item.lower() == "staircase key":
        inventory.pop(ItemID)
        print("You put the key in the keyhole and...\nYou have unlocked the staircase!")
        ROOMS[5][0] = "Floor 1 Staircase\nYou see a staircase leading to the second floor."
        ROOMS[5][7] = 6
    elif item.lower() == "sock":
        inventory.pop(ItemID)
        print("You wore the sock, amazing.")
    elif item.lower() == "red book":
        print("You read the book, it has text.")
    elif item.lower() == "front door key" and CurrentRoomID == 0:
        print("\n----Congratulations!----\nYou successfully escaped!")
        return True
    else:
        print("You can't seem to find a use for this item...")

while not done:
    print("\nYour action options are:\nn,e,s,w - move\nup/down - going up or down stairs\nsearch - searches the room you are in\nuse item - use an item from your inventory\ninventory - shows you your inventory")
    UserInput = input("\nYour action: ").lower()
    if UserInput == "check":
        GetRoomInformation(CurrentRoomID)
    elif UserInput == "e" or UserInput == "east":
        CurrentRoomID = GoToRoom(2,CurrentRoomID)
    elif UserInput == "w" or UserInput == "west":
        CurrentRoomID = GoToRoom(4,CurrentRoomID)
    elif UserInput == "s" or UserInput == "south":
        CurrentRoomID = GoToRoom(3,CurrentRoomID)
    elif UserInput == "n" or UserInput == "north":
        CurrentRoomID = GoToRoom(1,CurrentRoomID)
    elif (UserInput == "up" or UserInput == "u"):
        if CurrentRoomID == 5 and ROOMS[5][7]:
            CurrentRoomID = GoToRoom(7,CurrentRoomID)
        else:
            print("\nYou can't go any higher!")
    elif (UserInput == "down" or UserInput == "d"):
        if CurrentRoomID == 6:
            CurrentRoomID = GoToRoom(7,CurrentRoomID)
        else:
            print("\nYou can't go any lower!")
    elif UserInput == "search":
        SearchRoom(CurrentRoomID)
    elif UserInput == "use item":
        ItemToUse = input("\nWhat item do you wish to use? ")
        
        inInventory = False
        ItemID = 0
        
        c = -1
        for i in inventory:
            c += 1
            if ItemToUse.lower() == i.lower():
                inInventory = True
                ItemID = c
                break
            
        if not inInventory:
            print("\nYou have no such item!")
        else:
            done = UseItem(ItemToUse,CurrentRoomID,ItemID)
        
    elif UserInput == "inventory":
        if len(inventory) == 0:
            print("\nYou are empty handed.")
        else:
            print("\nYou have:")
        for i in inventory:
            print(i)
    else:
        print("\nAction not recognized")
