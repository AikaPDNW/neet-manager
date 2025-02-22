from collections import defaultdict
from tkinter import IntVar, StringVar
import datetime
from datetime import timedelta

encounter = list()
energy = list()  #
acts = defaultdict(lambda: None)
date = list()

# Action limit
rows = 100
date0 = datetime.datetime(2022,12,25,11,34)

def make_updater(i, m, e):
    def update(*args):
        if i > 0:
            e[i].set(e[i - 1].get() + m[i].get())

        else:
            e[i].set(m[i].get())

    return update


def make_updater_e(i, m, e):
    def update(*args):
        date[i].set((date0 + timedelta(hours=e[i].get())).strftime('%d,%m,%Y,%H,%M'))
        if i < len(e) - 1:
            e[i + 1].set(e[i].get() + m[i + 1].get())

    return update


def init_state():
    for i in range(rows):
        # create an instance of IntVar() and append to list m
        encounter.append(IntVar())
        energy.append(IntVar())  #
        date.append(StringVar())

        encounter[i].trace_add("write", make_updater(i, encounter, energy))
        energy[i].trace_add("write", make_updater_e(i, encounter, energy))