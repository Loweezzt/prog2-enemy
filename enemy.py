class Enemy:
    def __init__(self, health: int, attack_power: int, name: str):
        self.name = name
        self.health = health
        self.attack_power = attack_power

    def attack(self):
        print(f"{self.name} attackerar med {self.attack_power} skada")

    def take_damage(self, damage: int):
        self.health -= damage
        print(f"{self.name} tar {damage} skada och har {self.health} HP")

    def print_status(self):
        print(f"{self.name} har {self.health} HP")

slime = Enemy(10, 5, "Slajm")
goblin = Enemy(20, 10, "Goblin")
slime.print_status()
goblin.print_status()
#Klar med det innan lektionen.
#Gör som Jens gjorde på tavlan när jag har tid, hemma.
