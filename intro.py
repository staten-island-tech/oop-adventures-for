import tkinter as tk


def startcommand():
    print("start")
    #Command here

root = tk.Tk()

root.title("Scary elevator")
root.geometry("2000x2000") 

intro = tk.Label(root, text="SCARY ELEVATOR", font=("Creepster", 50), fg="red", bg="black")
intro.pack(pady=20) 

start = tk.Button(root, text="Start",command=startcommand)
start.pack()
start.place(x=900, y=400)
root.configure(bg="black")
root.mainloop()
