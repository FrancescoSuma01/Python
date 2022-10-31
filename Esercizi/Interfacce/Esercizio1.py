"""
    Genera e Apre una finesta con Titolo "Hello World" e all'interno "Questa è la mia prima app"
    e successivamente troviamo un bottonone"
"""

import tkinter as tk

app = tk.Tk() #crea la finestra

app.title("Hello World!") #titolo della finestra

app.geometry("300x200") #da la dimensione alla finestra

label = tk.Label(text="Questa è la mia prima app!", fg = "white", bg = "grey", width = 20, height = 3) #mette un titolo
label.pack() #impacchetta

button = tk.Button(text="Clicca Qui!", fg = "white", bg="grey" )
button.pack()

#fa mettere una casella per inserire testo
txt = tk.Entry(width=20)
txt.pack()

app.mainloop() #dopo questo non viene eseguito piu niente