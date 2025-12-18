import random 
From Player import Playerstats
class elevator:
    def __init__(self, enemy):
        self.enemy = enemy
    def floorssupplies(self):
        foodchance = random.randint(1, 2)
        healschance = random.randint(1, 8)
        if healschance == 1:
            player.bandages += 1
            print("bandage found.")
        elif healschance == 2:
            player.medkits += 1
            print("medkit found")
        else:
            print("no supplies found")
        if foodchance == 1:
            foodamount = random.randint(5, 10)
            player.supplies += foodamount
            print(f"{foodamount} food found.")
        else: 
            print("no food found.")