# i used GPT in some areas :)

class Player:
    def __init__(self, name, health, power):
        self.name = name
        self.health = health
        self.power = power

    def status(self):
        print(f"{self.name} - Health: {self.health}, Power: {self.power}")

    def rest(self):
        self.power += 20
        print(f"{self.name} rested and restored 20 power.")


class Warrior(Player):
    def __init__(self, name):
        super().__init__(name, health=100, power=90)

    def attack(self, target):
        if self.power >= 30:
            target.health -= 25
            self.power -= 30
            print(f"{self.name} attacked {target.name} for 25 damage.")
        else:
            print(f"{self.name} does not have enough power to attack.")

    def special_move(self, target):
        if self.power >= 60:
            target.health -= 50
            self.power -= 60
            print(f"{self.name} used special move on {target.name} for 50 damage!")
        else:
            print(f"{self.name} does not have enough power for special move.")


class Archer(Player):
    def __init__(self, name):
        super().__init__(name, health=80, power=90)

    def attack(self, target):
        if self.power >= 20:
            target.health -= 15
            self.power -= 20
            print(f"{self.name} attacked {target.name} for 15 damage.")
        else:
            print(f"{self.name} does not have enough power to attack.")

    def special_move(self, target):
        if self.power >= 60:
            for _ in range(3):
                target.health -= 15
            self.power -= 60
            print(f"{self.name} used special move on {target.name} with 3 quick shots!")
        else:
            print(f"{self.name} does not have enough power for special move.")


class Healer(Player):
    def __init__(self, name):
        super().__init__(name, health=70, power=90)

    def heal(self, target):
        if self.power >= 20:
            target.health += 20
            self.power -= 20
            print(f"{self.name} healed {target.name} for 20 health.")
        else:
            print(f"{self.name} does not have enough power to heal.")

    def special_move(self, target1, target2):
        if self.power >= 40:
            target1.health += 20
            target2.health += 20
            self.power -= 40
            print(f"{self.name} healed {target1.name} and {target2.name} for 20 health each.")
        else:
            print(f"{self.name} does not have enough power for special move.")
p1 = Warrior("Temur")
p2 = Archer("Ilyos")
p3 = Healer("Lola")

p1.status()
p2.status()
p3.status()

p1.attack(p2)
p2.attack(p1)
p3.heal(p1)

p1.status()
p2.status()
p3.status()