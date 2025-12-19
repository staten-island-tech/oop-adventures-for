import tkinter as tk

root = tk.Tk()

root.title("Scary elevator")
root.geometry("2000x2000") 

label = tk.Label(root, text="SCARY ELEVATOR", font=("Creepster", 50), fg="red", bg="black")
label.pack(pady=20) 

root.configure(bg="black")
root.mainloop()
