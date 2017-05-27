import tiles, world, items, enemies, actions
from player import Player

def play():
	print("Intro text")
	player = Player(hp=10,inventory=[items.Fists()],x=2,y=2) # initialize player object
	while True:
		room = world.tile_at(player.x,player.y)
		print(room.intro_text())
		room.modify_player(player)
		if player.hp <= 0:
			print("You have died.\n")
			break
		if player.victoryFlag == True:
			print("\nCongratulations! You win.\n")
			break
		choose_action(room,player)

def choose_action(room,player):
	# Given a room and a player, this function lists the possible actions 
	# and allows the player to select one.
	action = None
	while not action:
		available_actions = actions.get_available_actions(room,player)
		action_input = input("Action: ")
		action = available_actions.get(action_input) # from key, get the associated function
		if action and action[1] == "":
			action[0]()
		elif action and action[1] != "":
			action[0](action[1])
		else:
			print("Invalid action!\n")

play()