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

def make_updater_tdelta(i, td, ts):
    def update(*args):
        #time
        if i > 0:
            ts[i].set(ts[i - 1].get() + td[i].get())

        else:
            ts[i].set(td[i].get())


    return update

def make_updater_tsum(i, td, ts):
    def update(*args):
        #time
        date[i].set((date0 + timedelta(hours=ts[i].get())).strftime('  %H:%M   %d.%m  '))
        if i < len(ts) - 1:
            ts[i + 1].set(ts[i].get() + td[i + 1].get())

    return update


#energy updater
def make_updater_endelta(i, end, ens):
    def update(*args):
        if i > 0:
            ens[i].set(ens[i - 1].get() + end[i].get())

        else:
            ens[i].set(end[i].get())

    return update

def make_updater_ensum(i, end, ens):
    def update(*args):
        if i < len(ens) - 1:
            ens[i + 1].set(ens[i].get() + end[i + 1].get())

    return update

#money updater
def make_updater_mdelta(i, md, ms):
    def update(*args):
        if i > 0:
            ms[i].set(ms[i - 1].get() + md[i].get())

        else:
            ms[i].set(md[i].get())

    return update

def make_updater_msum(i, md, ms):
    def update(*args):
        if i < len(ms) - 1:
            ms[i + 1].set(ms[i].get() + md[i + 1].get())

    return update

#happiness updater
def make_updater_hdelta(i, hd, hs):
    def update(*args):
        if i > 0:
            hs[i].set(hs[i - 1].get() + hd[i].get())

        else:
            hs[i].set(hd[i].get())

    return update

def make_updater_hsum(i, hd, hs):
    def update(*args):
        if i < len(hs) - 1:
            hs[i + 1].set(hs[i].get() + hd[i + 1].get())

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

        tdelta[i].trace_add("write", make_updater_tdelta(i, tdelta, tsumm))
        tsumm[i].trace_add("write", make_updater_tsum(i, tdelta, tsumm))

        endelta[i].trace_add("write", make_updater_endelta(i, endelta, ensumm))
        ensumm[i].trace_add("write", make_updater_ensum(i, endelta, ensumm))

        mdelta[i].trace_add("write", make_updater_mdelta(i, mdelta, msumm))
        msumm[i].trace_add("write", make_updater_msum(i, mdelta, msumm))

        hdelta[i].trace_add("write", make_updater_hdelta(i, hdelta, hsumm))
        hsumm[i].trace_add("write", make_updater_hsum(i, hdelta, hsumm))