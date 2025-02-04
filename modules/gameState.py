from collections import defaultdict
from tkinter import IntVar

encounter = list()
energy = list()  #
acts = defaultdict(lambda: None)

# Action limit
rows = 100


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


def init_state():
    for i in range(rows):
        # create an instance of IntVar() and append to list m
        encounter.append(IntVar())
        energy.append(IntVar())  #

        encounter[i].trace_add("write", make_updater(i, encounter, energy))
        energy[i].trace_add("write", make_updater_e(i, encounter, energy))