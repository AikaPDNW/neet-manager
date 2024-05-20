def sleepcal(m, rows, e, i):
    m[i].set(m[i].get() + 1)
    
    for c in range(rows):     
        
        if c>0: e[c].set(e[c-1].get() + m[c].get())
        else: e[0].set(m[0].get())
