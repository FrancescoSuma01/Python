from cgitb import text
import tkinter as tk

app = tk.Tk()
app.geometry("400x500")
app.title("")

text = tk.Text(app)
text.pack()

text.insert(tk.END,"Nel mezzo del cammin\n")
text.insert(tk.END,"Di nostra vita\n")
text.insert(tk.END,"Mi ritrovai...")

str = text.get("2.3", "2.10")   #primo valore=riga secondo valore=colonna
text.delete("3.8", "3.12")   #primo valore=riga secondo valore=colonna

text.tag_config("mark", background="yellow", foreground='black')
text.tag_add("mark", "1.0", tk.END)

app.mainloop()