from tkinter import *

root = Tk()
root.geometry("400x400")


def interest():
    v = a.get()
    q = p.get()
    w = t.get()
    d = r.get()
    if v == 0:
        i = q * w * d / 100
    else:
        c = q * (1 + d / 100) ** w
        i = c - q

    l5.config(text=str(i))


a = IntVar()
p = IntVar()
t = IntVar()
r = IntVar()
rb1 = Radiobutton(root, variable=a, value=0, text="Simple intrest")
rb2 = Radiobutton(root, variable=a, value=1, text="Compount intrest")
rb1.grid(row=1, column=1)
rb2.grid(row=1, column=2)
f1 = Frame(root)
l1 = Label(f1, text="Select Principal Amount")
s1 = Scale(f1, from_=10000, to=1000000, orient=HORIZONTAL, variable=p)
l2 = Label(f1, text="Select times in years")
s2 = Scale(f1, from_=1, to=20, orient=HORIZONTAL, variable=t)
l3 = Label(f1, text="Select Rate of insrest")
s3 = Scale(f1, from_=5, to=35, orient=HORIZONTAL, variable=r)
b1 = Button(f1, text="Get returns", command=interest)
l4 = Label(f1, text="Your returns")
l5 = Label(f1)
f1.grid(row=2, column=1)
l1.pack()
s1.pack()
l2.pack()
s2.pack()
l3.pack()
s3.pack()
b1.pack()
l4.pack()
l5.pack()

root.mainloop()