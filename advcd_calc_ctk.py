import tkinter as tk
import math, os
import tkinter.messagebox
import customtkinter as ctk

clear = lambda: os.system("cls")
clear()


app = ctk.CTk()

ctk.set_appearance_mode("dark")

logo = tk.PhotoImage(file = "coconut.png")

app.iconphoto(0, logo)

app.title("Lumbego Calculator")

app.resizable(0, 0)

app.geometry("450x510+150+75")

calc_frame = ctk.CTkFrame(app)

calc_frame.grid()

class calc_class():
    def __init__(self):
        self.total = 0
        self.current = ""
        self.input_val = 1
        self.check_sum = 0
        self.op = ""
        self.result = 0

    def numEnter(self, num):
        self.result = 0
        first_num = txt_display.get()
        second_num = str(num)

        if self.input_val:
            self.current = second_num
            self.input_val = 0
        else:
            if second_num == ".":
                if second_num in first_num:
                    return
            self.current = first_num + second_num
        self.display(self.current)

    def sum_of_total(self):
        self.result = 1        
        self.current = float(self.current)
        if self.check_sum == 1:
            self.valid_foo()
        else:
            self.total = float(txt_display.get())

    def display(self, value):
        txt_display.delete(0, ctk.END)
        txt_display.insert(0, value)
    
    def valid_foo(self):
        match self.op:
            case "add":
                self.total += self.current
            case "sub":
                self.total -= self.current
            case "multi":
                self.total *= self.current
            case "divide":
                self.total /= self.current
            case "mod":
                self.total %= self.current
        self.input_val = 1
        self.check_sum = 0
        self.display(self.total)

    def operation(self, op):
        self.current = float(self.current)
        if self.check_sum:
            self.valid_foo()
        elif not self.result:
            self.total = self.current
            self.input_val = 1
        self.check_sum = 1
        self.op = op
        self.result = 0
    
    def clear_entry(self):
        self.result = 0
        self.current = "0"
        self.display(0)
        self.input_val = 1

    def all_clear_entry(self):
        self.clear_entry()
        self.total = 0

    def pi(self):
        self.result = 0
        self.current = math.pi
        self.display(self.current)
        
    def tau(self):
        self.result = 0
        self.current = math.tau
        self.display(self.current)
        
    def e(self):
        self.result = 0
        self.current = math.e
        self.display(self.current)
        
    def mathPM(self):
        self.result = 0
        self.current = -(float(txt_display.get()))
        self.display(self.current)
        
    def squared(self):
        self.result = 0
        self.current = math.sqrt(float(txt_display.get()))
        self.display(self.current)
        
    def cos(self):
        self.result = 0
        self.current = math.cos(math.radians(float(txt_display.get())))
        self.display(self.current)
        
    def cosh(self):
        self.result = 0
        self.current = math.cosh(math.radians(float(txt_display.get())))
        self.display(self.current)
        
    def tan(self):
        self.result = 0
        self.current = math.tan(math.radians(float(txt_display.get())))
        self.display(self.current)
        
    def tanh(self):
        self.result = 0
        self.current = math.tan(math.radians(float(txt_display.get())))
        self.display(self.current)
        
    def sin(self):
        self.result = 0
        self.current = math.sin(math.radians(float(txt_display.get())))
        self.display(self.current)
        
    def sinh(self):
        self.result = 0
        self.current = math.sinh(math.radians(float(txt_display.get())))
        self.display(self.current)
        
    def log(self):
        self.result = 0
        self.current = math.log(float(txt_display.get()))
        self.display(self.current)
        
    def exp(self):
        self.result = 0
        self.current = math.exp(float(txt_display.get()))
        self.display(self.current)
        
    def acosh(self):
        self.result = 0
        self.current = math.acosh(float(txt_display.get()))
        self.display(self.current)
        
    def asinh(self):
        self.result = 0
        self.current = math.asinh(float(txt_display.get()))
        self.display(self.current)
        
    def expm1(self):
        self.result = 0
        self.current = math.expm1(float(txt_display.get()))
        self.display(self.current)
        
    def lgamma(self):
        self.result = 0
        self.current = math.lgamma(float(txt_display.get()))
        self.display(self.current)
        
    def degrees(self):
        self.result = 0
        self.current = math.degrees(float(txt_display.get()))
        self.display(self.current)
        
    def log2(self):
        self.result = 0
        self.current = math.log2(float(txt_display.get()))
        self.display(self.current)
        
    def log10(self):
        self.result = 0
        self.current = math.log10(float(txt_display.get()))
        self.display(self.current)
        
    def log1p(self):
        self.result = 0
        self.current = math.log1p(float(txt_display.get()))
        self.display(self.current)

added_val = calc_class()

txt_display = ctk.CTkEntry(calc_frame, 
                       width = 450,
                       font = ("Helvetice", 20, "bold"),
                       fg_color = "#2b2b2b",
                       text_color = "#FF9F0A",
                       border_color = "#2b2b2b",
                       corner_radius = 90,
                       justify = "right")

txt_display.grid(row = 0, 
                 column = 0, 
                 columnspan = 4)

txt_display.insert(0, "0")


