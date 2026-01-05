import random
import time
import tkinter as tk
import keyboard
import intro
from elevator import elevator

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
        self.beans -= 1
        self.hunger += 40
        self.energy += 25
    def eatc(self):
        self.candy -= 1
        self.hunger += 20
        self.energy += 60
    def useb(self):
        self.bandages -= 1
        self.hp += 15
    def usem(self):
        self.medkits -= 1
        self.hp += 75
    def ignore(self):
        self.hunger -= 20
    def run(self):
        self.hunger -= 10
        self.energy -= 30
    def walk(self):
        self.energy -= 5
    def DOT(self):
        self.hp -= 10






