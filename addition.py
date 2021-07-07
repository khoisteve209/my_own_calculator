import tkinter
from tkinter import messagebox

root = tkinter.Tk()
root.title("Addition")
txt_1 = tkinter.Label(root, text="A number<an integer>", font=("Consolas", 12))
txt_1.pack(padx=10, pady=5)
txb_1 = tkinter.Entry(width=15, font=("Consolas", 12))
txb_1.pack(padx=10, pady=15)
txt_2 = tkinter.Label(root, text="Plus(+)", font=("Consolas", 12))
txt_2.pack(padx=10, pady=20)
txt_3 = tkinter.Label(root, text="B number<an integer>", font=("Consolas", 12))
txt_3.pack(padx=10, pady=25)
txb_2 = tkinter.Entry(width=15, font=("Consolas", 12))
txb_2.pack(padx=10, pady=30)
btn_1 = tkinter.Button(root, text="Calculate A + B", font=("Consolas", 12))
btn_1.pack(padx=10, pady=35)
count = 0


def myclick(event):
    global count
    count = count + 1
    if count >= 1:
        if txb_1.get() != "" and txb_2.get() != "":
            messagebox.showinfo("Calculated",
                                f"{int(txb_1.get())} + {int(txb_2.get())} = {int(txb_1.get()) + int(txb_2.get())}")
        else:
            messagebox.showerror("Oh no", "Some textboxes are empty")
    else:
        pass


btn_1.bind("<ButtonRelease-1>", myclick)
root.mainloop()
