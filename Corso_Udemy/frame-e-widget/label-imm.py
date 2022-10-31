import tkinter as tk

app = tk.Tk()
app.geometry("600x500")
app.title("app con immagine")

photo = tk.PhotoImage(file="immagine.png")

label = tk.Label(app)
label["image"] = photo
label["text"] = "nome: Francesco SUMA"
label["font"] = ("Times New Roman",20)
label["compound"] = "top"
label.pack()

app.mainloop()