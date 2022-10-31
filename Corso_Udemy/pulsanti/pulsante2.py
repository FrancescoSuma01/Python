import tkinter as tk

def btHandler():
    lb["text"] = "Ciao!"

app = tk.Tk()

app.title("Bottone")

app.geometry("400x300")

#crea il bottone
bt = tk.Button(text="Clicca qui!", command=btHandler)
bt.pack()

lb = tk.Label(text="")
lb.pack()

app.mainloop()