
import time

class Item:
	def __init__(self,name,desc,value):
		self.name = name
		self.desc = desc
		self.value = value

#---------------------------------------------------------------------
class Character:
	def __init__(self,name,charItems,charCoordinate):
		self.name = name
		self.items = charItems
		self.coordinate = charCoordinate

#---------------------------------------------------------------------

class Player(Character):
	def debug(self):
		print("Player name: %s" %p.name)
		print("Player's coordinate: %s" %p.coordinate)
		print("Player inventory: %s" %p.items)
		print("Current items in room: %s" %currentItems)


	def help(self):
		print("HELP MENU\n---------")
		print("""
move <direction>
read <item>
drop <item>
take <item>\n
For above inputs, see other synonyms for
these commands and how I validated them with for loop appends
to the 'commands' dictionary.\n
debug
inventory
""")



	def inventory(self): #Method for checking inventory
		if len(p.items) == 0:
			print("You are not holding any items")
		else:
			print("INVENTORY\n--------")
			for x in range (len(p.items)):
				print(p.items[x])


	def move(self): #Method for moving, changing player coordinate
		"""This will print out a statement in present tense FOR EFFECT,
		changing run to running and stuffs"""

		if splitAction[0] == "run":
			splitAction[0] += "ning"
		else:
			splitAction[0]+="ing"
		print(str(splitAction[0]) , str(splitAction[1]) +"...")

		#This changes coordinate depending on direction
		if "north" in action or "up" in action:
			p.coordinate[1] += 1
		elif "east" in action or "right" in action:
		 	p.coordinate[0]+=1
		elif "west" in action or "left" in action:
		 	p.coordinate[0]-=1
		elif "south" in action or "down" in action:
			p.coordinate[1]-=1

	def take(self): #Method for taking items: appending to inventory, deleting from room
		itemFound = False
		for x in range (len(splitAction)):
			if splitAction[x] in currentItems:
				"""Checks the whole string and finds if the user entered
				an item that is in the room, breaking out of the loop
				once found."""
				Places[str(p.coordinate)].remove(splitAction[x]) #delete item from room
				p.items.append(splitAction[x]) #append to inventory
				print("You took the %s" %splitAction[x])
				itemFound = True
				break

		if itemFound != True:
			print("That object is not in the room")
			"""This is printed if the string does not contain
			an item that is in the room, therefore
			 the object is not in the room, so there is
			 nothing to take"""

	def drop(self): #Method for dropping items: deleting from inventory, appending to room
		itemFound = False
		for x in range (len(splitAction)):
			if splitAction[x] in p.items:
				"""Checks the whole string and finds if the user entered
				an item that is in their inventory"""
				p.items.remove(str(splitAction[x])) #Delete item from inventory
				Places[str(p.coordinate)].append(str(splitAction[x])) #Append to room
				print("%s dropped." %splitAction[x])
				itemFound = True
				break

		if itemFound != True:
			print("That item is not in your inventory")
			"""This is printed if the string does not contain
			an item that is in the players inventory, therefore no
			item to drop"""

	def read(self): #Method that prints the items description
		itemFound = False
		for x in range (len(splitAction)):
			if splitAction[x] in p.items:
				"""Checks the whole string and finds if the user entered
				an item that is in the players inventory, breaking out of the loop
				once found."""
				print (eval(splitAction[x]).desc + "\nWorth %s gold" %eval(splitAction[x]).value)
				"""eval() reads the string as code, joining with the according method.
				 Prints description of item and according gold value on a seperate line"""
				itemFound = True
				break

		if itemFound != True:
			print("That object is not in your inventory")
			"""This is printed if the string does not contain
			an item that isn't in the players inventory."""


	def actionOnly(self): #Method when the input is only an action
		if splitAction[0] in moveActions:
 			print("I only understand you want to %s somewhere" %(splitAction[0]))
		elif splitAction[0] in takeActions or splitAction[0] in dropActions:
 			print("I only understand you want to %s something" %(splitAction[0]))



	def death(self):
		print("...\n")
		time.sleep(0.5)
		print("...\n")
		time.sleep(0.5)
		print("you were jumped by rabid monkeys and died!")
		input("PRESS ENTER TO CLOSE THE GAME")
		exit()



