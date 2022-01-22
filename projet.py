# Initialisation
# Choix du mot
import random
mot_a_trouver = random.choice(open('liste_francais.txt').readlines())
mot_a_trouver = mot_a_trouver[:len(mot_a_trouver)-1]

print(mot_a_trouver)

mot_a_afficher = '_'*(len(mot_a_trouver))
gagne = False
nb_erreur = 0
from os import system
proposition = str()

# Début de la partie
while nb_erreur < 8 and gagne == False and proposition != mot_a_trouver and mot_a_afficher != mot_a_trouver:

 system('cls')
 print(mot_a_trouver)
 print('Nombre d\'echecs : ' , nb_erreur)
 # Début
 print(mot_a_afficher)

 proposition = input('Proposition : ')

# Début des tests
 verif = 0
 if len(proposition) > 1:
  if proposition == mot_a_trouver:
   gagne = True
   print('GG')
  else:
   nb_erreur = nb_erreur + 1
 else:
  for i in range (len(mot_a_trouver)):
   if proposition == mot_a_trouver[i]:
    mot_a_afficher = mot_a_afficher[:i]+proposition+mot_a_afficher[i+1:]
    # Preuve de bonne lettre
    verif = 1
  if verif == 0:
   print('Echec hehe')
   nb_erreur = nb_erreur+1

# Fin du jeu (choix des différents message de fin)
if nb_erreur == 8:
 system('cls')
 print('Perdu')
 system('pause')

if mot_a_trouver == mot_a_afficher or proposition == mot_a_trouver or gagne == True:
 print('Bien vu')