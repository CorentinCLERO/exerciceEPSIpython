
chiffre = input("Entrez un chiffre : ")
chiffre2 = input("Entrez un autre chiffre : ")
opération = input("Entrez une opération : + - % ou x ")

if opération == 'x':
    result = int(chiffre) * int(chiffre2)
elif opération == '+':
    result = int(chiffre) + int(chiffre2)
elif opération == '-':
    result = int(chiffre) - int(chiffre2)
elif opération == '%':
    result = int(chiffre) / int(chiffre2)
elif opération == '/':
    result = int(chiffre) / int(chiffre2)
else:
    print("Opération non valide.")
    result = None

print("le résultat est :" )
print( result )