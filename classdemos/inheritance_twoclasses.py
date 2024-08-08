import random

# here are two "parent" classes that do not use inheritance

class Warrior:
    def __init__(self):
        self.health    = 100
        self.strength  = 10
        self.speed     = 5
        self.exp       = 0
        self.inventory = ["sword", "10 gold pieces"]

    def potion(self):
        self.health += 20

    def attack(self, other):
        other.health -= random.randint(1, self.strength)

class Wizard:
    def __init__(self):
        self.health    = 80
        self.mana      = 100
        self.intelligence = 15
        self.spells    = ["fireball", "teleport"]
        self.exp       = 0

    def cast_spell(self, spell, other):
        if spell in self.spells and self.mana >= 10:
            if spell == "fireball":
                damage = random.randint(20, 30)
                other.health -= damage
                self.mana -= 10
                print(f"Casting {spell} for {damage} damage!")
            elif spell == "teleport":
                print("Teleporting to safety!")
                self.mana -= 10
        else:
            print("Not enough mana or spell not known!")

# the new Dragonborn class inherits BOTH parent classes!

class Dragonborn(Warrior, Wizard):
    def __init__(self):
        Warrior.__init__(self)
        Wizard.__init__(self)
        self.shouts = ["force"]

    def shout(self, shout, other_person):
        if shout in self.shouts:
            print("FUS ro DAH!!!!")
            damage = random.randint(50, 100)
            other_person.health -= damage
        else:
            print("You don't know that shout!")


nord = Dragonborn()
bandit = Warrior()

print(f"The bandit has {bandit.health} health.")
nord.shout("force", bandit)
print(f"The bandit has {bandit.health} health.")
