#!/usr/bin/env python

# =============================================================================
# Titre : Principal.py
# Description : Programme qui permet de gérer des listes et des matrices.
# Auteur : Nicolas Bisson
# Date : 2015/05/14
# Version : 1.0
# Usage : python3 Principal.py
# Notes :
# python_version : 3.4.0
# =============================================================================


import os


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
          
            
def menuAccueil():
    """ Affiche les choix du menu principal et retourne un choix.
    """
    
    gestion1 = True
    while gestion1:
        print("Veuillez sélectionner un des modes suivants: \n")
        print("1 - Gestion de listes")
        print("2 - Gestion de matrices")
        print("0 - Quitter \n")
        
        choix = input("Choix: ")
        
        if not(gererEntrees(choix, "012")):
            print("Choix invalide. Veuillez entrer 0, 1 ou 2.")
        else:
            if choix == "1":
                menuEntreeListes()
            elif choix == "2":
                menuEntreeMatrices()
            elif choix == "0":
                gestion1 = False


def listesAccueil(liste):
    """ Affiche le menu de gestion de listes. Gère le choix pour lancer
        la fonction pour effectuer ce qui est demander.
    """
    
    gestion2 = True
    while gestion2:
        menuListe()
        
        choix = input("Choix: ")
        
        if not(gererEntrees(choix, "01234567")):
            print("Choix invalide. Veuillez entrer un choix valide.")
        else:
            if choix == "1":
                afficher(liste, 1)
            elif choix == "2":
                menuTri(liste, 1)
            elif choix == "3":
                maximum(liste, 1)
            elif choix == "4":
                minimum(liste, 1)
            elif choix == "5":                    
                somme(liste, 1)
            elif choix == "6":                    
                inversion(liste)
            elif choix == "7":
                gestion2 = False
                menuEntreeListes()
            elif choix == "0":
                gestion2 = False
    

def matricesAccueil(matrice):
    """ Gère le choix pour lancer la fonction qui effectue
        ce qui est demander.
    """
    gestion3 = True
    while gestion3:
        menuMatrice()
        
        choix = input("Choix: ")
        
        if not(gererEntrees(choix, "0123456789A")):
            print("Choix invalide. Veuillez entrer un choix valide.")
        else:
            if choix == "1":
                for ligne in matrice:
                    afficher(ligne, 2)
            elif choix == "2":
                menuTri(matrice, 2)
            elif choix == "3":
                matrice = transposition(matrice)
                menuTri(matrice, 3)
                matrice = transposition(matrice)
            elif choix == "4":
                maximum(matrice, 2)
            elif choix == "5":                    
                minimum(matrice, 2)
            elif choix == "6":                    
                somme(matrice, 2)
            elif choix == "7":
                matrice = transposition(matrice)
            elif choix == "8":
                gererLigneColonne(matrice)              
            elif choix == "9":
                matrice = transposition(matrice)
                gererLigneColonne(matrice)    
                matrice = transposition(matrice)         
            elif choix == "A":
                gestion3 = False
                menuEntreeMatrices()
            elif choix == "0":
                gestion3 = False
        

def menuListe():
    """ Affiche les choix possibles pour les listes.
    """
    
    print("Que voulez-vous faire? \n")
    print("1 - Afficher la liste")
    print("2 - Trier la liste")
    print("3 - Afficher la valeur maximale")
    print("4 - Afficher la valeur minimale")
    print("5 - Afficher la somme des valeurs")
    print("6 - Inverser la liste")
    print("7 - Modifier la liste")
    print("0 - Retour \n")


def menuMatrice():
    """ Affiche les choix possibles pour les matrices.
    """
    
    print("Que voulez-vous faire? \n")
    print("1 - Afficher la matrice")
    print("2 - Trier les lignes")
    print("3 - Trier les colonnes")
    print("4 - Afficher la valeur maximale")
    print("5 - Afficher la valeur minimale")
    print("6 - Afficher la somme des valeurs")
    print("7 - Transposer la matrice")
    print("8 - Gérer une ligne")
    print("9 - Gérer une colonne")
    print("A - Modifier la matrice")
    print("0 - Retour \n")


