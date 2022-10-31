import tkinter as tk

app = tk.Tk()
app.geometry("250x150")

label1 = tk.Label(app, text="Name: ", bg='yellow')
label1.place(x=10, y=10)
tk.Entry(app, bg='#fdffc7').place(x=90, y=10)

label2 = tk.Label(app, text="Password: ", bg='yellow')
label2.place(x=10, y=40)
tk.Entry(app, bg='#fdffc7').place(x=90, y=40)

tk.Button(app, text="Login").place(x=90, y=70)

app.mainloop()