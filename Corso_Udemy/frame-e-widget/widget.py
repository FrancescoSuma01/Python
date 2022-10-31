import tkinter as tk

app = tk.Tk()
app.title("widget")
app.geometry("400x300")

#master garantische che il frame si trova nella regione delimitata da app
#fr = tk.Frame(master=app, width=200, height=100)
fr = tk.Frame(master=app)
fr["width"] = 200
fr["height"] = 100
fr["background"] = 'red'

#flat, raised, sunken, solid, ridge, groove
fr["relief"] = 'solid' #sunken = sprofondato
fr["borderwidth"] = 3

#https://anzeljg.github.io/rin2/book2/2405/docs/tkinter/cursors.html
fr["cursor"] = 'pirate'
fr.pack()

app.mainloop()