import random
import time
import tkinter as tk

class player:
    def __init__(self, hunger, energy, bandages, medkits, beans, candy, hp):
        self.hunger = hunger
        self.energy = energy
        self.hp = hp
        self.bandages = bandages
        self.medkits = medkits
        self.beans = beans
        self.candy = candy
    def eatb(self):
        if self.beans < 1:
            print("no beans")
        self.beans -= 1
        self.hunger += 40
        self.energy += 5
    def eatc(self):
        if self.candy < 1:
            print("no candy")
        elif self.candy > 0:
            self.candy -= 1
            self.hunger += 20
            self.energy += 70
    def useb(self):
        if self.bandages < 1:
            print("no bandages")
        elif self.bandages > 0:
            self.bandages -= 1
            self.hp += 15
    def usem(self):
        if self.medkits < 1:
            print("no medkits")
        elif self.medkits > 0:
            self.medkits -= 1
            self.hp += 75
    def ignore(self):
        self.hunger -= 20
    def run(self):
        self.hunger -= 10
        self.energy -= 30
    def DOT(self):
        self.hp -= 10

class elevator:
    def __init__(self, beans, candy, bandages, medkits):
        self.beans = beans
        self.candy = candy
        self.bandages = bandages
        self.medkits = medkits
    def randomization(self):
        foodchance = random.randint(1,4)
        healchance = random.randint(1,4)
        if foodchance == 1:
            self.beans += 1
        if foodchance == 2:
            self.candy += 1
        if healchance == 1:
            self.bandages += 1
        if healchance == 2:
            self.medkits += 1

skip = input("Type skip to skip cutscene. Type anythng else to view cutscene. ")
if skip != "skip":
    print("Loading.")
    time.sleep(0.5)
    print("Loading..")
    time.sleep(0.5)
    print("Loading...")
    time.sleep(0.5)
    print("Loading....")
    time.sleep(0.5)
    print("It was a dark and stormy night.")
    time.sleep(2)
    print("You need to find somewhere to stay.")
    time.sleep(2)
    print("You spot a hotel in the distance.")
    time.sleep(2)
    print("You decide to enter....")
    time.sleep(2)
    print("There was no one at the front desk.")
    time.sleep(2)
    print("The door slams behind you!")
    time.sleep(2)
    print("BAM!!!")
p = player(100, 100, 0, 0, 0, 0, 100)
floor1 = elevator(0, 0, 0, 0)
floor1.randomization()



