from tkinter import *
from tkinter.ttk import * 
import time
from subprocess import call


def Start():
    bar_count = 100
    load = 0
    speed = 1
    while (load<bar_count):
        bar['value']+=(speed/bar_count)*100
        load += speed
        percent.set(str(int((load/bar_count)*100))+"%")
        time.sleep(0.2)
        root.update_idletasks() 
    while (load>=bar_count):
        root.destroy()
        call(["python","login.py"])
        
root = Tk()
root.geometry('500x450')
root.title('Progress')


button = Button(root, text="Start", command=Start).pack()
percent = StringVar()
text = StringVar()

texte_label = Label(root, text='Récupération des données',font=('Arial', 8))
texte_label.pack()

pourcent_label = Label(root, textvariable=percent)

bar= Progressbar(root, orient=HORIZONTAL, length=500)
bar.pack(pady=10)



root.mainloop()