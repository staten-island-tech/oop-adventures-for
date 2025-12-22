import tkinter as tk
import time

global game
game = 0
def startcommand():
    start.place(x=30000, y= 700)
    intro.config(text="Loading....")
    intro.place(x=830, y=400)
    game += 1
    print(game)
    #Command here
    
root = tk.Tk()

root.title("Scary elevator")
root.geometry("2000x2000") 

intro = tk.Label(root, text="SCARY ELEVATOR", font=("Creepster", 50), fg="red", bg="black")
intro.pack(pady=20) 

start = tk.Button(root, text="Start",command=startcommand, width= 20, height=3, font=("Creepster", 20), fg="red", bg="#660000")
start.pack()
start.place(x=830, y=400)
root.configure(bg="black")
root.mainloop()
