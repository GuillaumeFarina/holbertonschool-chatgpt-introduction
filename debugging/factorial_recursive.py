#!/usr/bin/python3  # Indique à l'interpréteur du système d'exécuter ce script avec Python 3

import sys  # Importe le module sys, qui permet d'accéder aux arguments de la ligne de commande

def factorial(n):
    # Définition d'une fonction récursive pour calculer le factoriel de n
    if n == 0:
        return 1  # Cas de base : 0! = 1
    else:
        return n * factorial(n-1)  # Appel récursif : n! = n * (n-1)!

# Récupère le premier argument de la ligne de commande, le convertit en entier,
# et appelle la fonction factorial avec cet entier
f = factorial(int(sys.argv[1]))

# Affiche le résultat du calcul du factoriel
print(f)