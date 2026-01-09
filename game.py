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
        foodchoice = input("Would you like to eat 1) beans or 2) candy?")
        if foodchoice == "1":
            if p.beans < 1:
                print("You have no beans")
                continue
            p.eatb()
            if p.hunger > 100:
                p.hunger = 100
            print(f"Hunger:{p.hunger}")
            print(f"Beans:{p.beans}")
            continue
        elif foodchoice == "2":
            if p.candy < 1:
                print("You have no candy")
                continue
            p.eatc()
            if p.hunger > 100:
                p.hunger = 100
            print(p.hunger)
            print(p.candy)
            continue
        if foodchoice != "1" or foodchoice != "2":
            print("Invalid choice error")
            continue
    elif choice == "1":
        p.hunger -= 25
        print(p.__dict__)
        days += 1
        print(f"Days:{days}")
    elif choice == "2":
        floor.randomization()
        if floor.beans > 0:
            print("You found some beans")
            p.beans += floor.beans
            floor.beans -= floor.beans
        elif floor.candy > 0:
            print("You found a candy bar")
            p.candy += floor.candy
            floor.candy -= floor.candy
        elif floor.bandages > 0:
            print("You found a bandage")
            p.bandages += floor.bandages
            floor.bandages -= floor.bandages
        elif floor.medkits > 0:
            print("You found a medkit")
            p.medkits += floor.medkits
            floor.medkits -= floor.medkits
        else:
            print("Nothing found")
    else:
        print("Invalid. Pick a valid choice.")
        continue
    print("A new floor is added to the elevator. What do you want to do?")