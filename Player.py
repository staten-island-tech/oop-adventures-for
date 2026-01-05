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
    def explore(self):

        elevator.floorssupplies()
    def DOT(self):
        self.hp -= 10

class elevator:
    def floorssupplies():
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


p = player(100, 100, 0, 0, 0, 0, 100)
print(p.hunger)