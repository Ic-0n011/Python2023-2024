import tkinter
from textAnalyser import TextAnalyser


def run():
    TextAnalyser(
        source_file="text.txt",
        parts_of_speech=["NOUN", "VERB"],
        words_ammount=int(words_ammount.get())
        )


window = tkinter.Tk()
window.geometry("1100x600+100+200")

words_ammount = tkinter.Entry(window)
words_ammount.pack()

btn = tkinter.Button(window, text="Click", command=run)
btn.pack()

window.mainloop()
