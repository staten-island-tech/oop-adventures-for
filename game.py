import time
from Player import player
from Player import elevator

p = player(100, 100, 1, 1, 1, 1, 100)
days = 0
floor = elevator(0, 0, 0, 0)
print("There's something off about this place. The elevator seems to get a new floor everyday. Maybe you will find soemthing useful there that will help you escape. What do you think you should do?")


while days <= 100:
    choice = input("1) Do nothing, 2) Explore the elevator, 3)Eat food  ")
    if choice == "3":
        foodchoice = input("Would you like to eat 1) beans or 2) candy?  ")
        if foodchoice == "1":
            if p.beans < 1:
                print("You have no beans")
                continue
            p.eatb()
            print(p.hunger)
            print(p.beans)
            continue
        elif foodchoice == "2":
            if p.candy < 1:
                print("You have no candy")
                continue
            p.eatc()
            print(p.hunger)
            print(p.candy)
            continue
        if foodchoice != "1" or foodchoice != "2":
            print("Invalid choice error")
            continue
    if choice == "1":
        p.hunger -= 25
        print(p.__dict__)
        days += 1
        print(f"Days:{days}")
    if choice == "2":
        floor.randomization()
        if floor.beans > 0:
            print("You found some beans")
            p.beans += floor.beans
            floor.beans -= floor.beans
        if floor.candy > 0:
            print("You found a candy bar")
            p.candy += floor.candy
            floor.candy -= floor.candy
        if floor.bandages > 0:
            print("You found a bandage")
            p.bandages += floor.bandages
            floor.bandages -= floor.bandages
        if floor.medkits > 0:
            print("You found a medkit")
            p.medkits += floor.medkits
            floor.medkits -= floor.medkits
        if floor.beans == 0 and floor.candy == 0 and floor.bandages == 0 and floor.medkits == 0:
            print("Nothing found")
    if choice != "1" or choice != "2" or choice != "3":
        print("Invalid. Pick a valid choice.")
        continue
    print("A new floor is added to the elevator. What do you want to do?")