import tkinter as tk

app = tk.Tk()
app.geometry("350x550")
app.title("CALCOLATRICE by Ciccio")

label = [['7','8','9','+'],['5','6','7','-'],['1','2','3','x'],['+','0','=',':']]

display = tk.Entry(app)
display.grid(row=0, column=0, columnspan=3)

for rw in range(4):
    app.rowconfigure(rw+1, weight=33, minsize=50)
    for cl in range(4):
        app.columnconfigure(cl, weight=1)

        fr = tk.Frame(app)
        fr.grid(row=rw+1, column=cl,sticky='nsew', padx=3, pady=3)

        bt = tk.Button(fr, text=label[rw][cl]).pack(expand=True, fill=tk.BOTH)

app.mainloop()