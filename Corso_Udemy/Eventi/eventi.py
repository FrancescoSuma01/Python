import tkinter as tk

def clic1():
    print("clic!!")

def azione1(e):
    print(e.x, e.y)

def azione2(e):
    print("tasto dx")

def azione3(e):
    print("doppio clic")

def azione4(e):
    print("x:", e.x, "y:", e.y)

def azione5(e):
    print("INVIO")

def azione6(e):
    print("azione 6")


app = tk.Tk()
app.geometry("300x200")

#bt = tk.Button(app, text="Clic", command=clic1)
bt = tk.Button(app, text="Clic")
bt.pack(fill=tk.BOTH, expand=True)

bt.bind('<Button-1>', azione1) #tasto sinistro
bt.bind('<Button-2>', azione2) #tasto destro
bt.bind('<Double-Button-1>', azione3) #doppio clic tasto sinistro

#bt.bind('<Motion>', azione4)

bt2 = tk.Button(app, text="Clic2")
bt2.pack(fill=tk.BOTH, expand=True)
bt2.focus()
bt2.bind('<Return>', azione5) #return = tasto invio
bt2.bind('<Return>', azione6, add='+') #con il piu chiamera il 5 e il 6

#bt2.unbind('<Return>') #non ascoltera più il tasto 

app.mainloop()