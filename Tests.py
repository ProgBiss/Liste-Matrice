#!/usr/bin/env python

# =============================================================================
# Titre : Tests.py
# Description : Jeux de tests.
# Auteur : Nicolas Bisson
# Date : 2015/05/14
# Version : 1.0
# Usage : python3 Tests.py
# Notes :
# python_version : 3.4.0
# =============================================================================


from Principal import fusion, transformationMatrice, transformationListe,\
    gererEntrees, partitionnement, transposition, choixPivot, triFusion


def gererEntrees(liste, choixValide):
    """ Gère les entrées des choix dans les menus et 
        celles des listes et des matrices.
    """
    
    if isinstance(choixValide, str):
        valide = True
        for element in liste:
            if not(element in choixValide):
                valide = False
    else:
        raise ValueError
    
    return valide


def menuTests():
    """ Menu qui pour lancer les tests.
    """
    
    gestion1 = True
    while gestion1:
        print("Veuillez sélectionner un des modes suivants: \n")
        print("1 - Lancer les tests")
        print("0 - Quitter \n")
        
        choix = input("Choix: ")
        
        if not(gererEntrees(choix, "012")):
            print("Choix invalide. Veuillez entrer 0 ou 1.")
        else:
            if choix == "1":
                tests()
            elif choix == "0":
                gestion1 = False


def tests():
    """ Lance tous les tests.
    """
        
    testFusion()
    testTriFusion()
    testChoixPivot()
    testPartitionnement()
    testTransformationListe()
    testTransformationMatrice()
    testTransposition()
    testGererEntrees()


def testTransformationListe():
    """ Jeux de tests pour la fonction "transformationListe".
    """
    
    isPassed = True
    try:
        transformationListe("Allo")
        isPassed = False
        print("Échec du test transformationListe: Type non valide. \n")
    except:
        pass
    retour = transformationListe("")
    if retour != []:
        isPassed = False
        print("Échec du test transformationListe: Liste en string vide (limite). \n")
    retour = transformationListe("1 2 3")
    if retour != [1, 2, 3]:
        isPassed = False
        print("Échec du test transformationListe: Liste en string (normale). \n")
    if isPassed:
        print("Test transformationListe s'est correctement effectué. \n")


def testTransformationMatrice():
    """ Jeux de tests pour la fonction "transformationMatrice".
    """
    
    isPassed = True
    try:
        transformationMatrice("Allo")
        isPassed = False
        print("Échec du test transformationMatrice: Type non valide. \n")
    except:
        pass
    retour = transformationMatrice([[]])
    if retour != [[]]:
        isPassed = False
        print("Échec du test transformationMatrice: Matrice vide (limite). \n")
    retour = transformationMatrice([["1", "2", "3"], ["1", "2", "3"]])
    if retour != [[1, 2, 3], [1, 2, 3]]:
        isPassed = False
        print("Échec du test transformationMatrice: Matrice en string (normale). \n")
    if isPassed:
        print("Test transformationMatrice s'est correctement effectué. \n")


def testFusion():
    """ Jeux de tests pour la fonction "fusion".
    """
    
    isPassed = True
    try:
        fusion("Allo", "Coucou")
        isPassed = False
        print("Échec du test fusion: Type non valide. \n")
    except:
        pass
    try:
        fusion([[1, 2, 3], [1, 2, 3]], [[1, 2, 3], [1, 2, 3]])
        isPassed = False
        print("Échec du test fusion: Valeur non valide. \n")
    except:
        pass
    retour = fusion([], [])
    if retour != []:
        isPassed = False
        print("Échec du test fusion: Liste vide (limite). \n")
    retour = fusion([2], [1, 3])
    if retour != [1, 2, 3]:
        isPassed = False
        print("Échec du test fusion: Liste mélangée (normale). \n")
    if isPassed:
        print("Test fusion s'est correctement effectué. \n")


