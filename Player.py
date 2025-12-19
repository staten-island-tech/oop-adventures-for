import random
import time
import tkinter as tk
import keyboard

class Player:
    def __init__(self, hunger, energy, bandages, medkits, foodsupply, hp):
        self.hunger = hunger
        self.energy = energy
        self.hp = hp
        self.bandages = bandages
        self.medkits = medkits
        self.foodsupply = foodsupply
    def ignore(self):
        self.hunger -= 50
    def run(self):
        self.hunger -= 15
        self.energy -= 50
    def walk(self):
        self.hunger -= 5
        self.energy -= 10
    def DOT(self):
        self.hp -= 10

class elevator:
    def __init__(self, food, supplies, enemy):
        self.food = food
        self.suppies = supplies
        self.enemy = enemy
    def floors(self):
        foodchance = random.randint(1, 2)
        if foodchance == 1:
            self.food += random.randint(5, 10)
            print(f"{self.food} food found.")
        else: 
            print("no food found")

root = tk.Tk()

root.title("Scary elevator")
root.geometry("2000x2000") 

label = tk.Label(root, text="SCARY ELEVATOR", font="Creepster")
label.pack(pady=20) 
root.mainloop()