import random

class Warrior():
    def __init__(self):
        self.health    = 100
        self.strength  = 10
        self.speed     = 5
        self.exp       = 0
        self.inventory = ["sword","10 gold pieces"]

    def potion(self):
        self.health += 20

    def attack(self, other_warrior):
        other_warrior.health -= random.randint(1, self.strength)

# CLASS INHERITANCE
class Monk(Warrior):
    # not only want to keep all the warrior attributes and methods
    # add new attributes
    def __init__(self):
        super().__init__()
        # ^^^ during our new __init__ method, we want to import all the attributes from the OLD __init__ method
        self.faith = 20
        self.strength = 5

    def lay_on_hands(self, other_warrior):
        other_warrior.health += self.faith*2

    def flurry_of_blows(self, other_warrior):
        other_warrior.health -= random.randint(1, self.strength)*3

john = Monk()
chad = Warrior()














