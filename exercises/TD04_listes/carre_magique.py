import random

carre_mag = [[4,14,15,1], [9,7,6,12], [5,11,10,8], [16,2,3,13]]
carre_pas_mag = [[4,14,15,1], [9,7,6,12], [5,11,10,8], [16,2,,13]]

def carrem() :
    for ligne in carre_mag:
        for col in ligne :
            print(col, end=" ")
        print()


def cpm(): 
    carre_pas_mag = list(carre_mag)
    ind = carre_pas_mag[3].index(3)
    carre_pas_mag[3][ind] = 7
    print(carre_pas_mag)
    return carre_pas_mag
carre_pas_mag= cpm()


def afficheCarre(carre):
    """ Affiche la liste à 2 dimensions carre comme un carré"""
    for ligne in carre_mag:

        for col in ligne :
            
            print(col, end=" ")
        print()

afficheCarre(carre_mag)

print()

afficheCarre(carre_pas_mag)


def testLignesEgales(carre):
    """ Renvoie la somme des éléments d'une ligne de la liste 2D carre si toutes les lignes ont la même somme, et -1 sinon """
    A = 0
    for i in range(len(carre)):
        B = 0
        for j in range(len(carre[i])):
            B += carre[i][j]
        A += B
    if A % B == 0:
        return A // 4
    else:
        return -1

print(testLignesEgales(carre_mag))
print(testLignesEgales(carre_pas_mag))

ef testColonnesEgales(carre):
    """ Renvoie la somme des éléments d'une colonne de la liste 2D carre si toutes les colonnes ont la même somme, et -1 sinon """
    A = 0
    for i in range(len(carre)):
        B = 0
        for j in range(len(carre[i])):
            B += carre[j][i]
        A += B
    if A % B == 0:
        return A // 4
    else:
        return -1 

print(testColonnesEgales(carre_mag))
print(testColonnesEgales(carre_pas_mag))

def testDiagonalesEgales(carre):
    """ Renvoie la somme des éléments d'une diagonale de la liste 2D carre si les 2 diagonales ont la même somme, et -1 sinon """
    B = 0
    C = 0
    for i in range(0, len(carre), 1):
        B += carre[i][i]
        C += carre[i][3-i]
    if B == C :
        return B
    else :
        return -1


print(testDiagonalesEgales(carre_mag))
print(testDiagonalesEgales(carre_pas_mag))

def estCarreMagique(carre):
    """ Renvoie True si c'est un carre magique et False sinon"""
    verif_1 = testLignesEgales(carre)
    verif_2 = testColonnesEgales(carre)
    verif_3 = testDiagonalesEgales(carre)
    if verif_1 == verif_2 == verif_3 and verif_1 != -1 and verif_2 != -1 and verif_3 != -1:
        return True
    else:
        return False

print(estCarreMagique(carre_mag))
print(estCarreMagique(carre_pas_mag))

def estNormal(carre):
    """ Retourne True si contient toutes les valeurs de 1 à n^2 où n est la taille 
        du carré, et False sinon """
    n = len(carre)
    nombres = list(range(1, n * n + 1))
    for i in range(n):
        for j in range(n):
            if carre[i][j] in nombres: #on teste d'abord pour pas générer d'erreur avec remove
                nombres.remove(carre[i][j])
    return len(nombres) == 0

print(estNormal(carre_mag))
print(estNormal(carre_pas_mag))