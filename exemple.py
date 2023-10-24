listedefruit = [
  {"fruit" : "Pomme", "taille" : 8},
  {"fruit" : "Poire", "taille" : 18},
  {"fruit" : "Cerise", "taille" : 2},
]

nom = input("Entrez votre nom : ")
prenom = input("Entrez votre prénom : ")

print("Salutation " + prenom.capitalize() + " " + nom.upper())

taille = int(input("Entrez votre taille (en cm): "))
valeur = "0"

def jeudesfruits():
  if taille:
    print("Choisissez un fruit pour connaître votre taille en fruit :")
    for index, fruit_info in enumerate(listedefruit):
      print(f"{index}: {fruit_info['fruit']}")
    print("3: Sortir")
    valeur = input("Choix :")
    if valeur == "3": 
      print("Au revoir "+ prenom.capitalize() + " " + nom.upper())
    elif valeur in ("0", "1", "2")  :
      print(f'Votre taille en fruit est de {taille / listedefruit[int(valeur)]["taille"]:.2f} {listedefruit[int(valeur)]["fruit"].lower()}')
      jeudesfruits()
    else:
      print("Mauvais choix")
      jeudesfruits()
  else:
    print("Choissisez une taille valide la prochaine fois")

jeudesfruits()