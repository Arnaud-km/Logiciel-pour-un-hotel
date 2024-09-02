import customtkinter as ctk
import tkinter as tk

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")

def Oublie():
    print('salut')

login = ctk.CTk()
login.geometry("500x350")

frame = ctk.CTkFrame(master=login)
frame.pack(pady= 20, padx=60, fill = "both", expand=True)

label = ctk.CTkLabel(master=frame, text="Authentification")
label.pack (pady=12, padx=10)

entrer_mail = ctk.CTkEntry(master=frame, placeholder_text="Entrer votre mail", font=('Arial', 12))
entrer_mail.pack(pady=12)
entrer_mdp = ctk.CTkEntry(master=frame, placeholder_text="Mot de passe", show="*")
entrer_mdp.pack(pady=12)

btn_connexion = ctk.CTkButton(master=frame, text='Connexion', command=Oublie)
btn_connexion.pack(padx=10, pady=12)

label_oublié = tk.Button(master=frame, text = 'Mot de passe oublié', command=Oublie, font=('Arial', 9), background='#999999')
label_oublié.pack(pady=12, padx=10)


login.mainloop()