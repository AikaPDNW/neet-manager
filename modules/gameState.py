from collections import defaultdict

encounter = list()
energy = list()  #
acts = defaultdict(lambda: None)

# Action limit
rows = 100

class SleepAction:
    @staticmethod
    def action(m, i):
        m[i].set(m[i].get() + 1)
        acts[i] = 'Sleep'
        # update values

    @staticmethod
    def cancel(m, i):
        m[i].set(m[i].get() - 1)
        acts[i] = None

    @staticmethod
    def getLabel(i):
        return 'Sleep' if acts[i] == 'Sleep' else 'Act'