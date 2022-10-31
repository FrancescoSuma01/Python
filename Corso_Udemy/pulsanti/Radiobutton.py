import tkinter as tk

def getSelected():
    v = selected.get()
    lab['text'] = "Hai selezionato: " + str(v)

app = tk.Tk()
app.geometry("400x300")

selected = tk.StringVar()
livelli = ('off','min','med','max')

i = 0
for lv in livelli:
    r = tk.Radiobutton(app)
    r["text"] = lv
    r["value"] = i
    i += 1
    r["variable"] = selected
    r["command"] = getSelected
    r.pack()

lab = tk.Label(app)
lab.pack()

app.mainloop()