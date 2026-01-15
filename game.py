import time
from Player import player
from Player import elevator
import random
import sys

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
        p.energy -= 15
        p.hunger -= 15
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
                    SystemExit
            elif hide == "3":
                ignorechance = random.randint(1,4)
                if ignorechance < 4:
                    print("The sound seems to fade. Hopefully whatever that was will not come back.")
                    time.sleep(1)
                    print("On the bright side.......")
                    time.sleep(1)
                elif ignorechance == 4:
                    print("The foosteps grew louder. Before you can react, a dark figure approaches you. Your vision blackens out.... ")
                    time.sleep(1)
            elif hide == "4":
                print("You decide to investigate the source of the sound.")
                time.sleep(1)
                findchance = random.randint(1, 2)
                if findchance == 1:
                    print("You eventually found a bottomless hole. What do you think you should do?")
                    choice = input("1) Jump in  2) Go back to the elevator   ")
                    while choice != "1" or choice != "2":
                        if choice == "1" or choice == "2":
                            break
                        choice = input("Invalid choice. Please pick one of the following. 1) Jump in  2) Go back to the elevator   ")
                    if choice == "1":
                        deathchance = random.randint(1,3)
                        if deathchance == 1:
                            print("You got impaled by a stalagmite at the bottom. Game Over")
                            sys.exit()
                        if deathchance == 2:
                            print("You keep falling and never reached the bottom. Game Over")
                            sys.exit()
                        if deathchance == 3:
                            print("You felt your feet reach the bottom. You scan your sorroundings. It seemes like you have discovered a new dimension. What should you do?")
                            choice = input("1) Explore  2) Try to climb back up  ")
                            while choice != "1" or choice != "2":
                                if choice == "1" or choice == "2":
                                    break
                                choice = input("Invalid choice. Please pick one of the following. 1) Explore  2) Try to climb back up ")
                            if choice == "1":
                                escapechance = random.randint(1,2)
                                if escapechance == 1:
                                    print("You see some light in the distance. You run towards it and find an exit. You win!")
                                    sys.exit()
                                if escapechance == 2:
                                    print("You find yourself back at the elevator and a day seems to have passed. What do you want to do?")
                                    days += 1
                                    continue
                            if choice == "2":
                                print("You slipped and fell to your death. Game Over")
                                sys.exit()
                if findchance == 2:
                    print("You found a box of explosives. What should you do?")
                    choice = input("1) Light it up  2) Ignore it and continue walking  ")
                    while choice != "1" or choice != "2":
                        if choice == "1" or choice == "2":
                            break
                        choice = input("Invalid choice.  ")
                    if choice == "1":
                        escapechance = random.randint(1,3)
                        if escapechance == 1:
                            print("The explosives blew up a hole in the wall and you were able to climb out and escape. You win!")
                            sys.exit()
                        if escapechance == 2:
                            print("You accdientally set fire to yourself while trying to ignite the explosives.  ")
                            p.hp -= 50
                            if p.hp < 1:
                                print("Game Over")
                                sys.exit()
                            choice = input("You are nadly injured. What should you do? 1) Use bandage  2) Use Medkit  3) Ignore and go back to elevator  ")
                            while choice != "1" or choice != "2" or choice != "3":
                                if choice == "1" or choice == "2" or choice == "3":
                                    break
                                choice = input("Invalid choice.  ")
                            if choice == "1":
                                p.useb
                                continue
                            if choice == "2":
                                p.usem
                                continue
                            if choice == "3":
                                print("You weren't able to make it back to the eleavtor without a medkit or a bandage. Game Over")
                                sys.exit()
                        if escapechance == 3:
                            print("You blew up. Game Over")
                            sys.exit()
                    if choice == "2":
                        print("Dead End. You return to the elevator. However...")
                        time.sleep(2)
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
            print("You found nothing")
    else:
        print("Invalid. Pick a valid choice.")
        continue
    print("A new floor is added to the elevator. What do you want to do?")
