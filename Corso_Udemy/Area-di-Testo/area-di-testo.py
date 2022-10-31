from cProfile import label
import tkinter as tk

def btClic():
    txt = msg.get()
    lb["text"] = "Ciao, " + txt


def btClear():
    #ripulisce tutta la casella 
    msg.delete(0, tk.END)

app = tk.Tk()
app.title("Saluto Personale")
app.geometry("400x300")

bt = tk.Button(text="Vuoi un saluto? Cliccami", command=btClic)
bt.pack()

msg = tk.Entry()
msg.pack()

lb = tk.Label(text=" ")
lb.pack()

btc = tk.Button(text="clear", command=btClear)
btc.pack()

app.mainloop()