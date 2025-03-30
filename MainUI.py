from tkinter import *
from tkinter.ttk import *

from modules.gameState import tsumm, date, tdelta, ensumm, msumm, hsumm, rows, init_state
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
        tempBt.grid(row=i % 40, column=(i // 40) * 7, sticky=W, pady=2)
        actBt.append(tempBt)

        tdeltaLabel = Label(master, textvariable=tdelta[i])  # used textvariable instead
        tdeltaLabel.grid(row=i % 40, column=(i // 40) * 7 + 1, sticky=W, pady=2)

        tsummLabel = Label(master, textvariable=tsumm[i])  #
        tsummLabel.grid(row=i % 40, column=(i // 40) * 7 + 2, sticky=W, pady=2)  #

        dateLabel = Label(master, textvariable=date[i])  #
        dateLabel.grid(row=i % 40, column=(i // 40) * 7 + 3, sticky=W, pady=2)  #

        energyLabel = Label(master, textvariable=ensumm[i])  #
        energyLabel.grid(row=i % 40, column=(i // 40) * 7 + 4, sticky=W, pady=2)  #

        moneyLabel = Label(master, textvariable=msumm[i])  #
        moneyLabel.grid(row=i % 40, column=(i // 40) * 7 + 5, sticky=W, pady=2)  #

        happinessLabel = Label(master, textvariable=hsumm[i])  #
        happinessLabel.grid(row=i % 40, column=(i // 40) * 7 + 6, sticky=W, pady=2)  #


startBt = Button(master, text="Start", command=maintable)
startBt.grid(row=0, column=0, sticky=W, pady=2)

mainloop()
