from tkinter import *
from tkinter import IntVar
from modules.gameState import tdelta, rows
from modules.actions import SleepAction

def cancel_action(bt, i, action):
    action.cancel(tdelta, i)
    bt[i].configure(text=action.getLabel(i), command=lambda idx=i: openActionWindow(bt, idx, rows))


def commit_action(bt, i, action, window):
    action.action(tdelta, i)
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

    sleepLb = Label(ActionWindow, text = "Sleep")
    sleepLb.grid(row=0, column=0, sticky=W, pady=2)

    sdelta = IntVar()

    sleepScale = Scale(ActionWindow, orient=HORIZONTAL, length=200, from_=1.0, to=8.0, variable = sdelta)
    sleepScale.grid(row=1, column=0, sticky=W, pady=2)

    cleanLb = Label(ActionWindow, text="Sleep")
    cleanLb.grid(row=3, column=0, sticky=W, pady=2)

    languages = ["Python", "C#", "Java", "JavaScript"]
    cleanCombobox = Combobox(values=languages)
    cleanCombobox.grid(row=4, column=0, sticky=W, pady=2)

    cookLb = Label(ActionWindow, text="Sleep")
    cookLb.grid(row=6, column=0, sticky=W, pady=2)

    workLb = Label(ActionWindow, text="Sleep")
    workLb.grid(row=9, column=0, sticky=W, pady=2)

    studyLb = Label(ActionWindow, text="Sleep")
    studyLb.grid(row=12, column=0, sticky=W, pady=2)

    gymLb = Label(ActionWindow, text="Sleep")
    gymLb.grid(row=15, column=0, sticky=W, pady=2)

    socialLb = Label(ActionWindow, text="Sleep")
    socialLb.grid(row=18, column=0, sticky=W, pady=2)

    hobbyLb = Label(ActionWindow, text="Sleep")
    hobbyLb.grid(row=21, column=0, sticky=W, pady=2)
