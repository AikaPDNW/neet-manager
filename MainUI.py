from re import I
from tkinter import *
from tkinter.ttk import *
from array import *

from modules.gameState import energy, encounter, rows


from modules import actionWindowUI

master = Tk()
master.state('zoomed')
master.title("NEET manager")

actBt = list()




def make_updater(i, m, e):
    def update(*args):
        if i > 0:
            e[i].set(e[i - 1].get() + m[i].get())
        else:
            e[i].set(m[i].get())

    return update


def make_updater_e(i, m, e):
    def update(*args):
        if i < len(e) - 1:
            e[i + 1].set(e[i].get() + m[i + 1].get())

    return update


def maintable():
    for i in range(rows):
        # create an instance of IntVar() and append to list m
        encounter.append(IntVar())
        energy.append(IntVar())  #

        tempBt = Button(master, text="Act", command=lambda idx=i: actionWindowUI.openActionWindow(actBt,
                                                                                                  idx, rows))  # assign the lambda to command
        tempBt.grid(row=i % 40, column=(i // 40) * 6, sticky=W, pady=2)
        actBt.append(tempBt)

        encounter[i].trace_add("write", make_updater(i, encounter, energy))
        energy[i].trace_add("write", make_updater_e(i, encounter, energy))

        encounterLb = Label(master, textvariable=encounter[i])  # used textvariable instead
        encounterLb.grid(row=i % 40, column=(i // 40) * 6 + 1, sticky=W, pady=2)

        energyLabel = Label(master, textvariable=energy[i])  #
        energyLabel.grid(row=i % 40, column=(i // 40) * 6 + 2, sticky=W, pady=2)  #


startBt = Button(master, text="Start", command=maintable)
startBt.grid(row=0, column=0, sticky=W, pady=2)

mainloop()
