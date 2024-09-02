import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.geometry('1000x700')
root.title('Travailleur')

label_trav = ttk.Label(root, text='Enregistrement Travailleur', font=('Arial', 25), background='gray')
btn_exit = tk.Button(root, text=' x ', font=('Arial', 10),fg='white', background='red')

nom = ttk.Label(root, text='Nom',font=('Arial', 13))
entrer_nom = tk.Entry(root, font=('Bold', 11), width=30)

prenom = ttk.Label(root, text='Prénom',font=('Arial', 13))
entrer_prenom = tk.Entry(root, font=('Bold', 11), width=30)

sexe = ttk.Label(root, text='Sexe', font=('Arial', 13))
option_sexe = ["Homme", "Femme"]
entrer_sexe = ttk.Combobox(root, values= option_sexe, font=('Bold', 11), width=30)
entrer_sexe.current(0)


phone = ttk.Label(root, text='Télephone', font=('Arial', 13))
entrer_phone = tk.Entry(root, font=('Bold', 11), width=30)

civilite = ttk.Label(root, text='Civilité', font=('Arial', 13))
option_civilite = ["Célibataire", "Marié"]
entrer_civilite = ttk.Combobox(root, values= option_civilite, font=('Bold', 11), width=30)
entrer_civilite.current(0)

date_naissance = ttk.Label(root, text='Date de naissance', font=('Arial', 13))
entrer_date_naissance = tk.Entry(root, font=('Bold', 11), width=30)

poste = ttk.Label(root, text='Poste', font=('Arial', 13))
option_poste = ["Sécurité", "Serveur", "Réceptionniste"]
entrer_poste = ttk.Combobox(root, values= option_poste, font=('Bold', 11), width=30)
entrer_poste.current(0)

adresse = ttk.Label(root, text='Adresse', font=('Arial', 13))
entrer_adresse = tk.Entry(root, font=('Bold', 11), width=30)

num_carte = ttk.Label(root, text='Numero de carte', font=('Arial', 13))
entrer_num_carte = tk.Entry(root, font=('Bold', 11), width=30)

salaire = ttk.Label(root, text='Salaire', font=('Arial', 13))
entrer_salaire = tk.Entry(root, font=('Bold', 11), width=30)

btn_enregister = ttk.Button(root,text='Enregistrer', width=20)
btn_rechercher = ttk.Button(root,text='Rechercher', width=20)
btn_modifier = ttk.Button(root,text='Modifier', width=20)
btn_supprimer = ttk.Button(root,text='Supprimer', width=20)


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
#colonne 2
civilite.grid(row=1, column=1, sticky='nw', padx=10, pady=10)
entrer_civilite.grid(row=1, column =1,sticky='w', padx=10, pady=10)

date_naissance.grid(row=2, column=1, sticky='nw', padx=10, pady=10)
entrer_date_naissance.grid(row=2, column =1,sticky='w', padx=10, pady=10)

poste.grid(row=3, column=1, sticky='nw', padx=10, pady=10)
entrer_poste.grid(row=3, column =1,sticky='w', padx=10, pady=10)

adresse.grid(row=4, column=1, sticky='nw', padx=10, pady=10)
entrer_adresse.grid(row=4, column =1,sticky='w', padx=10, pady=10)
#colonne 3
num_carte.grid(row=1, column=2, sticky='nw', padx=10, pady=10)
entrer_num_carte.grid(row=1, column =2,sticky='w', padx=10, pady=10)

salaire.grid(row=2, column=2, sticky='nw', padx=10, pady=10)
entrer_salaire.grid(row=2, column =2,sticky='w', padx=10, pady=10)

btn_enregister.grid(row=3, column=2, sticky='nw', padx=20, pady=10)
btn_rechercher.grid(row=3, column=2, sticky='ne', padx=20, pady=10)
btn_modifier.grid(row=3, column=2, sticky='sw', padx=20, pady=10)
btn_supprimer.grid(row=3, column=2, sticky='se', padx=20, pady=10)

root.mainloop()