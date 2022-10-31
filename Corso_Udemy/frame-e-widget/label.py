import tkinter as tk


app = tk.Tk()
app.geometry("400x300")

ll = tk.Label(app, text="Ecco una label")
ll["background"] = 'yellow'
ll["foreground"] = 'blue'
ll["font"] = ("Times New Roman", 20)
ll.pack()

app.mainloop()