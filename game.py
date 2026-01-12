import time
from Player import player
from Player import elevator
import random
from PIL import Image


p = player(100, 100, 1, 1, 1, 1, 100)
days = 0
floor = elevator(0, 0, 0, 0)
print("There's something off about this place. The elevator seems to get a new floor everyday. Maybe you will find soemthing useful there that will help you escape. What do you think you should do?")


while days <= 100:
    choice = input("1) Sleep, 2) Explore the elevator, 3)Eat food  ")
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
        enemychance = random.randint(1,2)
        if enemychance == 1:
            print("You hear something in the distance. Strange footsteps that doesn't sound human. What will you do?")
            hide = input("1)Hide in a closet 2)Run to the elavtor 3)Ignore 4)Check out the source of the sound   ")
            while hide != "1" or hide != "2" or hide != "3" or hide != "4":
                if hide == "1" or hide == "2" or hide == "3" or hide == "4":
                    break
                hide = input("Invalid choice. Pick one of the following. 1)Hide in a closet 2)Run to the elavtor 3)Ignore 4)Check out the source of the sound   ")
            if hide == "1":
                print("You hid in the nearest closet and saw a dark shadow zip pass. What was that?   ")
            elif hide == "2":
                print("You dash back to the elevator and you hear footsteps behind you.")
                time.sleep(1)
                print("You felt some claws pierce your skin. Ouch!")
                p.hp -= 75
                time.sleep(1)
                if p.hp > 0:
                    print("Luckily, you were able to make it back to the elevator alive.")
                elif p.hp <= 0:
                    print("Game Over. You got killed by a _______")
                    break
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