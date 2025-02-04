from tkinter import *
from tkinter.ttk import *

from modules.gameState import energy, encounter, rows, init_state
from modules.actionWindowUI import openActionWindow

master = Tk()
master.state('zoomed')
master.title("NEET manager")

actBt = list()


def maintable():
    init_state()
    for i in range(rows):
        tempBt = Button(master, text="Act", command=lambda idx=i: openActionWindow(actBt,
                                                                                                  idx, rows))  # assign the lambda to command
        tempBt.grid(row=i % 40, column=(i // 40) * 6, sticky=W, pady=2)
        actBt.append(tempBt)

        encounterLb = Label(master, textvariable=encounter[i])  # used textvariable instead
        encounterLb.grid(row=i % 40, column=(i // 40) * 6 + 1, sticky=W, pady=2)

        energyLabel = Label(master, textvariable=energy[i])  #
        energyLabel.grid(row=i % 40, column=(i // 40) * 6 + 2, sticky=W, pady=2)  #


startBt = Button(master, text="Start", command=maintable)
startBt.grid(row=0, column=0, sticky=W, pady=2)

mainloop()
