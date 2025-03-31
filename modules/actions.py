from modules.gameState import acts

class SleepAction:
    @staticmethod
    def action(m, i):
        m[i].set(m[i].get() + 1)
        acts[i] = 'Sleep'
        # update values

    @staticmethod
    def sleep_action(tdelta, sdelta, ensumm, i):
        tdelta[i].set(tdelta[i].get() + sdelta.get())
        ensumm[i].set(ensumm[i].get() + sdelta.get()*10)
        if ensumm[i].get() > 100:
            ensumm[i].set(100)
        acts[i] = 'Sleep'

    @staticmethod
    def cancel(m, i):
        m[i].set(m[i].get() - 1)
        acts[i] = None

    @staticmethod
    def getLabel(i):
        return 'Sleep' if acts[i] == 'Sleep' else 'Act'