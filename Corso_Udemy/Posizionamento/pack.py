import tkinter as tk

app = tk.Tk()
app.geometry("500x400")

fr1 = tk.Frame(app, background="blue", height=50)
fr1.pack(fill=tk.BOTH, side=tk.TOP, expand=False)

fr2 = tk.Frame(app, background="red", height=50)
fr2.pack(fill=tk.BOTH, side=tk.TOP, expand=True)

fr3 = tk.Frame(fr2, background="yellow", height=50, width=50)
fr3.pack(fill=tk.BOTH, side=tk.LEFT)

tk.Button(fr1, text="Button Fr1").pack()
tk.Button(fr2, text="Button Fr2").pack()
tk.Button(fr3, text="Button Fr3").pack()

app.mainloop()