def menuEntreeListes():
    """ Demande à l'utilisateur le moyen d'obtenir la liste. Prends cette
        liste et l'envoi pour la gèrer selon les désirs de l'utilisateur.
    """
    
    gestion4 = True
    while gestion4:
        choix = input("Voulez-vous entrer une liste via un fichier? " + \
                      "(oui/non/annuler): ")
        if choix == "oui" or choix == "OUI" or choix == "Oui":
            fichierListe = input("Entrer le nom du fichier: ")
            if os.path.exists(fichierListe):
                fichier = open(fichierListe, mode="r")
                liste = fichier.readline()
                fichier.close()
                if not(gererEntrees(liste, "0123456789 -")):
                    print("Veuillez recommencer.")
                else:
                    gestion4 = False
                    listesAccueil(transformationListe(liste))
            else:
                print("Fichier introuvable.")
        elif choix == "non" or choix == "NON" or choix == "Non":
            print("Entrer une liste séparée par des espaces.")
            liste = str(input("Liste :"))
            if not(gererEntrees(liste, "0123456789 -")):
                print("Veuillez recommencer.")
            else:
                gestion4 = False
                listesAccueil(transformationListe(liste))
        elif choix == "annuler" or choix == "ANNULER" or choix == "Annuler":
            gestion4 = False
        else:
            print("Choix invalide.")


def menuEntreeMatrices():
    """ Demande à l'utilisateur le moyen d'obtenir la matrice. Prends cette
        liste et l'envoi pour la gèrer selon les désirs de l'utilisateur.
    """
    
    gestion5 = True
    while gestion5:
        choix = input("Voulez-vous entrer une matrice via un fichier? " + \
                      "(oui/non/annuler): ")
        if choix == "oui" or choix == "OUI" or choix == "Oui":
            fichierMatrice = input("Entrer le nom du fichier: ")
            if os.path.exists(fichierMatrice):
                fichier = open(fichierMatrice, mode="r")
                matrice = []
                for ligne in fichier:
                    ligne = ligne.rstrip("\n")
                    ligne2 =  ligne.split()
                    matrice.append(ligne2)
                if not(gererEntrees(ligne, "0123456789 -\n")):
                    print("Ligne incorrect.")
                else:
                    fichier.close()
                    gestion5= False
                    matricesAccueil(transformationMatrice(matrice))
            else:
                print("Fichier introuvable.")
        elif choix == "non" or choix == "NON" or choix == "Non":
            print("Entrer une matrice séparée par des espaces.")
            execution = True
            matrice = []
            while execution:
                matriceLigne = input()
                if not(gererEntrees(matriceLigne, "0123456789 -")):
                    print("Veuillez recommencer.")
                    execution = False
                elif matriceLigne == "":
                    gestion5 = False
                    execution = False
                    matricesAccueil(transformationMatrice(matrice))
                else:
                    matrice.append(transformationListe(matriceLigne))
        elif choix == "annuler" or choix == "ANNULER" or choix == "Annuler":
            gestion5 = False
        else:
            print("Choix invalide.")


def transformationListe(liste):
    """ Transforme chaque chiffre de la string rentrer en integer.
    """
    
    listeInt = []
    listeSplit = liste.split()
    for element in listeSplit:
        elementInt = int(element)
        listeInt.append(elementInt)
        
    return listeInt


def transformationMatrice(matrice):
    """ Transforme chaque chiffre de chaque ligne en integer.
        Transforme chaque ligne en liste à l'intérieur d'une 
        liste pour créer la matrice.
    """
    
    gestion8 = True
    while gestion8:
        if matrice == []:
            gestion8 = False
            matriceInt = []
        else:
            longueur = len(matrice[0])
            for ligne in matrice:
                if len(ligne) != longueur:
                    print("Veuillez recommencer, matrice invalide. Les lignes " + \
                          "doivent avoir la même longueur.")
                    gestion8 = False
                elif len(ligne) == longueur:
                    pass
            matriceInt = []
            for ligne in matrice:
                ligneInt = []
                for element in ligne:
                    elementInt = int(element)
                    ligneInt.append(elementInt)
                matriceInt.append(ligneInt)
                gestion8 = False
        
    return matriceInt


