from tkinter import *
from tkinter import ttk

root = Tk()
root.title("METANIT.COM")
root.geometry("250x250")

verticalScale = ttk.Scale(orient=VERTICAL, length=200, from_=1.0, to=100.0, value=50)
verticalScale.pack()

root.mainloop()