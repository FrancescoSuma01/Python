import tkinter as tk

def btclick1(event):
    print("OK")

def btclick2(event):
    print("Carn")

def btclick3(event):
    print("Sazizz")
    
def dbclick(event):
    print("Carnazza")
    
def kbpressed(event):
    print(event.char)

window = tk.Tk()

window.geometry("300x200")

#legge gli eventi del mouse
bt = tk.Button(text="Press me!")
bt.pack()
bt.bind("<Button-1>", btclick1)
bt.bind("<Button-2>", btclick2)
bt.bind("<Button-3>", btclick3)
lb = tk.Label(text="label1")
lb.pack()
bt.bind("<Double-Button-1>", dbclick)

#legge gli eventi della tastiera
window.bind("<Key>", kbpressed)

window.mainloop()