def afficher(liste, menuPrecedent):
    """ Affiche la liste à l'écran.
    """
    
    listeAfficher = []
    for element in liste:
        listeAfficher.append(str(element))
    if  menuPrecedent == 1:
        print("Liste: ", " ".join(listeAfficher))
    elif menuPrecedent == 2:
        print(" ".join(listeAfficher))


def maximum(liste, menuPrecedent):
    """ Affiche le maximum de la liste à l'écran.
    """
    
    if len(liste) < 0:
        print("Impossible qu'une liste ait moins d'un élément.")
    elif len(liste) == 0:
        print("Liste vide.")
    else:
        if menuPrecedent == 1:
            print("Max: ", max(liste))
        elif menuPrecedent == 2:
            print("Max: ", max(max(liste)))


def minimum(liste, menuPrecedent):                      
    """ Affiche le minimum de la liste à l'écran.
    """
    
    if len(liste) < 0:
        print("Impossible qu'une liste ait moins d'un élément.")
    elif len(liste) == 0:
        print("Liste vide.")
    else:
        if menuPrecedent == 1:
            print("Min: ", min(liste))
        elif menuPrecedent == 2:
            print("Min: ", min(min(liste)))


def somme(liste, menuPrecedent):
    """ Affiche la somme de la liste à l'écran.
    """
    
    if len(liste) < 0:
        print("Impossible qu'une liste ait moins d'un élément.")
    elif len(liste) == 0:
        print("Liste vide, donc il n'y a pas de somme.")
    else:
        if menuPrecedent == 1:
            print("Somme: ", sum(liste))
        elif menuPrecedent == 2:
            total = 0
            for ligne in liste:
                totalTemp = sum(ligne)
                total += totalTemp
            print("Somme: ", total)

def inversion(liste):
    """ Inverse les éléments de la liste.
    """
    
    if len(liste) < 0:
        print("Impossible qu'une liste ait moins d'un élément.")
    elif len(liste) == 0:
        print("Liste vide, aucune inversion possible.")
    else:
        liste.reverse()


def gererLigneColonne(matrice):
    """ Envoi la ligne ou la colonne souhaitée dans le menu 
        de gestion de listes pour en faire la gestion.
    """ 
    gestion7 = True
    ligneOK = True
    ligne = None
    choixOK = False
    while gestion7:
        while ligneOK != False:
            while ligne is None:
                ligne = None
                try:
                    ligne = input("Quel est la ligne/colonne à gérer: ")
                    choixOK = True
                except:
                    ligneOK = True
            if choixOK == True:
                if not(gererEntrees(ligne, "0123456789")):
                    print("Veuillez recommencer.")
                    gestion7 = False
                elif (gererEntrees(ligne, "0123456789")):
                    ligneInt = int(ligne)
                    if matrice == []:
                        print("Veuillez réessayer. Cette matrice est vide.")
                        gestion7 = False
                        ligneOK = False
                    elif ligneInt < 0 or ligneInt > len(matrice):
                        print("Veuillez réessayer. Cette ligne n'existe pas.")
                        gestion7 = False
                        ligneOK = False
                    else:
                        matriceLigne = matrice[ligneInt - 1][:]  
                        listesAccueil(matriceLigne) 
                        liste = []
                        for element in matriceLigne:
                            liste.append(element)
                        matrice[ligneInt - 1] = liste
                        gestion7 = False
                        ligneOK = False


def triBulle(liste):
    """ Tri la liste avec la méthode de tri bulle.
        Algorithme: Louis Marchand.
    """
    
    grandeurListe = len(liste)
    echange = True
    while ((grandeurListe > 0) and (echange)):
        echange = False
        for position in range(0, grandeurListe - 1):
            if (liste[position] > liste[position + 1]):
                listeTemporaire = liste[position]
                liste[position] = liste[position + 1]
                liste[position + 1] = listeTemporaire
                echange = True
        grandeurListe -= 1
    

