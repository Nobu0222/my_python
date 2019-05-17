import tkinter as tk

root=tk.Tk()

def func(ev):
    label.config(text=e.get())

label=tk.Label(root,text="InputText")
label.pack()
e=tk.Entry(root)
e.pack()
e.bind("<Return>",func)
root.mainloop()