#----------------------------------------------------------------------------------------------
#Player Instantiation
p=Player("",[],[0,0])

#-------------------------------------------------------------------------------------------
#Item instances.
#Item name, Description, Price. Defined in class init function.
item2 = Item("item2","Description for item2",100)
note = Item("note",#2east,2north,1west.
	"""
Front of the note:
----------------------
| BINARY DIRECTIONS  |
|      0010 1110     |
|      0010 1010     |
|      0001 1011     |
----------------------

Back of the note:
---------------------
| BASE2 TO BASE16   |
|-------------------|
| E=East    B=West  |
|A,C=North D,F=South|
---------------------"""
	,0)
poop = Item("poop","Well done for making your way here! Thanks for playing the demo!",0)



#-----------------------------------------------------------------------------------------------
#Room dictionary where key = coordinate, value = list of items in room
Places ={
"[0, 0]" : [note.name,item2.name],
"[1, 2]" : [poop.name],
}
"""you need a space, for [0, 0],
Coordinate as string type as the code only compares p.coordinate with
the place coordinate, no need to manipulate dictionary key."""
deathRooms = ([0,1],[0,-1],[1,1],[1,-1],[2,-1],[3,0],[3,1],[3,2],[3,3],[3,4],[2,3],[1,3])


#--------------------------------------------------------------------------------------------
#Commands
commands={
"debug": p.debug,
"help": p.help,
"inventory": p.inventory,
}


direction = ["north","east","south","west","up","right","down","left"]
moveActions = ["walk","run","move","go","sprint"]
takeActions = ["take","grab","pick up","pickup"]
dropActions = ["drop","discard"]
readActions = ["read","examine"]

for y in range (len(readActions)):
	commands.update(dict.fromkeys({readActions[y]}, p.actionOnly))
	"""Inputs with only the readAction will go to
	the actionOnly method"""
for y in range (len(dropActions)):
	commands.update(dict.fromkeys({dropActions[y]}, p.actionOnly))
	"""Inputs with only the dropAction will go to
	the actionOnly method"""
for y in range (len(takeActions)):
	commands.update(dict.fromkeys({takeActions[y]}, p.actionOnly))
	"""Inputs with only the takeAction will go to
	the actionOnly method"""
for y in range (len(moveActions)):
	commands.update(dict.fromkeys({moveActions[y]}, p.actionOnly))
	"""Inputs with only the moveAction will go to
	the actionOnly method"""

for x in range (len(direction)):
	for y in range (len(moveActions)):
		commands.update(dict.fromkeys({moveActions[y] + " " + direction[x]}, p.move))
		"""Assigns every moveAction with every direction as a key, all linked to the p.move method."""
#---------------------------------------------------------------------------------------------
if __name__ == "__main__":
	counter = 0
	p.name = input("Welcome to the demo of Monkey Island, please enter your name.\n>>")
	print("""Hi %s. This is a demo of Monkey Island, including an open world
and item system. Type 'debug' for game information or 'help' for possible commands """ %p.name)

	while True:
		found = False #Used for recognising input
		if p.coordinate in deathRooms:
			p.death()
		if p.coordinate == [1,2] and counter == 0:
			print("You notice some poop scattered on the floor.")
			counter+=1
			#checking if the player is in a death room
		if str(p.coordinate) in Places.keys():
			currentItems = Places[str(p.coordinate)]
		else:
			currentItems = []
			"""currentItems is a list, holding the items in the room which the player is in.
			This checks through Places dictionary"""


		action = input(">>").lower()
		splitAction = action.split()
		if len(splitAction)==0:
			print ("You didn't enter anything.")
			continue

		if action in commands.keys():
			commands[action]() #Runs the function of according action in dictionary
		else:
			for x in range(len(readActions)):
				if str(readActions[x]) == splitAction[0]:
					p.read()
					found = True
			for x in range(len(takeActions)):
				if str(takeActions[x]) == splitAction[0]:
					p.take()
					found = True
			for x in range(len(dropActions)):
				if str(dropActions[x]) == splitAction[0]:
					p.drop()
					found = True
				"""commands dictionary filters out action only inputs, so if the user
				enters an action and anything else (apart from moving), these loops will
				check if the action word is the first word, calling the according method."""

			if found != True: #IF the input is not recognised
				print("I dont understand what you are saying")
