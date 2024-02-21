import tkinter as tk
import random as rnd
from os import system

clear = lambda: system("cls")
clear()

expression_dict = {"expression": "",}

def press_num(num):
    expression_dict["expression"] += str(num)
    equation.set(expression_dict["expression"])

def press_symb(symb):
    if len(expression_dict["expression"]) == 0:
        expression_dict["expression"] = "0" + symb

    symb_val = [string for string in expression_dict["expression"]]
    if symb_val[-1] in "+-*/.":
        symb_val[-1] = symb
        expression_dict["expression"] = "".join(symb_val)
    else:
        expression_dict["expression"] += symb

    equation.set(expression_dict["expression"])
        

def equal_press():
    try:
        total = eval(str(expression_dict["expression"]))
        
        equation.set(total)

        expression_dict["expression"] = f"{total}"

    except:
        equation.set(" error ")
        expression_dict["expression"] = ""

def clr():
    expression_dict["expression"] = ""
    equation.set("0")

def num_btn_maker(num, row_val, col_val):
    return tk.Button(win, text = f" {str(num)} ", 
                     command = lambda: press_num(num), 
                     height = 5, width = 8, font = ("Verdana", 10), fg = "white", bg = "#333333").grid(row = row_val, padx = 2, pady = 2, column = col_val, stick = "nswe")

def symb_btn_maker(symb, row_val, col_val):
    return tk.Button(win, text = f" {symb} ", 
                     command = lambda: press_symb(symb), 
                     height = 5, width = 8, font = ("Verdana", 10), fg = "white", bg = "#FF9F0A").grid(row = row_val, padx = 2, pady = 2, column = col_val, stick = "nswe")


if __name__ == "__main__":
    win = tk.Tk()

    win.title("Lumbego")

    win.geometry("390x410+150+75")

    win.config(bg = "black")

    win.resizable(False, False)

    logo = tk.PhotoImage(file = "logo.png")

    win.iconphoto(False, logo)

    equation = tk.StringVar()

    # Expression field
    tk.Button(win, command = clr()).grid(row = 0, column = 0)
    expression_field = tk.Entry(win, textvariable = equation, font = ("Verdana", 15), width = 30,fg = "white", bg = "black", justify = tk.RIGHT)
    expression_field.grid(row = 0, column = 0, columnspan = 5)
    
    # Numbers
    num_btn_maker(1, 1, 1)
    num_btn_maker(2, 1, 2)
    num_btn_maker(3, 1, 3)

    num_btn_maker(4, 2, 1)
    num_btn_maker(5, 2, 2)
    num_btn_maker(6, 2, 3)

    num_btn_maker(7, 3, 1)
    num_btn_maker(8, 3, 2)
    num_btn_maker(9, 3, 3)
    
    zero_btn = tk.Button(win, text = "0", command = lambda: press_num(0), height = 5, width = 8, fg = "white", bg = "#333333")
    zero_btn.grid(row = 4, column = 2, columnspan = 2, stick = "wesn", padx = 2, pady = 2)

    # Symbols
    symb_btn_maker("+", 1, 0)
    symb_btn_maker("-", 2, 0)
    symb_btn_maker("*", 3, 0)
    symb_btn_maker("/", 4, 0)
    symb_btn_maker(".", 4, 4)

    equal_btn = tk.Button(win, text = "=", command = equal_press, height = 5, width = 8, fg = "white", bg = "#FF9F0A")
    equal_btn.grid(row = 1, column = 4, rowspan = 3, stick = "wens", padx = 2, pady = 2,)

    clear_btn = tk.Button(win, text = "C", command = clr, height = 5, width = 8, fg = "white", bg = "#333333")
    clear_btn.grid(row = 4, column = 1, padx = 2, pady = 2, stick = "wens")

    win.mainloop()