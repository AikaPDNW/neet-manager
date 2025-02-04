from tkinter import *
from modules.gameState import encounter, rows
from modules.actions import SleepAction

def cancel_action(bt, i, action):
    action.cancel(encounter, i)
    bt[i].configure(text=action.getLabel(i), command=lambda idx=i: openActionWindow(bt, idx, rows))


def commit_action(bt, i, action, window):
    action.action(encounter, i)
    bt[i].configure(text=action.getLabel(i), command=lambda idx=i: cancel_action(bt, i, action))
    window.destroy()

    for c in range(rows):
        bt[c].configure(state=["normal"])

def openActionWindow(bt, i, rows,):
    # Toplevel object which will
    # be treated as a new window
    ActionWindow = Toplevel()

    # sets the title of the
    # Toplevel widget
    ActionWindow.title("Action")

    # sets the geometry of toplevel
    ActionWindow.geometry("800x400")
    for c in range(rows):
        bt[c].configure(state=["disabled"])

    bt[i].configure(state=["active"])
    for r in range(6):
        btSle = Button(ActionWindow, text="Sleep", command=lambda idx=i: commit_action(bt, idx, SleepAction, ActionWindow))
        btSle.grid(row=r, column=1, sticky=W, pady=2)