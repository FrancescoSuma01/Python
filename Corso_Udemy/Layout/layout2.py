import tkinter as tk

app = tk.Tk()
app.geometry("500x300")

fr1 = tk.Frame(app, background="yellow")
fr1.pack(fill=tk.X, side=tk.TOP, padx=5, pady=5) #fill = come si allargherà il frame

bt1 = tk.Button(fr1, text="Cliccami!").pack(side=tk.LEFT)
bt2 = tk.Button(fr1, text="Cliccami!").pack(side=tk.BOTTOM)
bt3 = tk.Button(fr1, text="Cliccami!").pack(side=tk.RIGHT)

fr2 = tk.Frame(app, background="blue")
fr2.pack(fill=tk.X, side=tk.TOP, padx=5, pady=5)

bt4 = tk.Button(fr2, text="Cliccami!").pack(side=tk.LEFT)
bt5 = tk.Button(fr2, text="Cliccami!").pack(side=tk.LEFT)

app.mainloop()