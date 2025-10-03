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

Goblin = Enemy(15, 100, "Goblin")
Goblin.print_status()
 
class Enemy2:
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

Goblin = Enemy2(15, 100, "Skeleton")
Goblin.print_status()