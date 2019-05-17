import tkinter as tk

root=tk.Tk()

def func():
	label.config(text="押せ！")

label=tk.Label(root,text="PushBotton")
label.pack()
button=tk.Button(root,text="Pushed!",command=func)
button.pack()
root.mainloop()