sdelta = IntVar()

    btSle = Button(ActionWindow, text="Sleep", command=lambda idx=i: commit_action(bt, idx, SleepAction, ActionWindow))
    btSle.place(x=0, y=0)

    verticalScale = Scale(ActionWindow, orient=VERTICAL, length=200, from_=1.0, to=8.0, variable = sdelta)
    verticalScale.pack()
    verticalScale.place(x=0, y=30)