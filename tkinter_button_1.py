import tkinter as tk

root=tk.Tk()

def func():
	print("押せ")
button=tk.Button(root,text="pushed",command=func)
button.pack()
root.mainloop()