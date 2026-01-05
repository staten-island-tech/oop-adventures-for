import tkinter as tk
import time

def update1():
    intro.config(text="Loading..")

def update2():
    intro.config(text="Loading...")

def update3():
    intro.config(text="Loading....")

def update4():
    intro.config(text="It was a dark and stormy night.", font=("Creepster", 20))
    intro.place(x=200, y=400)

def update5():
    intro.config(text="It was a dark and stormy night. You need to find somewhere to stay.")
  
def update6():
    intro.config(text="It was a dark and stormy night. You need to find somewhere to stay. You spot a hotel in the distance.")

def update7():
    intro.config(text="It was a dark and stormy night. You need to find somewhere to stay. You spot a hotel in the distance. You decide to enter....")

def update8():
    intro.config(text="There was no one at the front desk.")

def update9():
    intro.config(text="There was no one at the front desk. The door slams behind you! ")

def update10():
    intro.config(text="There was no one at the front desk. The door slams behind you! BAM!!! ")

def startcommand():
    intro.place(x=750, y=300)
    intro.config(text="Loading.")
    root.after(500, update1)
    root.after(1000, update2)
    root.after(1500, update3)
    root.after(2000, update4)
    root.after(4500, update5)
    root.after(7000, update6)
    root.after(9500, update7)
    root.after(12000, update8)
    root.after(14500, update9)
    root.after(17000, update10)
    #Command here

def skipcommand():
    intro.place_forget()

root = tk.Tk()

root.title("Scary elevator")
root.geometry("2000x2000") 

intro = tk.Label(root, text="SCARY ELEVATOR", font=("Creepster", 50), fg="red", bg="black")
intro.pack(pady=20) 
skip = tk.Button(root, text="SKIP", command=skipcommand, width= 20, height=3, font=("Creepster"))
skip.pack()
skip.place(x=1575, y=750)


root.configure(bg="black")
startcommand()
root.mainloop()
