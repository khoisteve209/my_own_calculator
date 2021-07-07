import tkinter
from tkinter import messagebox
from tkinter import font
dow = tkinter.Tk()
dow.title("Multipliction")
txt_1 = tkinter.Label(dow, text="A number<an integer>", font=("Consolas", 12))
txt_1.pack(padx=10, pady=10)
txb_1 = tkinter.Entry(width=15, font=("Consolas", 12))
txb_1.pack(padx=10, pady=15)
txt_3 = tkinter.Label(dow, text="times(*)", font=("Consolas", 12))
txt_3.pack(padx=10, pady=20)
txt_2 = tkinter.Label(dow, text="B number<an integer>", font=("Consolas", 12))
txt_2.pack(padx=10, pady=25)
txb_2 = tkinter.Entry(width=15, font=("Consolas", 12))
txb_2.pack(padx=10, pady=30)
btn_1 = tkinter.Button(dow, text="Calculate A * B", font=("Consolas", 12))
btn_1.pack(padx=10, pady=35)
c = 0
def btn_1_click(event):
    global c
    c = c + 1
    if c >= 1:
        if txb_1.get() != "" and txb_2.get() != "":
            messagebox.showinfo("Calculated", f"{txb_1.get()} * {txb_2.get()} = {int(txb_1.get()) * int(txb_2.get())}") 
        else:
            messagebox.showerror("Error", "Some textboxes are empty")
    else:
        pass
btn_1.bind("<ButtonRelease-1>", btn_1_click)
dow.mainloop()