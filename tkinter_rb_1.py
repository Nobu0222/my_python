import tkinter as tk

root=tk.Tk()

def func1():
	label.config(text='Button1')

def func2():
	label.config(text='Button2')

sel=tk.IntVar()
sel.set(1)
label=tk.Label(root,text='SelectButton')
label.pack()
rb1=tk.Radiobutton(root,text='Button1',variable=sel,value=1,command=func1)
rb1.pack()
rb2=tk.Radiobutton(root,text='Button2',variable=sel,value=2,command=func2)
rb2.pack()
root.mainloop()