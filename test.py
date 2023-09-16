import tkinter



window = tkinter.Tk()
checkButton1_cheked = tkinter.StringVar()
checkButton1 = tkinter.Checkbutton(window,
                                    text="существительное",
                                    onvalue="iii",
                                    offvalue="",
                                    variable=checkButton1_cheked)
checkButton1.pack()
checkButton2_cheked = tkinter.StringVar()
checkButton2 = tkinter.Checkbutton(window,
                                    text="Глагол",
                                    onvalue="qwq",
                                    offvalue="",
                                    variable=checkButton1_cheked)
checkButton2.pack()
checkButton3_cheked = tkinter.StringVar()
checkButton3 = tkinter.Checkbutton(window,
                                    text="причастие",
                                    onvalue="уку",
                                    offvalue="",
                                    variable=checkButton1_cheked)
checkButton3.pack()
checkButton4_cheked = tkinter.StringVar()
checkButton4 = tkinter.Checkbutton(window,
                                    text="прилагательное",
                                    onvalue="апа",
                                    offvalue="",
                                    variable=checkButton1_cheked)
checkButton4.pack()
pos = []
def run(pos):
    if checkButton1_cheked.get():
        pos.append(checkButton1_cheked.get())
    if checkButton2_cheked.get():
        pos.append(checkButton2_cheked.get())
    if checkButton3_cheked.get():
        pos.append(checkButton3_cheked.get())
    if checkButton4_cheked.get():
        pos.append(checkButton4_cheked.get())
    print(pos)


buttton = tkinter.Button(window, command=run(pos))
buttton.pack()
window.mainloop()