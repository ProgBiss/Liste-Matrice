# coding=UTF-8

# =============================================================================
# titre           :tris2.py
# description     :Exemples de tris (Fusion et Rapide)
# author          :Louis Marchand
# date            :20150406
# version         :1.0
# usage           :import tris2
# notes           :
# python_version  :3.4.0
# =============================================================================


def fusionner(tableau1, tableau2):
    """
        Effectue la fusion de tableau1 et tableau2 de maniÃ¨re
        Ã  retourner une liste triÃ© contenant tous les Ã©lÃ©ments
        de `tableau1' et de `tableau2'.
    """
    n = len(tableau1)
    m = len(tableau2)
    i = 0
    j = 0
    resultat = []
    while i < n and j < m:
        if tableau1[i] <= tableau2[j]:
            resultat.append(tableau1[i])
            i = i + 1
        else:
            resultat.append(tableau2[j])
            j = j + 1
    while i < n:
        resultat.append(tableau1[i])
        i = i + 1
    while j < m:
        resultat.append(tableau2[j])
        j = j + 1
    return resultat


def tri_fusion(tableau):
    """
        Effectue le tris du tableau en utilisant l'algorithme du tri fusion et
        retourne le tableau triÃ©.
    """
    n = len(tableau)
    resultat = []
    if n <= 1:
        resultat = tableau
    else:
        sous_tableau1 = tableau[: int(n / 2)]
        sous_tableau2 = tableau[int(n / 2):]
        sous_tableau_trie1 = tri_fusion(sous_tableau1)
        sous_tableau_trie2 = tri_fusion(sous_tableau2)
        resultat = fusionner(sous_tableau_trie1, sous_tableau_trie2)
    return resultat


def choix_pivot(tableau, premier, dernier):
    """
        Retourne l'index du pivot Ã  utiliser dans `tableau' considÃ©rant
        que le dÃ©but du tableau Ã  triÃ© est Ã  l'index `premier' et que
        la fin est Ã  l'index `dernier'
    """
    return premier


def partitionner(tableau, premier, dernier, pivot):
    """
        Modifier les Ã©lÃ©ments du `tableau' de maniÃ¨re Ã  ce que tous les
        Ã©lÃ©ments de valeur infÃ©rieurs ou Ã©gals de l'Ã©lÃ©ment pivot
        (`tableau[pivot]') soit avec un index infÃ©rieur Ã  celui-ci et
        les Ã©lÃ©ments de valeur supÃ©rieur aient un index supÃ©rieur. Retourne
        l'index de l'Ã©lÃ©ment pivot Ã  la fin des dÃ©placements. Les index
        infÃ©rieurs Ã  `premier' et supÃ©rieurs Ã  `dernier' sont ignorÃ©s.
    """
    element_pivot = tableau[pivot]
    tableau[pivot] = tableau[dernier]
    tableau[dernier] = element_pivot
    j = premier
    for i in range(premier, dernier):
        if tableau[i] <= element_pivot:
            temp = tableau[i]
            tableau[i] = tableau[j]
            tableau[j] = temp
            j = j + 1
    tableau[dernier] = tableau[j]
    tableau[j] = element_pivot
    return j


def tri_rapide_recursion(tableau, premier, dernier):
    """
        Effectue le tris en place du `tableau' en utilisant l'algorythme du
        tri rapide. Le tableau Ã  triÃ© ce trouve Ã  partir de l'index
        `premier' jusqu'Ã  l'index dernier.
    """
    if premier < dernier:
        pivot = choix_pivot(tableau, premier, dernier)
        pivot = partitionner(tableau, premier, dernier, pivot)
        print("Liste: " + str(tableau) + " Premier: " + str(premier) +
              " Dernier: " + str(dernier) + " Pivot: " + str(pivot))
        tri_rapide_recursion(tableau, premier, pivot - 1)
        tri_rapide_recursion(tableau, pivot + 1, dernier)


def tri_rapide(tableau):
    """
        Effectue le tris en place du `tableau' en utilisant l'algorythme du
        tri rapide.
    """
    n = len(tableau)
    tri_rapide_recursion(tableau, 0, n - 1)
