import tkinter as tk
from turtle import left, right

from setuptools import Command

def left():
    print("Saziz")

def rigth():
    print("carn")


app = tk.Tk()
app.geometry("600x500")

#bt = tk.Button(app, command=clic)
bt = tk.Button(app)
bt["text"] = "Clicca qui"
bt["state"] = 'active' #disabled
bt.pack()

bt.bind("<Button-1", command=left)
bt.bind("<Button-2", command=right)

app.mainloop()