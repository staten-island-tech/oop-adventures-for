class elevator:
    def __init__(self, enemy):
        self.enemy = enemy
    def floorssupplies(self):
        foodchance = random.randint(1, 5)
        healschance = random.randint(1, 16)
        if healschance <= 4:
            player.bandages += 1
            print("bandage found.")
        elif healschance == 5:
            player.medkits += 1
            print("medkit found")
        else:
            print("no supplies found")
        if foodchance == 1:
            player.beans += 1
            print("you found canned beans.")
        elif foodchance == 2:
            player.candy += 1
            print("you found a candy bar.")
        else: 
            print("no food found.")