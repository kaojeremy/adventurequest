import items, enemies

class MapTile:
	# This is an abstract base class used as a template for all tiles in the worldspace.
	def __init__(self,x,y):
		self.x = x
		self.y = y

	def intro_text(self):
		raise NotImplementedError()

	def modify_player(self,player):
		raise NotImplementedError()

class StartingRoom(MapTile):
	# The room that the player starts in.
	def intro_text(self):
		return "\nYou are in a small cavernous chamber.\nThere appears to be only one exit.\n"

	def modify_player(self,player):
		# Room has no action on player
		pass

class LootRoom(MapTile):
	# A room in which the player finds some loot.

	loot_claimed = False

	def __init__(self,x,y,item):
		self.item = item
		super().__init__(x,y)

	def add_loot(self,player):
		player.inventory.append(self.item)
		self.loot_claimed = True

	def modify_player(self,player):
		if self.loot_claimed == False:
			self.add_loot(player)

class EnemyRoom(MapTile):
	# A room in which the player encounters an enemy.
	def __init__(self,x,y,enemy):
		self.enemy = enemy
		super().__init__(x,y)

	def modify_player(self,player):
		if self.enemy.is_alive():
			player.hp = player.hp - self.enemy.damage
			print("The {} attacks you and does {} damage. You have {} HP remaining.\n".format(self.enemy.name,self.enemy.damage,player.hp))

class EmptyCavePath(MapTile):
    def intro_text(self):
        return "\nYou make your way through a cavernous pathway.\nThere appears to be nothing of interest here.\n"
 
    def modify_player(self, player):
        #Room has no action on player
        pass

class SkeletonRoom(EnemyRoom):
	def __init__(self,x,y):
		super().__init__(x,y,enemies.Skeleton())

	def intro_text(self):
		if self.enemy.is_alive():
			return "\nYou see a spooky Skeleton.\n"
		else:
			return "\nYou see a spooky pile of bones in the corner.\n"

class OpenChestRoom(MapTile):
	loot_claimed = False

	notLooted_text = "\nYou see a chest hidden among the rocks.\n"
	looted_text = "\nYou see an open chest here.\n"

	def __init__(self,x,y,item):
		self.item = item()
		super().__init__(x,y)

	def intro_text(self):
		if self.loot_claimed == False:
			return self.notLooted_text
		else:
			return self.looted_text

	def interact_player(self,player):
		if self.loot_claimed == False:
			print("\nYou open the chest to find a {}.".format(self.item.name))
			self.add_loot(player)
			self.loot_claimed == True
		else:
			print("\nYou open the chest to find nothing.")

	def add_loot(self,player):
		player.inventory.append(self.item)
		self.loot_claimed = True

	def modify_player(self,player):
		pass

class DoorRoom(MapTile):
	room_blocked = True
	block_dx = 0
	block_dy = -1

	def intro_text(self):
		return "\nYou see a door blocking the rest of the cave.\n"

	def interact_player(self,player):
		if self.room_blocked == True and not any(isinstance(x,items.DoorKey) for x in player.inventory):
			print("\nYou try to open the door but it is futile.\nIt appears to be securely locked.")
		elif self.room_blocked == True and any(isinstance(x,items.DoorKey) for x in player.inventory):
			print("\nYou unlock the door with your Key.")
			self.room_blocked = False
		elif self.room_blocked == False:
			print("\nThe door is already unlocked.")

	def modify_player(self,player):
		pass

class VictoryRoom(MapTile):

	def intro_text(self):
		return "\nYou see a bright light in the distance."

	def modify_player(self,player):
		player.victoryFlag = True
