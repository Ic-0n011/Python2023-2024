from textAnalyser import TextAnalyser
from tkinter import *
from tkinter import ttk
text_cmd = "привет"

def show_message():
    k = entry.get()     # получаем введенный текст
    if k.isdigit():
        wc_width = int(k)
        label["text"] = 
    

root = Tk()
root.geometry("500x300") 
 
entry = ttk.Entry()
entry.pack(anchor=NW, padx=6, pady=6)
  
btn = ttk.Button(text="Click", command=show_message)
btn.pack(anchor=NW, padx=6, pady=6)
 
label = ttk.Label()
label.pack(anchor=NW, padx=6, pady=6)
label["text"] = text_cmd
root.mainloop()