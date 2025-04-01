from modules.gameState import acts

class Actions       :
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
    def clean_action(tdelta, cleanActs_var, cleanActs, ensumm, i):
        if cleanActs_var.get() == cleanActs[1]:
            tdelta[i].set(tdelta[i].get() + 1)
            ensumm[i].set(ensumm[i].get() - 10)

        elif cleanActs_var.get() == cleanActs[2]:
            tdelta[i].set(tdelta[i].get() + 2)
            ensumm[i].set(ensumm[i].get() - 20)

        acts[i] = 'Clean'

        if ensumm[i].get() > 100:
            ensumm[i].set(100)

        if ensumm[i].get() < 0:
            ensumm[i].set(0)

    @staticmethod
    def cook_action(tdelta, cookActs_var, cookActs, ensumm, hsumm, i):
        if cookActs_var.get() == cookActs[1]:
            tdelta[i].set(tdelta[i].get() + 1)
            ensumm[i].set(ensumm[i].get() - 10)

        elif cookActs_var.get() == cookActs[2]:
            tdelta[i].set(tdelta[i].get() + 2)
            ensumm[i].set(ensumm[i].get() - 20)
            hsumm[i].set(hsumm[i].get() + 10)

        acts[i] = 'Clean'

        if hsumm[i].get() > 100:
            hsumm[i].set(100)

        if hsumm[i].get() < 0:
            hsumm[i].set(0)

        if ensumm[i].get() > 100:
            ensumm[i].set(100)

        if ensumm[i].get() < 0:
            ensumm[i].set(0)

    @staticmethod
    def cancel(m, i):
        m[i].set(m[i].get() - 1)
        acts[i] = None

    @staticmethod
    def getLabel(i):
        return 'Sleep' if acts[i] == 'Sleep' else 'Act'