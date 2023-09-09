from tkinter import *
from tkinter import ttk
 
def show_message():
    label["text"] = entry.get()     # получаем введенный текст
 
root = Tk()
root.title("METANIT.COM")
root.geometry("600x600") 
 
entry = ttk.Entry()
entry.pack(anchor=NW, padx=10, pady=10)
  
btn = ttk.Button(text="Click", command=show_message)
btn.pack(anchor=NW, padx=10, pady=10)
 
label = ttk.Label()
label.pack(anchor=NW, padx=10, pady=10)
  
root.mainloop()