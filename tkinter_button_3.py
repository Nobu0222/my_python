import tkinter as tk

root=tk.Tk()

def func():
	label.config(text="押せ！")

def func_event(ev):
	label.config(text="押すんだ！")

label=tk.Label(root,text="↓BOTTON↓")
label.pack()
button=tk.Button(root,text="Push!",command=func)
button.pack()
button.bind("<Leave>",func_event)
root.mainloop()