def testTriFusion():
    """ Jeux de tests pour la fonction "triFusion".
    """
    
    isPassed = True
    try:
        triFusion("Allo")
        isPassed = False
        print("Échec du test triFusion: Type non valide. \n")
    except:
        pass
    try:
        triFusion([[1, 2, 3], [1, 2, 3]])
        isPassed = False
        print("Échec du test triFusion: Valeur non valide. \n")
    except:
        pass
    retour = triFusion([])
    if retour != []:
        isPassed = False
        print("Échec du test triFusion: Liste vide (limite). \n")
    retour = triFusion([4, 1, 3, 2])
    if retour != [1, 2, 3, 4]:
        isPassed = False
        print("Échec du test triFusion: Liste mélangée (normale). \n")
    if isPassed:
        print("Test triFusion s'est correctement effectué. \n")


def testChoixPivot():
    """ Jeux de tests pour la fonction "choixPivot".
    """
    
    isPassed = True
    try:
        choixPivot("Allo", "Coucou", "Bonjour")
        isPassed = False
        print("Échec du test choixPivot: Type non valide. \n")
    except:
        pass
    try:
        choixPivot([5, 3, 2, 4], [1, 2, 3, 4], [5, 3, 2, 4])
        isPassed = False
        print("Échec du test choixPivot: Valeur non valide. \n")
    except:
        pass
    premier = 0
    retour = choixPivot([5, 3, 2, 4], premier, 3)
    if retour != premier:
        isPassed = False
        print("Échec du test choixPivot: Liste mélangée (normale). \n")
    if isPassed:
        print("Test choixPivot s'est correctement effectué. \n")


def testPartitionnement():
    """ Jeux de tests pour la fonction "partitionnement".
    """
    
    isPassed = True
    try:
        partitionnement("Allo", "Coucou", "Bonjour", "Beh")
        isPassed = False
        print("Échec du test partitionnement: Type non valide. \n")
    except:
        pass
    try:
        partitionnement([5, 3, 2, 4], [1, 2, 3, 4], [5, 3, 2, 4], [1, 2, 3, 4])
        isPassed = False
        print("Échec du test partitionnement: Valeur non valide. \n")
    except:
        pass
    premier = 0
    pivot = premier
    retour = partitionnement([5, 3, 2, 4], premier, 3, pivot)
    if retour != 0:
        isPassed = False
        print("Échec du test partitionnement: 0 (normale). \n")
    if isPassed:
        print("Test partitionnement s'est correctement effectué. \n")


def testTransposition():
    """ Jeux de tests pour la fonction "transposition".
    """
    
    isPassed = True
    try:
        transposition("Coucou")
        isPassed = False
        print("Échec du test transposition: Type non valide. \n")
    except:
        pass
    try:
        transposition([1, 2, 3, 4])
        isPassed = False
        print("Échec du test transposition: Valeur non valide. \n")
    except:
        pass
    retour = transposition([])
    if retour != []:
        isPassed = False
        print("Échec du test transposition: Matrice vide (limite). \n")
    retour = transposition([[1, 2, 3], [1, 2, 3]])
    if retour != [[1, 1], [2, 2], [3, 3]]:
        isPassed = False
        print("Échec du test transposition: Matrice (normale). \n")
    if isPassed:
        print("Test transposition s'est correctement effectué. \n")


def testGererEntrees():
    """ Jeux de tests pour la fonction "gererEntrees".
    """
    
    isPassed = True
    try:
        gererEntrees("Bonjour", 123)
        isPassed = False
        print("Échec du test gererEntrees: Type non valide. \n")
    except:
        pass
    retour = gererEntrees("Allo", "Coucou")
    if retour != False:
        isPassed = False
        print("Échec du test gererEntrees: Valeur introuvable (limite). \n")
    retour = gererEntrees("3", "12345")
    if retour != True :
        isPassed = False
        print("Échec du test gererEntrees: Choix et liste correct (normale). \n")
    if isPassed:
        print("Test gererEntrees s'est correctement effectué. \n")

menuTests()