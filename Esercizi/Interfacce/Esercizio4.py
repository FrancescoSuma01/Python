import tkinter as tk

def incrementa():
    n = int(lbvalue["text"]) + 1
    lbvalue["text"] = n 
    
def decrementa():
    n = int(lbvalue["text"]) - 1
    lbvalue["text"] = n

window = tk.Tk()
window.geometry("300x200")

btplus = tk.Button(text="+", width = 10, height = 2, command=incrementa)
btplus.pack()
btminus = tk.Button(text="-", width = 10, height = 2, command=decrementa)
btminus.pack()
lbvalue = tk.Label(text="0", width = 10, height = 2, bg = "grey")
lbvalue.pack()

window.mainloop()