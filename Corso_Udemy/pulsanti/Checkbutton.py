import tkinter as tk

def leggiValore():
    v = scelta.get()
    lab["text"] = v

app = tk.Tk()
app.geometry("400x300")

scelta = tk.StringVar()

ck = tk.Checkbutton(app, command=leggiValore)
ck["text"] = "Accetto le condizioni"
ck["state"] = "active"
ck["onvalue"] = "Ok"
ck["offvalue"] = "No"
ck["variable"] = scelta
ck.pack()

lab = tk.Label(app)
lab.pack()

app.mainloop()