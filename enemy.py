class Enemy:
    def __init__(self):
        self.name = "Goblin"
        self.health = 100
        self.attack_power = 15

    def print_status(self):
        print(f"Enemy: {self.name}, Health: {self.health}, Attack Power: {self.attack_power}")
