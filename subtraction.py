import tkinter
from tkinter import messagebox
from tkinter import font
win = tkinter.Tk()
win.title("Subtraction")
lbl_1 = tkinter.Label(win, text="The A minus", font=("Consolas", 12))
lbl_1.pack(padx=10, pady=10)
txb_1 = tkinter.Entry(width=15, font=("Consolas", 12))
txb_1.pack(padx=10, pady=15)
lbl_3 = tkinter.Label(win, text="Minus(-)", font=("Consolas", 12))
lbl_3.pack(padx=10, pady=20)
lbl_2 = tkinter.Label(win, text="The B subtrahend", font=("Consolas", 12))
lbl_2.pack(padx=10, pady=25)
txb_2 = tkinter.Entry(width=15, font=("Consolas", 12))
txb_2.pack(padx=10, pady=30)
btn1 = tkinter.Button(win, text="Calculate A - B", font=("Consolas", 12))
btn1.pack(padx=10, pady=35)
t = 0
def ct(event):
    global t
    t = t + 1
    if t >= 1:
        if txb_1.get() != "" and txb_2.get() != "":
            messagebox.showinfo("Calculated", f"{txb_1.get()} - {txb_2.get()} = {int(txb_1.get()) - int(txb_2.get())}")
        else:
            messagebox.showerror("Error", "Some textboxes are empty")
    else:
        pass
btn1.bind("<ButtonRelease-1>", ct)
win.mainloop()