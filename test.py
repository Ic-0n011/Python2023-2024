import tkinter as tk


dollar = 97


window = tk.Tk()
window.geometry("800x600+100+200")


def change_label_text():

    rub = float(entry.get())
    usd = 97.75
    cny = 13.31
    byn = 38.73

    label_cny['text'] = str(rub / cny) + "Китайский юань"
    label_byn['text'] = str(rub / byn) + "Белорусский рубль"
    label_usd['text'] = str(rub / usd) + "доллар США"


entry = tk.Entry()
entry.pack()

btn = tk.Button(text="Click", command=change_label_text)
btn.pack()

label = tk.Label()
label.pack()


label = tk.Label(window, text='Измеритель глубины рубля')
label.pack()
label_usd = tk.Label(window, text="")
label_cny = tk.Label(window, text="")
label_byn = tk.Label(window, text="")
label_usd.pack()
label_byn.pack()
label_cny.pack()


#запуск окна
window.mainloop()
