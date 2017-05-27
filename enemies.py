import items

class Enemy:
	# The base class for all enemies in the game.
	def __init__(self,name,hp,damage,drops):
	# This function initializes the enemy.
	# Inputs: name (a string)
	#		  hp (an integer)
	#         damage (an integer)
	#		  drops (a list of objects)
		self.name = name
		self.hp = hp
		self.damage = damage
		self.drops = drops

	def is_alive(self):
	# This method returns True if enemy is dead, False otherwise.
		return self.hp > 0

class Skeleton(Enemy):
	def __init__(self):
		super().__init__(name="Skeleton",hp=10,damage=2,drops=[items.DoorKey()])