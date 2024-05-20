
from tkinter import *
from tkinter.ttk import *

from modules import calmodule

master = Tk()
master.state('zoomed')
master.title("NEET manager")



rows = 100
m = list()
bt = list()
e = list() #

def sleep(bt,i):
    calmodule.sleepcal(m, rows, e, i)
    bt[i].configure(text = "Sleep", command = lambda idx=i: cancel(bt,idx))
    # btn["text"] = f"Clicks {clicks}"
    # w = w*
    # disable Act button
    newWindow.destroy()
    for c in range(rows):
        
        bt[c].configure(state = ["normal"])

def cancel(bt,i):
    m[i].set(m[i].get() - 1)
    bt[i].configure(text = "Act", command = lambda idx=i: openNewWindow(bt,idx))
    #openNewWindow(bt,idx)

def openNewWindow(bt,i):
    
    global newWindow
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
    for c in range(rows):
        bt[c].configure(state = ["disabled"])

    
    bt[i].configure(state = ["active"])
    for r in range(6):
        btSle = Button(newWindow, text = "Sleep", command = lambda idx = i: sleep(bt,idx))
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


def maintable():
    for i in range(rows):
        # create an instance of IntVar() and append to list m
        m.append(IntVar())
        e.append(IntVar()) #



        w = Button(master, text = "Act", command = lambda idx=i: openNewWindow(bt,idx)) # assign the lambda to command
        w.grid(row = i % 40, column = (i // 40) * 6, sticky = W, pady = 2)
        bt.append(w)
        
        # def recall(*args):
        #     e[i].set(e[i-1].get() + m[i].get()) if i > 0 else e[i].set(m[i].get())
        #     print(args, e[i].get())
        
        # m[i].trace_add("write", recall)

        # m[i].trace_add('write', lambda val: e[i].set(e[i-1].get() + val) if i > 0 else e[i].set(val))
        # e[i].trace_add('write', lambda val: e[i+1].set(val + m[i+1]) if i < len(rows)-1 else None)
        #m[i].trace_add("write", lamda: e[i].set())
        # m[i].set(m[i-1].get) #

        l1 = Label(master, textvariable = m[i]) # used textvariable instead
        l1.grid(row = i % 40, column = (i // 40) * 6 + 1, sticky = W, pady = 2)

        l2 = Label(master, textvariable = e[i]) #
        l2.grid(row = i % 40, column = (i // 40) * 6 + 2, sticky = W, pady = 2) #

b1 = Button(master, text = "Start", command = maintable)
b1.grid(row = 0, column = 0, sticky = W, pady = 2)

mainloop()