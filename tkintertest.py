import tkinter as tk

def is_valid_email(email):
  if "@" in email and "." in email:
    return True
  return False

def is_valid_mdp(mdp):
  has_upper = any(c.isupper() for c in mdp)
  has_lower = any(c.islower() for c in mdp)
  has_digit = any(c.isdigit() for c in mdp)
  
  return has_upper and has_lower and has_digit

def action_bouton():
  pseudo = champ_texte_pseudo.get()
  email = champ_texte_email.get()
  mdp = champ_texte_mdp.get()
  if pseudo and email and mdp:
    if is_valid_email(email) and is_valid_mdp(mdp):
      etiquette.config(text="Bravo " + pseudo + " tu es inscrit avec ton email : " + email)
      print("pseudo : " + pseudo + " / email : " + email + " / mdp : " + mdp)
    else:
      etiquette.config(text="Votre email ou mot de passe ne sont pas au bon format")
  else:
    etiquette.config(text="Veuillez remplir tous les champs.")

fenetre = tk.Tk()
fenetre.title("Ma premiere interface graphique")

etiquette_pseudo = tk.Label(fenetre, text="Rentrez votre pseudo :")
etiquette_pseudo.pack()
champ_texte_pseudo = tk.Entry(fenetre)
champ_texte_pseudo.pack()

etiquette_email = tk.Label(fenetre, text="Rentrez votre email :")
etiquette_email.pack()
champ_texte_email = tk.Entry(fenetre)
champ_texte_email.pack()

etiquette_mdp = tk.Label(fenetre, text="Rentrez votre mot de passe (1 minuscule, 1 majuscule, 1 chiffre) :")
etiquette_mdp.pack()
champ_texte_mdp = tk.Entry(fenetre, show="*")
champ_texte_mdp.pack()

bouton = tk.Button(fenetre, text="Valider votre inscription", command=action_bouton)
bouton.pack()

etiquette = tk.Label(fenetre, text="")
etiquette.pack()

fenetre.geometry("400x300")

fenetre.mainloop()