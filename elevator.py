from Player import Player
import random 
class elevator:
    def __init__(self, food, supplies, enemy):
        self.food = food
        self.suppies = supplies
        self.enemy = enemy
    def floors(self):
        foodchance = random.randint(1, 2)
        if foodchance == 1:
            self.food += random.randint(5, 10)
            print(f"{self.food} food found.")
        else: 
            print("no food found")

elevator.floors
