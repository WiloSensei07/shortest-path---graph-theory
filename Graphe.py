# -*- coding: utf-8 -*-
"""
Created on Fri Mar 19 10:10:42 2021

@author: Sinka
"""

"""
TP1 Graphe

"""

import numpy as np
import pandas as pd

class  Arrete:
    """
    Classe d'arete de graphe
    """
    def __init__(self,initial,final,cout):
        self.sommetInit = initial
        self.sommetFinal= final
        self.coutArrete = cout

class Graphe:
    """
    Classe de graphe
    """
    def __init__(self,ns,arretes):
        self.nbSommet = ns
        self.listArrete = arretes

def saisie_arrete():
    """
    fonction qui permet de construire 
    une arete a partir d'informations saisies au clavier 
    """
    print("Definition d'une arrete")
    print()
    debut = int(input("entrez le sommet de départ : "))
    fin = int(input("entrez le sommet de fin : "))
    cout = int(input("entrez le cout de arrete : "))
    print()
    return Arrete(debut, fin, cout) #La fonction renvoie une arrete

def saisie_graphe():
    """
    fonction qui permet de construire
    un graphe a partir d'informations saisies au clavier 
    """
    arretes = []
    ns = int(input("entrez le nombre de sommet "))
    na = int(input("entrez le nombre d'arrete "))
    for i in range(na):
        arretes.append(saisie_arrete())
    return Graphe(ns, arretes) #La fonction renvoie un graphe

def adjacence(g):
    """
    fonction qui prend en entree un graphe
    et qui renvoie sa matrice d'adjacence (une liste à 02 dimensions)
    """
    n = g.nbSommet
    Mat = np.zeros((n,n), (int))
    #print(Mat)
    
    for arretes in g.listArrete:
        i = arretes.sommetInit
        j = arretes.sommetFinal
        Mat.itemset((i,j),1)
        Mat.itemset((j,i),1)
    return Mat
    
def afficherMatrice(matrice):
    """
    fonction qui prend en entree une matrice d'adjacence 
    et qui l'affiche sous sa forme matricielle
    """
    cols = len(matrice)*[" "]
    matrice = pd.DataFrame(matrice, columns=cols, index = cols)
    print(matrice)

graf = saisie_graphe()
print('****** Matrice adjacence **************')
afficherMatrice(adjacence(graf))

def produit(M1,M2):
    """
    fonction du produit de deux matrices
    """
    M = np.dot(M1,M2)
    for i in range(M.shape[0]):
        for j in range(M.shape[1]):
            if(M[i,j]>0):
                M[i,j]=1
            else:
                M[i,j]=0
    return M

def somme(M1,M2):
    """
    fonction de le somme de deux matrices
    """
    M = np.zeros((M1.shape[0],M1.shape[1]))
    for i in range(M.shape[0]):
        for j in range(M.shape[1]):
            M[i,j]=M1[i,j]+M2[i,j]
            if(M[i,j]>0):
                M[i,j]=1
            else:
                M[i,j]=0
    return M

def egal(M1,M2):
    """
    fonction qui compare deux matrices
    """
    for i in range(M1.shape[0]):
        for j in range(M1.shape[1]):
            if(M1[i,j]!=M2[i,j]):
                return False
    return True

def matricetransitive(g):
    """
    fonction qui définit la matrice transitive 
    """
    M0=np.identity(g.nbSommet)
    M=adjacence(g)
    MT=M0
    Mi=M
    while True:
        MT=somme(MT,Mi)
        Mi=produit(Mi,M) #Ici on passe à la seconde itération
        MT1=somme(MT,Mi)
        if(egal(MT,MT1)):
            break
    return MT

print()
print('****** Matrice transitive **************')
afficherMatrice(matricetransitive(graf))


# Algorithme de Kruskal

def trie(g):
    """
    fonction qui fait le tri d'un graphe en fonction des couts des arretes'
    """
    liste=sorted(g.listArrete,key=lambda arretes:arretes.coutArrete)
    graphe=Graphe(g.nbSommet,liste)
    return graphe

def kruskal(g):
    """
    fonction de Kruskal
    """
    cc=[0]*g.nbSommet
    for i in range(g.nbSommet):
        cc[i]=i
    graphe=trie(g)
    T=[]
    for k in range(len(g.listArrete)):
        x=graphe.listArrete[k].sommetInit
        y=graphe.listArrete[k].sommetFinal
        if(cc[x]!=cc[y]):
            T.append([x,y])
            for i in range(g.nbSommet):
                if(cc[i]==cc[x]):
                    cc[i]=cc[y]
    print(T)

print()
 # *************  methode Kruskal ***********
print('****** Liste des sommets optimaux **************')
print()
graf1 = trie(graf)
court_chemin = kruskal(graf1)
