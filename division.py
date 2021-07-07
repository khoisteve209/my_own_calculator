import tkinter
from tkinter import messagebox
from tkinter import font

r = tkinter.Tk()
r.title("Division")
txt_1 = tkinter.Label(r, text="The A dividend<an integer>", font=("Consolas", 12))
txt_1.pack(padx=10, pady=10)
txb_1 = tkinter.Entry(width=15, font=("Consolas", 12))
txb_1.pack(padx=10, pady=15)
t1 = tkinter.Label(r, text="Is divided by(/)", font=("Consolas", 12))
t1.pack(padx=10, pady=20)
txt_2 = tkinter.Label(r, text="The B divisor<an integer>", font=("Consolas", 12))
txt_2.pack(padx=10, pady=25)
txb_2 = tkinter.Entry(width=15, font=("Consolas", 12))
txb_2.pack(padx=10, pady=30)
btn_1 = tkinter.Button(r, text="Calculate A / B", font=("Consolas", 12))
btn_1.pack(padx=10, pady=35)
clickcount = 0


def onclick(event):
    global clickcount
    clickcount = clickcount + 1
    if clickcount >= 1:
        if txb_1.get() != "" and txb_2.get() != "":
            messagebox.showinfo("Calculated",
                                f"{int(txb_1.get())} / {int(txb_2.get())} = {int(txb_1.get()) / int(txb_2.get())}")
        else:
            messagebox.showinfo("Error", "Some of textboxes are empty")
    else:
        pass


btn_1.bind("<ButtonRelease-1>", onclick)
r.mainloop()