def triInsertion(liste):
    """ Tri la liste avec la méthode de tri par insertion.
        Algorithme: Louis Marchand.
    """
    
    grandeurListe = len(liste)
    for position in range(1, grandeurListe):
        element = liste[position]
        position2 = position
        while position2 > 0 and liste[position2 - 1] > element:
            liste[position2] = liste[position2 - 1]
            position2 -= 1
        liste[position2] = element


def fusion(liste1, liste2):
    """ Fusionne les listes pour les trier. Va avec le tri fusion.
        Algorithme: Louis Marchand
    """
    
    grandeurListe1 = len(liste1)
    grandeurListe2 = len(liste2)
    position = 0
    position2 = 0
    resultat = []
    while position < grandeurListe1 and position2 < grandeurListe2:
        if isinstance(liste1[position], int):
            if liste1[position] <= liste2[position2]:
                resultat.append(liste1[position])
                position += 1
            else:
                resultat.append(liste2[position2])
                position2 += 1
        else:
            raise ValueError
    while position < grandeurListe1:
        resultat.append(liste1[position])
        position += 1
    while position2 < grandeurListe2:
        resultat.append(liste2[position2])
        position2 += 1
        
    return resultat


def triFusion(liste):
    """ Tri la liste avec la méthode de tri par fusion.
        Algorithme: Louis Marchand.
    """
    
    if isinstance(liste, list):
        grandeurListe = len(liste)
        if grandeurListe <= 1:
            resultat = liste
        else:
            sousListe1 = liste[: int(grandeurListe / 2)]
            sousListe2 = liste[int(grandeurListe / 2) :]
            sousListeTriee1 = triFusion(sousListe1)
            sousListeTriee2 = triFusion(sousListe2)
            resultat = fusion(sousListeTriee1, sousListeTriee2)
    else:
        raise ValueError
        
    return resultat


def choixPivot(liste, entierPremier, entierDernier):
    """ Retourne le premier chiffre de la liste. Va avec le tri rapide.
        Algorithme: Louis Marchand.
    """
    
    for element in liste:
        if isinstance(element, int) and isinstance(entierPremier, int) \
        and isinstance(entierDernier, int):
            pass
        else:
            raise ValueError
        
    return entierPremier


def partitionnement(liste, entierPremier, entierDernier, entierPivot):
    """ Divise la liste pour trier une partie à la fois. Va avec le tri rapide.
        Algorithme: Louis Marchand.
    """
    
    for element in liste:
        if isinstance(element, int) and isinstance(entierPremier, int) \
        and isinstance(entierDernier, int) and isinstance(entierPivot, int):
            elementPivot = liste[entierPivot]
            liste[entierPivot] = liste[entierDernier]
            liste[entierDernier] = elementPivot
            element2 = entierPremier
            for element in range(entierPremier, entierDernier):
                if liste[element] <= elementPivot:
                    listeTemporaire2 = liste[element]
                    liste[element] = liste[element2]
                    liste[element2] = listeTemporaire2
                    element2 += 1
            liste[entierDernier] = liste[element2]
            liste[element2] = elementPivot
        else:
            raise ValueError
    
    return element2
    

def triRapide2(liste, entierPremier, entierDernier):
    """ Tri la liste avec la méthode de tri rapide.
        Algorithme : Louis Marchand.
    """
    
    if entierPremier < entierDernier:
        entierPivot = choixPivot(liste, entierPremier, entierDernier)
        entierPivot = partitionnement(liste, entierPremier, entierDernier, entierPivot)
        triRapide2(liste, entierPremier, entierPivot - 1)
        triRapide2(liste, entierPivot + 1, entierDernier)
 
 
def triRapide(liste):
    """ Lance le tri rapide.
        Algorithme: Louis Marchand.
    """
    
    grandeurListe = len(liste)
    triRapide2(liste, 0, grandeurListe - 1)
    

