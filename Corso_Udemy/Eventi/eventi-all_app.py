import tkinter as tk

'''
def getTasto(e):
    print(e)
'''

def getTasto(e):
    print(e)
    if (e.char == 'a'):
        print("AAAA")

def close(e):
    app.destroy()

def x(e):
    print("---")

def y(e):
    print("+++")

app = tk.Tk()
app.geometry("300x200")

#app.bind("<Key>", getTasto)
app.bind("<Escape>", close)
app.bind("<Key-A>", x)   #prende combinazioni di tasti in questo caso Shift+A
app.bind("<Shift-Tab>", y) #prende combinazioni di tasti in questo caso Shift+Tab

app.mainloop()

'''
app = tk.Tk()
app.geometry("300x200")

#key prende gli eventi della tastiera
app.bind("<Key>", getTasto)

app.mainloop()
'''