import webbrowser as wb
import tkinter
from tkinter import messagebox

window = tkinter.Tk()
window.title("Calculator")
btn_add = tkinter.Button(window, text="Addition", font=("Consolas", 12))
btn_add.pack(padx=10, pady=10)
count1 = 0


def click1(event):
    global count1
    count1 = count1 + 1
    if count1 >= 1:
        wb.get().open("E:\\CODE_DEV\\Python\\App\\Winform\\own_calculator\\addition.py")
    else:
        pass


btn_add.bind("<ButtonRelease-1>", click1)
btn_sub = tkinter.Button(window, text="Subtraction", font=("Consolas", 12))
btn_sub.pack(padx=10, pady=15)
count2 = 0


def click2(event):
    global count2
    count2 = count2 + 1
    if count2 >= 1:
        wb.get().open("E:\\CODE_DEV\\Python\\App\\Winform\\own_calculator\\subtraction.py")
    else:
        pass


btn_sub.bind("<ButtonRelease-1>", click2)
btn_mul = tkinter.Button(window, text="Multiplication", font=("Consolas", 12))
btn_mul.pack(padx=10, pady=20)
count3 = 0


def click3(event):
    global count3
    count3 = count3 + 1
    if count3 >= 1:
        wb.get().open("E:\\CODE_DEV\\Python\\App\\Winform\\own_calculator\\multiplication.py")
    else:
        pass


btn_mul.bind("<ButtonRelease-1>", click3)
btn_div = tkinter.Button(window, text="Division", font=("Consolas", 12))
btn_div.pack(padx=10, pady=25)
count4 = 0


def click4(event):
    global count4
    count4 = count4 + 1
    if count4 >= 1:
        wb.get().open("E:\\CODE_DEV\\Python\\App\\Winform\\own_calculator\\division.py")
    else:
        pass


btn_div.bind("<ButtonRelease-1>", click4)
btn_help = tkinter.Button(window, text="Help", font=("Consolas", 12))
btn_help.pack(padx=10, pady=30)
count5 = 0


def click5(event):
    global count5
    count5 = count5 + 1
    if count5 >= 1:
        messagebox.showinfo("First", "Please dont click space in some textboxes")
        messagebox.showinfo("Second", "Write integers")
    else:
        pass


btn_help.bind("<ButtonRelease-1>", click5)
window.mainloop()
