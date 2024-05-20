from re import I
from tkinter import *
from tkinter.ttk import *
from array import *

from mainWindow import sleep
        
def openNewWindow(i):
    
    # Toplevel object which will 
    # be treated as a new window
    newWindow = Toplevel()
 
    # sets the title of the
    # Toplevel widget
    newWindow.title("Action")
 
    # sets the geometry of toplevel
    newWindow.geometry("800x400")
    


    # def hobby():
    #     newWindow.destroy()
    # def social():
    #     newWindow.destroy()
    # def house():
    #     newWindow.destroy()
    # def train():
    #     newWindow.destroy()
    # def work():
    #     newWindow.destroy()
    # def study():
    #     newWindow.destroy()
    # def buy():
    #     newWindow.destroy()
        


    for r in range(6):
        btSle = Button(newWindow, text = "Sleep", command = lambda idx = i: sleep(idx))
        # btHob = Button(newWindow, text = "Hobby", command = hobby)
        # btSoc = Button(newWindow, text = "Social", command = social)
        # btHou = Button(newWindow, text = "House", command = house)
        # btTra = Button(newWindow, text = "Train", command = train)
        # btWor = Button(newWindow, text = "Work", command = work)
        # btStu = Button(newWindow, text = "Study", command = study)
        # btBuy = Button(newWindow, text = "Buy", command = buy)
        
        btSle.grid(row = r, column = 1, sticky = W, pady = 2)
        # btHob.grid(row = r, column = 2, sticky = W, pady = 2)
        # btSoc.grid(row = r, column = 3, sticky = W, pady = 2)
        # btHou.grid(row = r, column = 4, sticky = W, pady = 2)
        # btTra.grid(row = r, column = 5, sticky = W, pady = 2)
        # btWor.grid(row = r, column = 6, sticky = W, pady = 2)
        # btStu.grid(row = r, column = 7, sticky = W, pady = 2)
        # btBuy.grid(row = r, column = 8, sticky = W, pady = 2)