import time
from Player import player
from Player import elevator

p = player(100, 100, 0, 0, 0, 0, 100)
days = 0
floor = elevator(0, 0, 0, 0)

while days <= 100:
    print("A new floor is added to the elevator. What do you want to do?")
    choice = input("1) Do nothing, 2) Explore the elevator    ")
    if choice == "1":
        p.hunger -= 25
        print(p.__dict__)
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
    