# Function requires number, row and column value
def num_btn_maker(num, row_, col):
    num_btn = ctk.CTkButton(calc_frame,
              width = 90,
              height = 90, corner_radius = 90,
              fg_color = "#333333", hover_color = "#000000",
              text_color = "white",
              font = ("Helvetica", 20, "bold"),
              text = num, 
              command = lambda: added_val.numEnter(num))
    num_btn.grid(row = row_, column = col, pady = 1)


# Function requires symbol, row and column value
def symb_btn_maker(text_, cmd, row_, col):
    symb_btn = ctk.CTkButton(calc_frame, 
              text = text_, 
              width = 90, height = 90, corner_radius = 90,
              fg_color = "#FF9F0A", hover_color = "#E3C139",
              font = ("Helvetica", 15, "bold"),
              command = cmd)
    symb_btn.grid(row = row_, column = col)

# Number buttons
num_btn_maker(1, 4, 0)
num_btn_maker(2, 4, 1)  # Third row
num_btn_maker(3, 4, 2)

num_btn_maker(4, 3, 0)
num_btn_maker(5, 3, 1)  # Second row
num_btn_maker(6, 3, 2)

num_btn_maker(7, 2, 0)
num_btn_maker(8, 2, 1)  # First row
num_btn_maker(9, 2, 2)

num_btn_maker(0, 5, 0) # Zero btn


# Symbol buttons
symb_btn_maker(chr(67), added_val.clear_entry, 1, 0) # Button Clear
symb_btn_maker(chr(67) + chr(69), added_val.all_clear_entry, 1, 1) # Button All Clear
symb_btn_maker("\u221A", added_val.squared, 1, 2) # Button Squared

symb_btn_maker("+", lambda: added_val.operation("add"), 1, 3) # Button Add
symb_btn_maker("-", lambda: added_val.operation("sub"), 2, 3) # Button Sub
symb_btn_maker("x", lambda: added_val.operation("multi"), 3, 3) # Button Multi
symb_btn_maker("/", lambda: added_val.operation("divide"), 4, 3) # Button Divide

symb_btn_maker(".", lambda: added_val.numEnter("."), 5, 2) # Button Dot
symb_btn_maker(chr(177), added_val.mathPM, 5, 1) # Button PM
symb_btn_maker("=", added_val.sum_of_total, 5, 3) # Button Equal

# Row 1:
symb_btn_maker("pi", added_val.pi, 1, 4) # Button Pi num
symb_btn_maker("Cos", added_val.cos, 1, 5) # Button Cos
symb_btn_maker("tan", added_val.tan, 1, 6) # Button Clear
symb_btn_maker("sin", added_val.sin, 1, 7) # Button Clear

# Row 2:
symb_btn_maker("2pi", added_val.tau, 2, 4) # Button 2pi
symb_btn_maker("Cosh", added_val.cosh, 2, 5) # Button Cosh
symb_btn_maker("tanh", added_val.tanh, 2, 6) # Button tanh
symb_btn_maker("sinh", added_val.sinh, 2, 7) # Button sinh

# Row 3:
symb_btn_maker("log", added_val.log, 3, 4) # Button log
symb_btn_maker("exp", added_val.exp, 3, 5) # Button exp
symb_btn_maker("Mod", lambda: added_val.operation("mod"), 3, 6) # Button Mod
symb_btn_maker("e", added_val.e, 3, 7) # Button E

# Row 4:
symb_btn_maker("log10", added_val.log10, 4, 4) # Button log10
symb_btn_maker("log1p", added_val.log1p, 4, 5) # Button cos
symb_btn_maker("expm1", added_val.expm1, 4, 6) # Button expm1
symb_btn_maker("gamma", added_val.lgamma, 4, 7) # Button gamma

# Row 5:
symb_btn_maker("log2", added_val.log2, 5, 4) # Button log2
symb_btn_maker("deg", added_val.degrees, 5, 5) # Button degree
symb_btn_maker("acosh", added_val.acosh, 5, 6) # Button acosh
symb_btn_maker("asinh", added_val.asinh, 5, 7) # Button asinh

# Label for additional buttons
lbl_display = ctk.CTkLabel(calc_frame, text = "Scientific Calculator",
                       font = ("Helvetica", 20, "bold"),
                       fg_color = "#2b2b2b", text_color = "white", justify = "center")
lbl_display.grid(row = 0, column = 4, columnspan = 4, pady = 1)

def iExit():
    iExit = tkinter.messagebox.askyesno(title = "Lumbego Calculator",
                                        message = "Do you wish to exit?")
    if iExit:
        app.destroy()
    
def Scientific():
    app.resizable(0, 0)
    app.geometry("1000x491+0+0")

def Standart():
    app.resizable(0, 0)
    app.geometry("450x491+0+0")

menubar = tk.Menu(calc_frame)

# Menu Bar 1:
file_menu = tk.Menu(menubar, tearoff = 0)
menubar.add_cascade(label = "File", menu = file_menu)
file_menu.add_command(label = "Standart", command = Standart)
file_menu.add_command(label = "Scientific", command = Scientific)
file_menu.add_separator()
file_menu.add_command(label = "Exit", command = iExit)

# Menu Bar 1:
edit_menu = tk.Menu(menubar, tearoff = 0)
menubar.add_cascade(label = "Edit", menu = edit_menu)
edit_menu.add_command(label = "Cut")
edit_menu.add_command(label = "Copy")
edit_menu.add_separator()
edit_menu.add_command(label = "Paste")

app.config(menu = menubar)
app.mainloop()