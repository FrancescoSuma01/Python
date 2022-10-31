import tkinter as tk

def accedi():
    u = user.get() #restituisce il contenuto della cella
    p = pwd.get()  ##restituisce il contenuto della cella
    print("utente: ", u)
    print("Password: ", p)

    #pulizia delle caselle
    user.set("")
    pwd.set("")

app = tk.Tk()
app.geometry("400x300")
app.title("Modelli")

user = tk.StringVar()
pwd = tk.StringVar()

tx1 = tk.Entry(app, textvariable = user)
tx1.pack()

tx2 = tk.Entry(app, textvariable = pwd)
tx2["show"] = '*' #show serve a sosituire i caratteri che inseriamo con quello che viene messo dopo l'uguale
tx2.pack()

bt = tk.Button(app, text="Accedi", command=accedi)
bt.pack()

app.mainloop()