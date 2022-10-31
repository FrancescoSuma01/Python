import tkinter as tk

app = tk.Tk()
app.geometry("400x300")

for rw in range(0,3):
    app.rowconfigure(rw, weight=33, minsize=50)
    for cl in range(3):
        app.columnconfigure(cl, weight=33, minsize=50)

        fr = tk.Frame(app)
        fr.grid(row=rw, column=cl, sticky='nsew', padx=3, pady=3)

        bt = tk.Button(fr, text=f"R: {rw}\n C: {cl}").pack(expand=True, fill=tk.BOTH)

app.mainloop()