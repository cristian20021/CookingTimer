
from tkinter import *
from tkinter import ttk
root = Tk()
root.title('Cooking Timer')
root.geometry("400x400")
frm = ttk.Frame(root, padding=10)
frm.grid()
ttk.Label(frm, text="Timers:").grid(column=1, row=1)

root.mainloop()