# coding=UTF-8

# =============================================================================
# titre           :tris.py
# description     :Exemples de tris (Bulle et insertion)
# author          :Louis Marchand
# date            :20150330
# version         :1.0
# usage           :import tris1
# notes           :
# python_version  :3.4.0
# =============================================================================


def tri_bulle(tableau):
    """
    Effectue le tris en place du tableau en utilisant l'algorithme du tri bulle
    """
    n = len(tableau)
    for i in range(n-1, -1, -1):
        for j in range(i):
            if tableau[j] > tableau[j + 1]:
                temp = tableau[j]
                tableau[j] = tableau[j + 1]
                tableau[j + 1] = temp


def tri_insertion(tableau):
    """
    Effectue le tris en place du tableau en utilisant l'algorithme du tri
    insertion
    """
    n = len(tableau)
    for i in range(1, n):
        element = tableau[i]
        j = i
        while j > 0 and tableau[j - 1] > element:
            tableau[j] = tableau[j - 1]
            j = j - 1
        tableau[j] = element
