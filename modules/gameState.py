from collections import defaultdict
from tkinter import IntVar
import datetime
from datetime import timedelta

encounter = list()
time = list()  #
acts = defaultdict(lambda: None)
date = list()

# Action limit
rows = 100
date0 = datetime.datetime(2022,12,25,11,34)

def make_updater(i, en, t,):
    def update(*args):
        if i > 0:
            t[i].set(date.hour[i - 1] + en[i].get())
            date[i] = date[i-1] + timedelta(hours = en[i].get())
        else:
            t[i].set(date0.hour + en[i].get())
            date[i] = date[i] + timedelta(hours=en[i].get())


    return update


def make_updater_t(i, en, t):
    def update(*args):
        if i < len(t) - 1:
            t[i + 1].set(date[i] + en[i + 1].get())
            date[i+1] = date[i] + timedelta(hours=en[i+1].get())

    return update



def init_state():
    for i in range(rows):
        # create an instance of IntVar() and append to list m
        encounter.append(IntVar())
        time.append(IntVar())  #
        date.append(datetime.datetime())


        encounter[i].trace_add("write", make_updater(i, encounter, time))
        time[i].trace_add("write", make_updater_t(i, encounter, time))
