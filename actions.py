from collections import OrderedDict
import world, tiles

def get_available_actions(room,player):
	# Given a room and the player, this function prints out the available actions for the player to do.
	actions = OrderedDict() # initialize ordered dictionary
	print("Choose an action: ")
	if isinstance(room,tiles.EnemyRoom) and room.enemy.is_alive():
		action_adder(actions,"a",(player.attack,""),"Attack")
		action_adder(actions,"r",(player.run_away,""),"Run Away")
	else:
		if hasattr(room,'interact_player'):
			action_adder(actions,"f",(room.interact_player,player),"Interact")
		if player.inventory:
			action_adder(actions,"i",(player.print_inventory,""),"Print inventory")
		if world.tile_at(room.x,room.y-1):
			action_adder(actions,"n",(player.move_north,""),"Go north")
		if world.tile_at(room.x,room.y+1):
			action_adder(actions,"s",(player.move_south,""),"Go south")
		if world.tile_at(room.x-1,room.y):
			action_adder(actions,"w",(player.move_west,""),"Go west")
		if world.tile_at(room.x+1,room.y):
			action_adder(actions,"e",(player.move_east,""),"Go east")
	return actions


def action_adder(action_dict,hotkey,action,name):
	# This function adds an action for the player to use.
	# Inputs: action_dict (the dictionary object)
	#		  hotkey (string, the button to press)
	#	      action (the method hotkey is linked to)
	#		  name (string, name of the action)
	action_dict[hotkey.lower()] = action # add to dictionary
	action_dict[hotkey.upper()] = action # add to dictionary
	print("{}: {}".format(hotkey,name)) # print information