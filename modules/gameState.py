from collections import defaultdict
from tkinter import IntVar, StringVar
import datetime
from datetime import timedelta

tdelta = list()
tsumm = list()  #
date = list()

endelta = list()
ensumm = list()

mdelta = list()
msumm = list()

hdelta = list()
hsumm = list()

acts = defaultdict(lambda: None)

# Action limit
rows = 100
date0 = datetime.datetime(2022,12,25,11,34)

def make_updater_delta(i, td, ts):
    def update(*args):
        if i > 0:
            ts[i].set(ts[i - 1].get() + td[i].get())

        else:
            ts[i].set(td[i].get())

    return update


def make_updater_sum(i, td, ts):
    def update(*args):
        date[i].set((date0 + timedelta(hours=ts[i].get())).strftime('  %H:%M   %d.%m  '))
        if i < len(ts) - 1:
            ts[i + 1].set(ts[i].get() + td[i + 1].get())

    return update


def init_state():
    for i in range(rows):
        # create an instance of IntVar() and append to list m
        tdelta.append(IntVar())
        tsumm.append(IntVar())  #
        date.append(StringVar())
        endelta.append(IntVar())
        ensumm.append(IntVar())
        mdelta.append(IntVar())
        msumm.append(IntVar())
        hdelta.append(IntVar())
        hsumm.append(IntVar())

        tdelta[i].trace_add("write", make_updater_delta(i, tdelta, tsumm))
        tsumm[i].trace_add("write", make_updater_sum(i, tdelta, tsumm))