import random
import time
import tkinter as tk
from Player import player
from Player import elevator
p = player(100, 100, 0, 0, 0, 0, 100)
floor1 = elevator
floor1.floorssupplies(1)
print(p.beans)
print(p.candy)