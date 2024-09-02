import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.geometry('820x700')
root.title('Switch')


def Switch(_actif, page):
    for child in options_fm.winfo_children():
        if isinstance(child, tk.Label):
            child['bg']= 'SystemButtonFace'
            
    _actif['bg'] = '#0097e8'
    
    for fm in main_fm.winfo_children():
        fm.destroy()
        root.update()
    
    page()
    


#création du conteneur des menus
options_fm = tk.Frame(root)

options_fm.pack(pady = 5)

options_fm.pack_propagate(False)
options_fm.configure(width=820, height=35)

#contenu
btn_caisse = tk.Button(options_fm, text = 'Caisse', font=('Arial', 15),bd = 0, fg='#0097e8', activeforeground='#0097a5',
                      command= lambda:Switch(_actif=caisse_actif, page=page_caisse))
btn_caisse.place(x=0, y=0, width=115)

btn_chambre = tk.Button(options_fm, text = 'Chambre', font=('Arial', 15),bd = 0, fg='#0097e8', activeforeground='#0097a5',
                        command= lambda:Switch(_actif=chambre_actif, page=page_chambre))
btn_chambre.place(x=115, y=0, width=115)

btn_admin = tk.Button(options_fm, text = 'Admin', font=('Arial', 15),bd = 0, fg='#0097e8', activeforeground='#0097a5',
                      command= lambda:Switch(_actif=admin_actif, page=page_admin))
btn_admin.place(x=220, y=0, width=115)

btn_client = tk.Button(options_fm, text = 'Client', font=('Arial', 15),bd = 0, fg='#0097e8', activeforeground='#0097a5',
                      command= lambda:Switch(_actif=client_actif, page=page_client))
btn_client.place(x=335, y=0, width=115)

btn_travailleur = tk.Button(options_fm, text = 'Travailleur', font=('Arial', 15),bd = 0, fg='#0097e8', activeforeground='#0097a5',
                      command= lambda:Switch(_actif=travailleur_actif, page=page_travailleur))
btn_travailleur.place(x=445, y=0, width=120)

btn_statistic = tk.Button(options_fm, text = 'Statistique', font=('Arial', 15),bd = 0, fg='#0097e8', activeforeground='#0097a5',
                      command= lambda:Switch(_actif=statistic_actif, page=page_statistic))
btn_statistic.place(x=565, y=0, width=120)

btn_param = tk.Button(options_fm, text = 'Paramètre', font=('Arial', 15),bd = 0, fg='#0097e8', activeforeground='#0097a5',
                      command= lambda:Switch(_actif=param_actif, page=page_param))
btn_param.place(x=680, y=0, width=140)

btn_exit = tk.Button(options_fm, text = 'Quitter',font=('Arial', 10),bd = 0, fg='#ff0000', activeforeground='#0097a5')
btn_exit.place(x=650, y=650)

#ligne de l'actif
caisse_actif = tk.Label(options_fm, bg = '#0097e8')
caisse_actif.place(x = 22, y = 30, height= 2, width=72)

chambre_actif = tk.Label(options_fm)
chambre_actif.place(x = 137, y = 30, height= 2, width=72)

admin_actif = tk.Label(options_fm)
admin_actif.place(x = 242, y = 30, height= 2, width=72)

client_actif = tk.Label(options_fm)
client_actif.place(x = 357, y = 30, height= 2, width=72)

travailleur_actif = tk.Label(options_fm)
travailleur_actif.place(x = 470, y = 30, height= 2, width=72)

statistic_actif = tk.Label(options_fm)
statistic_actif.place(x = 587, y = 30, height= 2, width=72)

param_actif = tk.Label(options_fm)
param_actif.place(x = 712, y = 30, height= 2, width=72)

main_fm = tk.Frame(root)
main_fm.pack(fill = tk.BOTH, expand=True)



def page_caisse():
    page_caisse_fm = tk.Frame(main_fm)
    page_caisse_lb = tk.Label(page_caisse_fm, text='Hello Caisse', font=('Arial', 20), fg = '#0097e8')
    
    page_caisse_lb.pack()
    
    page_caisse_fm.pack(fill=tk.BOTH, expand=True)
    
def page_client():
    page_client_fm = tk.Frame(main_fm)
    page_client_lb = tk.Label(page_client_fm, text='Hello Client', font=('Arial', 20), fg = '#0097e8')
    
    page_client_lb.pack()
    
    page_client_fm.pack(fill=tk.BOTH, expand=True)
    
def page_chambre():
    page_chambre_fm = tk.Frame(main_fm)
    page_chambre_lb = tk.Label(page_chambre_fm, text='Hello Chambre', font=('Arial', 20), fg = '#0097e8')
    
    page_chambre_lb.pack()
    
    page_chambre_fm.pack(fill=tk.BOTH, expand=True)
    
def page_admin():
    page_admin_fm = tk.Frame(main_fm)
    page_admin_lb = tk.Label(page_admin_fm, text='Hello Admin', font=('Arial', 20), fg = '#0097e8')
    
    page_admin_lb.pack()
    
    page_admin_fm.pack(fill=tk.BOTH, expand=True)
    
def page_statistic():
    page_statistic_fm = tk.Frame(main_fm)
    page_statistic_lb = tk.Label(page_statistic_fm, text='Hello Statistic', font=('Arial', 20), fg = '#0097e8')
    
    page_statistic_lb.pack()
    
    page_statistic_fm.pack(fill=tk.BOTH, expand=True)
    
def page_travailleur():
    page_travailleur_fm = tk.Frame(main_fm)
    page_travailleur_lb = tk.Label(page_travailleur_fm, text='Hello Travailleur', font=('Arial', 20), fg = '#0097e8')
    
    page_travailleur_lb.pack()
    
    page_travailleur_fm.pack(fill=tk.BOTH, expand=True)    
    
    
def page_param():
    page_param_fm = tk.Frame(main_fm)
    page_param_lb = tk.Label(page_param_fm, text='Hello Paramètre', font=('Arial', 20), fg = '#0097e8')
    
    page_param_lb.pack()
    
    page_param_fm.pack(fill=tk.BOTH, expand=True)
    
main_fm = tk.Frame(root)
main_fm.pack(fill=tk.BOTH, expand=True)
    
                            
page_caisse()
root.mainloop()