def triPeigne(liste):
    """ Tri la liste avec la méthode de tri à peigne.
        Algorithme: http://fr.wikipedia.org/wiki/Tri_à_peigne.
    """
    
    intervalle = len(liste) 
    echange = True
    while intervalle > 1 or echange == True:
        intervalle = int(intervalle / 1.3)
        if intervalle < 1:
            intervalle = 1
        position = 0
        echange = False
        while position < len(liste) - intervalle:
            if liste[position] > liste[position + intervalle]:
                listeTemporaire = liste[position]
                liste[position] = liste[position + intervalle]
                liste[position + intervalle] = listeTemporaire
                echange = True
            position += 1


def triShell(liste):
    """ Tri la liste avec la méthode de tri shell.
        Algorithme: en.wikipedia.org/wiki/Shellsort
    """
    
    grandeurListe = len(liste)
    gaps = [701, 301, 132, 57, 23, 10, 4, 1]
    for gap in gaps:
        element = gap
        while element < grandeurListe:
            listeTemporaire = liste[element]
            element2 = element
            while element2 >= gap and liste[element2 - gap] > listeTemporaire:
                liste[element2] = liste[element2 - gap]
                element2 -= gap
            liste[element2] = listeTemporaire
            element += 1
    
    
def changementListe(liste, nouvelleListe):
    """ Transforme la liste du début pour qu'elle devienne comme 
        la nouvelle liste qui est modifiée.
    """
    if len(liste) == len(nouvelleListe):
        for element in range(len(liste)):
            liste[element] = nouvelleListe[element]
    

def transposition(matrice):
    """Fait une transposition de matrice 
       (change les lignes pour les colonnes et vice-versa).
       Algorithme : 
       http://stackoverflow.com/questions/17037566/transpose-a-matrix-in-python
    """
    if matrice == []:
        transpose = [list(element) for element in zip(*matrice)]
    else:
        for element in matrice:
            if isinstance(matrice, list):
                transpose = [list(element) for element in zip(*matrice)]
            else:
                raise ValueError
    
    return transpose


def menuTri(liste, menuPrecedent):
    """ Affiche le menu pour choisir le typpe de tri à effectuer.
    """
    
    gestion6 = True
    while gestion6:
        print("1 - Tri bulle")
        print("2 - Tri insertion")
        print("3 - Tri fusion")
        print("4 - Tri rapide")
        print("5 - Tri peigne")
        print("6 - Tri shell")
        
        if menuPrecedent == 1:
            triListe(liste)
            gestion6 = False
        elif menuPrecedent == 2 or menuPrecedent == 3:
            triMatrices(liste)
            gestion6 = False
        
        
def triListe(liste):
    """ Effectue le tri choisi pour une liste simple.
    """
    
    gestion9 = True
    while gestion9:
        choix = input("Quel tri voulez-vous: ")
        
        if not(gererEntrees(choix, "123456")):
            print("Choix invalide. Recommencez.")
        else:
            if choix == "1":
                gestion9 = False
                triBulle(liste)
            elif choix == "2":
                gestion9 = False
                triInsertion(liste)
            elif choix == "3":
                gestion9 = False
                liste = changementListe(liste, triFusion(liste))
            elif choix == "4":
                gestion9 = False
                triRapide(liste)
            elif choix == "5":
                gestion9 = False
                triPeigne(liste)
            elif choix == "6":
                gestion9 = False
                triShell(liste)
            
            
def triMatrices(matrice):
    """ Effectue le tri choisi pour les lignes ou les colonnes d'une matrice.
    """
    
    choix = input("Quel tri voulez-vous: ")
    
    if not(gererEntrees(choix, "123456")):
        print("Choix invalide. Recommencez.")
    else:
        if choix == "1":
            for ligne in matrice:
                triBulle(ligne)
        elif choix == "2":
            for ligne in matrice:
                triInsertion(ligne)
        elif choix == "3":
            for ligne in matrice:
                matrice = changementListe(ligne, triFusion(ligne))
        elif choix == "4":
            for ligne in matrice:
                triRapide(ligne)
        elif choix == "5":
            for ligne in matrice:
                triPeigne(ligne)
        elif choix == "6":
            for ligne in matrice:
                triShell(ligne)