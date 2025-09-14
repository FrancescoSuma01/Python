import tkinter as tk
from tkinter import ttk
import const as c
import ProjectName as PjName

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title(c.name)
        self.geometry('1000x691')
        self.resizable(False, False)
        self.configure(bg='#e9ecef')
        frame = MainFrame(self)
        frame.pack(fill="both", expand=True, padx=20, pady=20)

class MainFrame(tk.Frame):
    def __init__(self, container):
        super().__init__(container)
        self.configure(bg='#e9ecef')
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=3) 
        self.grid_rowconfigure(0, weight=1)
        self.create_options_section()
        self.create_right_section()

    def create_options_section(self):
        options_frame = tk.LabelFrame(
            self, text="⚙️ Opzioni", font=("Segoe UI", 12, "bold"),
            bg='#ffffff', fg='#212529', bd=0, relief='flat',
            width=1000, height=400, padx=20, pady=20
        )
        options_frame.grid(row=0, column=0, sticky="ns", padx=(0, 20))
        options_frame.grid_propagate(False)  
        self.selectedOption = tk.StringVar(value=c.rb1)
        options = [c.rb1, c.rb2, c.rb3, c.rb4, c.rb5]
        for option in options:
            radio = tk.Radiobutton(
                options_frame, text=option, variable=self.selectedOption, 
                value=option, bg='#ffffff', fg='#495057',
                font=('Segoe UI', 10),
                anchor="w", indicatoron=True
            )
            radio.pack(fill="x", pady=4)

    def create_right_section(self):
        right_main_frame = tk.Frame(self, bg='#e9ecef')
        right_main_frame.grid(row=0, column=1, sticky="nsew")
        right_main_frame.grid_rowconfigure(0, weight=0)
        right_main_frame.grid_rowconfigure(1, weight=0)
        right_main_frame.grid_rowconfigure(2, weight=0)
        right_main_frame.grid_columnconfigure(0, weight=1)

        input_frame = tk.LabelFrame(
            right_main_frame, text="📝 Input", font=("Segoe UI", 12, "bold"),
            bg='#ffffff', fg='#212529', bd=0, relief='flat', padx=20, pady=20,
            height=280
        )
        input_frame.grid(row=0, column=0, sticky="nsew", pady=(0, 15))
        input_frame.grid_propagate(False)
        input_frame.grid_columnconfigure(0, weight=1)
        input_frame.grid_rowconfigure(1, weight=1)
        
        input_label = tk.Label(
            input_frame, text=c.originalText, bg='#ffffff',
            fg='#495057', font=('Segoe UI', 10)
        )
        input_label.grid(row=0, column=0, sticky="w", pady=(0, 8))
        
        self.input_text = tk.Text(
            input_frame, font=('Segoe UI', 11), bd=1, relief='flat',
            highlightthickness=1, highlightcolor='#3498db',
            wrap='word', bg='#f8f9fa'
        )
        self.input_text.grid(row=1, column=0, sticky="nsew")
        self.input_text.focus_set()
        
        input_scroll = tk.Scrollbar(input_frame, orient="vertical", command=self.input_text.yview)
        input_scroll.grid(row=1, column=1, sticky="ns")
        self.input_text.config(yscrollcommand=input_scroll.set)

        execute_btn = tk.Button(
            right_main_frame, text=f"🚀 {c.executeLogic}", command=self.executeLogic,
            font=("Segoe UI", 11, "bold"), bg='#3498db', fg='white',
            bd=0, width=18, height=2, relief='flat', cursor='hand2'
        )
        execute_btn.grid(row=1, column=0, pady=5)
        execute_btn.bind("<Enter>", lambda e: execute_btn.config(bg='#2980b9'))
        execute_btn.bind("<Leave>", lambda e: execute_btn.config(bg='#3498db'))

        output_frame = tk.LabelFrame(
            right_main_frame, text="📤 Output", font=("Segoe UI", 12, "bold"),
            bg='#ffffff', fg='#212529', bd=0, relief='flat', padx=20, pady=20,
            height=280
        )
        output_frame.grid(row=2, column=0, sticky="nsew", pady=(15, 0))
        output_frame.grid_propagate(False)
        output_frame.grid_columnconfigure(0, weight=1)
        output_frame.grid_rowconfigure(1, weight=1)
        
        output_label = tk.Label(
            output_frame, text=c.modifiedText, bg='#ffffff',
            fg='#495057', font=('Segoe UI', 10)
        )
        output_label.grid(row=0, column=0, sticky="w", pady=(0, 8))
        
        self.output_text = tk.Text(
            output_frame, font=('Segoe UI', 11), bd=1, relief='flat',
            wrap='word', bg="#f8f9fa", selectbackground="#3498db", 
            selectforeground="white", state="disabled"
        )
        self.output_text.grid(row=1, column=0, sticky="nsew")
        
        output_scroll = tk.Scrollbar(output_frame, orient="vertical", command=self.output_text.yview)
        output_scroll.grid(row=1, column=1, sticky="ns")
        self.output_text.config(yscrollcommand=output_scroll.set)
        
        copy_btn = tk.Button(
            output_frame, text=f"📋 {c.copy}", command=self.copy_to_clipboard,
            font=("Segoe UI", 11, "bold"), bg='#27ae60', fg='white',
            bd=0, width=18, height=2, relief='flat', cursor='hand2'
        )
        copy_btn.grid(row=2, column=0, columnspan=2, pady=(12, 0))
        copy_btn.bind("<Enter>", lambda e: copy_btn.config(bg='#229954'))
        copy_btn.bind("<Leave>", lambda e: copy_btn.config(bg='#27ae60'))
        self.input_text.bind('<Control-Return>', lambda event: self.executeLogic())

    def executeLogic(self):
        if self.selectedOption.get() == c.rb1:
            input_text = self.input_text.get("1.0", "end-1c")
            result = PjName.projectName(input_text)
            self.output_text.config(state="normal")
            self.output_text.delete("1.0", "end")
            self.output_text.insert("1.0", result)
            self.output_text.config(state="disabled")

    def copy_to_clipboard(self):
        text_to_copy = self.output_text.get("1.0", "end-1c")
        if text_to_copy:
            self.clipboard_clear()
            self.clipboard_append(text_to_copy)
            self.update()
            original_text = text_to_copy
            self.output_text.config(state="normal")
            self.output_text.delete("1.0", "end")
            self.output_text.insert("1.0", "✅ Copiato negli appunti!")
            self.output_text.config(bg="#d5f4e6", state="disabled")
            def restore_text():
                self.output_text.config(state="normal")
                self.output_text.delete("1.0", "end")
                self.output_text.insert("1.0", original_text)
                self.output_text.config(bg="#f8f9fa", state="disabled")
            self.after(1500, restore_text)

if __name__ == "__main__":
    app = App()
    app.mainloop()
