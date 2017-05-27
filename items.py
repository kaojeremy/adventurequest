class Item():
    # The base class for all items in the game
    def __init__(self, name, description, value):
    # This function initializes the item.
    # Inputs: name (a string)
    #         description (a string)
    #         value (an integer)
        self.name = name
        self.description = description
        self.value = value
    def __str__(self):
        return "{}\n======\n{}\nValue: {}\n".format(self.name, self.description, self.value)

class Weapon(Item):
    # The superclass for weapons.
    def __init__(self, name, description, value, damage):
        self.damage = damage
        super().__init__(name, description, value)

    def __str__(self):
        return "{}\n======\n{}\nValue: {}\nDamage: {}\n".format(self.name, self.description, self.value, self.damage)

class Sword(Weapon):
    def __init__(self):
        super().__init__(name="Sword",
                         description="A rusty old sword.",
                         value=10,damage=5)

class Fists(Weapon):
    def __init__(self):
        super().__init__(name="Fists",
                         description="Your bare hands.",
                         value=0,damage=1)

class DoorKey(Item):
    # A key that unlocks a door.
    def __init__(self):
        super().__init__(name="Key",
                         description="A mysterious key.",
                         value=0)