import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.geometry('1000x700')
root.title('Caisse')

label_trav = ttk.Label(root, text='Enregistrement client', font=('Arial', 25), background='gray')
btn_exit = tk.Button(root, text=' x ', font=('Arial', 10),fg='white', background='red')
#colonne 01
nom = ttk.Label(root, text='Nom du client',font=('Arial', 13))
entrer_nom = tk.Entry(root, font=('Bold', 11), width=30)

prenom = ttk.Label(root, text='Prénom du client',font=('Arial', 13))
entrer_prenom = tk.Entry(root, font=('Bold', 11), width=30)

sexe = ttk.Label(root, text='Sexe', font=('Arial', 13))
option_sexe = ["Homme", "Femme"]
entrer_sexe = ttk.Combobox(root, values= option_sexe, font=('Bold', 11), width=30)
entrer_sexe.current(0)

phone = ttk.Label(root, text='Numero de télephone', font=('Arial', 13))
entrer_phone = tk.Entry(root, font=('Bold', 11), width=30)

provenance = ttk.Label(root, text='Pays de provénance', font=('Arial', 13))
option_provenance = ["Autres", "Madagascar"]
entrer_provenance = ttk.Combobox(root, values= option_provenance, font=('Bold', 11), width=30)
entrer_provenance.current(0)

#colonne 02
num_carte = ttk.Label(root, text='Numero de carte', font=('Arial', 13))
entrer_num_carte = tk.Entry(root, font=('Bold', 11), width=30)

date_entree = ttk.Label(root, text='Date entrée', font=('Arial', 13))
entrer_date_entree = tk.Entry(root, font=('Bold', 11), width=30)

date_sortie= ttk.Label(root, text='Date sortie', font=('Arial', 13))
entrer_date_sortie = tk.Entry(root, font=('Bold', 11), width=30)

adresse = ttk.Label(root, text='Adresse', font=('Arial', 13))
entrer_adresse = tk.Entry(root, font=('Bold', 11), width=30)

#colonne 03

nb_lit = ttk.Label(root, text='Nombre de lit', font=('Arial', 13))
option_nb_lit = ["1", "2","3","4","5"]
entrer_nb_lit = ttk.Combobox(root, values= option_nb_lit, font=('Bold', 11), width=30)
entrer_nb_lit.current(0)

chambre = ttk.Label(root, text='Type de chambre', font=('Arial', 13))
option_chambre = ["Studio", "Penthouse"]
entrer_chambre = ttk.Combobox(root, values= option_chambre, font=('Bold', 11), width=30)
entrer_chambre.current(0)

num_chambre = ttk.Label(root, text='Numéro de chambre', font=('Arial', 13))
option_num_chambre = ["1", "2","3","4","5"]
entrer_num_chambre = ttk.Combobox(root, values= option_num_chambre, font=('Bold', 11), width=30)
entrer_num_chambre.current(0)

prix = ttk.Label(root, text='Prix', font=('Arial', 13))
entrer_prix = tk.Entry(root, font=('Bold', 11), width=30)

btn_inscrire = ttk.Button(root,text='Inscrire', width=20)
btn_effacer = ttk.Button(root,text='Effacer', width=20)


#création du grid
root.columnconfigure((0,1,2), weight=1)

root.rowconfigure(0, weight=1)
root.rowconfigure((1,2,3,4,5), weight=3)

label_trav.grid(row=0, column=0, columnspan=3, sticky='nsew')
btn_exit.grid(row=0, column=0, columnspan=3, sticky='ne')
#colonne 1
nom.grid(row=1, column=0, sticky='nw', padx=10, pady=10)
entrer_nom.grid(row=1, column =0,sticky='w', padx=10, pady=10)

prenom.grid(row=2, column=0, sticky='nw', padx=10, pady=10)
entrer_prenom.grid(row=2, column =0,sticky='w', padx=10, pady=10)

sexe.grid(row=3, column=0, sticky='nw', padx=10, pady=10)
entrer_sexe.grid(row=3, column =0,sticky='w', padx=10)

phone.grid(row=4, column=0, sticky='nw', padx=10, pady=10)
entrer_phone.grid(row=4, column =0,sticky='w', padx=10, pady=10)

provenance.grid(row=5, column=0, sticky='nw', padx=10, pady=10)
entrer_provenance.grid(row=5, column =0,sticky='w', padx=10, pady=10)

#colonne 2
num_carte.grid(row=1, column=1, sticky='nw', padx=10, pady=10)
entrer_num_carte.grid(row=1, column =1,sticky='w', padx=10, pady=10)

date_entree.grid(row=2, column=1, sticky='nw', padx=10, pady=10)
entrer_date_entree.grid(row=2, column =1,sticky='w', padx=10, pady=10)

date_sortie.grid(row=3, column=1, sticky='nw', padx=10, pady=10)
entrer_date_sortie.grid(row=3, column =1,sticky='w', padx=10, pady=10)

adresse.grid(row=4, column=1, sticky='nw', padx=10, pady=10)
entrer_adresse.grid(row=4, column =1,sticky='w', padx=10, pady=10)
#colonne 3
nb_lit.grid(row=1, column=2, sticky='nw', padx=10, pady=10)
entrer_nb_lit.grid(row=1, column =2,sticky='w', padx=10, pady=10)

chambre.grid(row=2, column=2, sticky='nw', padx=10, pady=10)
entrer_chambre.grid(row=2, column =2,sticky='w', padx=10, pady=10)

num_chambre.grid(row=3, column=2, sticky='nw', padx=10, pady=10)
entrer_num_chambre.grid(row=3, column =2,sticky='w', padx=10, pady=10)

prix.grid(row=4, column=2, sticky='nw', padx=10, pady=10)
entrer_prix.grid(row=4, column =2,sticky='w', padx=10, pady=10)

btn_inscrire.grid(row=5, column=2, sticky='nw', padx=20, pady=10)
btn_effacer.grid(row=5, column=2, sticky='ne', padx=20, pady=10)


root.mainloop()