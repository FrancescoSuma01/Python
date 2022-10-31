import tkinter as tk

def hello():
    name = txt.get()
    if not (name):
        label["text"]="Inserisci un nome"
    else:
        label["text"]="Ciao, "+txt.get()+"!"
    
def reset():
    label["text"]=" "
    
app = tk.Tk() #crea la finestra

#app.title("Hello World!") #titolo della finestra

app.geometry("300x200") #da la dimensione alla finestra

label = tk.Label(text="Label1") #mette un titolo
label.pack() #impacchetta

button = tk.Button(text="Clicca Qui!", command=hello )
button.pack()

button = tk.Button(text="Reset!", command=reset)
button.pack()

#fa mettere una casella per inserire testo
txt = tk.Entry(width=20)
txt.pack()

app.mainloop() #dopo questo non viene eseguito piu niente
