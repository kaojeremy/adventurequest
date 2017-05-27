import items, world, tiles
import random

class Player:
	
	victoryFlag = False

	def __init__(self,hp,inventory,x,y):
		# This function initializes the player object.
		# Inputs: hp (integer)
		#	      gold (integer)
		#		  exp (integer)
		#		  inventory (list)
		#	      x (integer)
		#	      y (integer)
		self.hp = hp
		self.inventory = inventory
		self.x = x
		self.y = y

	def move(self,dx,dy):
		# This function moves the player character.
		# Check if player would be moving into a blocked room
		currentRoom = world.tile_at(self.x,self.y)
		if hasattr(currentRoom,'room_blocked'):
			if currentRoom.room_blocked == True and dx == currentRoom.block_dx and dy == currentRoom.block_dy:
				print("\nThis way is blocked! You cannot move forward.")
			else:
				self.x += dx
				self.y += dy
		else:
			self.x += dx
			self.y += dy

	def move_north(self):
		self.move(dx=0,dy=-1)

	def move_south(self):
		self.move(dx=0,dy=1)

	def move_west(self):
		self.move(dx=-1,dy=0)

	def move_east(self):
		self.move(dx=1,dy=0)

	def print_inventory(self):
		print("\nInventory:\n")
		for item in self.inventory:
			print(item)
		best_weapon = self.get_strongest_weapon()
		print("Your best weapon is your {}.".format(best_weapon.name))

	def get_strongest_weapon(self):
		max_damage = 0
		best_weapon = None
		for item in self.inventory:
			try:
				if item.damage > max_damage:
					best_weapon = item
					max_damage = item.damage
			except AttributeError:
				pass
		return best_weapon

	def attack(self):
		room = world.tile_at(self.x,self.y) # identify current tile
		enemy = room.enemy # extract the enemy located at that room
		weapon = self.get_strongest_weapon() # get the player's weapon
		enemy.hp = enemy.hp - weapon.damage
		print("\nYou swing your {} at the {} and deal {} points of damage.".format(weapon.name,enemy.name,weapon.damage))
		if enemy.hp <= 0:
			print("\nThe {} dies! It drops:".format(enemy.name))
			for item in enemy.drops:
				print(item.name)
				self.inventory.append(item)

	def run_away(self):
		possible_moves = self.get_adjacent_tiles() # get possible moves based on tile data
		index = random.randint(0,len(possible_moves)-1) # random number between 0 and length of possible moves vector
		possible_moves[index]
		print("\nYou flee from battle!")

	def get_adjacent_tiles(self):
		moves = []
		if world.tile_at(self.x+1,self.y):
			moves.append(self.move_east())
		if world.tile_at(self.x-1,self.y):
			moves.append(self.move_west())
		if world.tile_at(self.x,self.y-1):
			moves.append(self.move_north())
		if world.tile_at(self.x,self.y+1):
			moves.append(self.move_south())
		return moves


