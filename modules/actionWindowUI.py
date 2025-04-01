from tkinter import *
from tkinter import ttk
from tkinter import IntVar,StringVar
from modules.gameState import tdelta, hsumm, ensumm, rows
from modules.actions import Actions

cleanActs = ['None', 'Washing the dishes', 'Vacuuming the room']
cookActs = ['None', 'Struggle meal', 'Fancy meal']
workActs = ['None', 'Full shift', "Half shift"]
studyActs = ['None', 'Languages', 'Coding']
gymActs = ['None', 'Intense session', 'Chill session']
socialActs = ['None', 'Playing online games', 'Playing board games', 'Bar']
hobbyActs = ['None', 'Painting miniatures', 'Playing single games']

def cancel_action(bt, i, action):
    action.cancel(tdelta, i)
    bt[i].configure(text=action.getLabel(i), command=lambda idx=i: openActionWindow(bt, idx, rows))


def commit_action(bt, i, sdelta, cleanActs_var, cleanActs, cookActs_var, cookActs, action, window):
    if sdelta.get() > 0:
        action.sleep_action(tdelta, sdelta, ensumm, i)
    elif cleanActs_var.get() != 'None':
        action.clean_action(tdelta, cleanActs_var, cleanActs, ensumm, i)
    elif cookActs_var.get() != 'None':
        action.cook_action(tdelta, cookActs_var, cookActs, ensumm, hsumm, i)
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
    ActionWindow.geometry("800x500")
    for c in range(rows):
        bt[c].configure(state=["disabled"])

    bt[i].configure(state=["active"])

    applyBt = Button(ActionWindow, text="Apply Changes", command=lambda idx=i: commit_action(bt, idx, sdelta, cleanActs_var, cleanActs, cookActs_var, cookActs, Actions, ActionWindow))
    applyBt.grid(row=0, column=1, sticky=W, pady=2)

    sleepLb = Label(ActionWindow, text = "Sleep")
    sleepLb.grid(row=0, column=0, sticky=W, pady=2)

    sdelta = IntVar()
    sleepScale = Scale(ActionWindow, orient=HORIZONTAL, length=200, from_=0.0, to=8.0, variable = sdelta)
    sleepScale.grid(row=1, column=0, sticky=W, pady=2)

    cleanLb = Label(ActionWindow, text="Clean")
    cleanLb.grid(row=3, column=0, sticky=W, pady=2)

    cleanActs_var = StringVar(value=cleanActs[0])
    cleanCombobox = ttk.Combobox(ActionWindow, textvariable=cleanActs_var, values = cleanActs, state ='readonly')
    cleanCombobox.grid(row=4, column=0, sticky=W, pady=2)

    cookLb = Label(ActionWindow, text="Cook")
    cookLb.grid(row=6, column=0, sticky=W, pady=2)

    cookActs_var = StringVar(value=cookActs[0])
    cookCombobox = ttk.Combobox(ActionWindow, textvariable=cookActs_var, values=cookActs, state='readonly')
    cookCombobox.grid(row=7, column=0, sticky=W, pady=2)

    workLb = Label(ActionWindow, text="Work")
    workLb.grid(row=9, column=0, sticky=W, pady=2)

    n3 = StringVar()
    workCombobox = ttk.Combobox(ActionWindow, textvariable=n3)
    workCombobox['values'] = ('a', 'b')
    workCombobox.grid(row=10, column=0, sticky=W, pady=2)

    studyLb = Label(ActionWindow, text="Study")
    studyLb.grid(row=12, column=0, sticky=W, pady=2)

    n4 = StringVar()
    studyCombobox = ttk.Combobox(ActionWindow, textvariable=n4)
    studyCombobox['values'] = ('a', 'b')
    studyCombobox.grid(row=13, column=0, sticky=W, pady=2)

    gymLb = Label(ActionWindow, text="Gym")
    gymLb.grid(row=15, column=0, sticky=W, pady=2)

    n5 = StringVar()
    gymCombobox = ttk.Combobox(ActionWindow, textvariable=n5)
    gymCombobox['values'] = ('a', 'b')
    gymCombobox.grid(row=16, column=0, sticky=W, pady=2)

    socialLb = Label(ActionWindow, text="Social")
    socialLb.grid(row=18, column=0, sticky=W, pady=2)

    n6 = StringVar()
    socialCombobox = ttk.Combobox(ActionWindow, textvariable=n6)
    socialCombobox['values'] = ('a', 'b')
    socialCombobox.grid(row=19, column=0, sticky=W, pady=2)

    hobbyLb = Label(ActionWindow, text="Hobby")
    hobbyLb.grid(row=21, column=0, sticky=W, pady=2)

    n7 = StringVar()
    hobbyCombobox = ttk.Combobox(ActionWindow, textvariable=n7)
    hobbyCombobox['values'] = ('a', 'b')
    hobbyCombobox.grid(row=22, column=0, sticky=W, pady=2)