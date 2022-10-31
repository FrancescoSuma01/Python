import tkinter as tk

def btHandler():
    print("Hello!")

app = tk.Tk()

app.title("Bottone")

app.geometry("400x300")

#crea il bottone
bt = tk.Button(text="Clicca qui!", command=btHandler)
bt.pack()

app.mainloop()