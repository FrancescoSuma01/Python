import tkinter as tk

app = tk.Tk()
app.geometry("400x300")

lab = tk.Label(app, text="Sazizza a te e famiglia!", background="yellow")
lab.pack()

ent = tk.Entry(app, background="blue")
ent.pack()

bt = tk.Button(app, text="Cliccami!")
bt.pack()

app.mainloop()