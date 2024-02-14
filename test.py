import math
import time

# utf-coding 

#chapitre 4 5 : LISTES ET BOUCLES****************************************************************************************

 # liste = ["lundi","mardi","mercredi","jeudi",'vendredi','samedi',]
# for animal in liste :
#     print(animal)
#
# i = 0
# while i<len(liste) :
#     print(liste[i])
#     i = i+1
#
#

# for i in range(1,11) :
#     print(i, end = "")

# impairs = list(range(1,22,2))
#
# pair = []
# for i in range(len(impairs)) :
#     pair.append(impairs[i]+1)
#
# print(pair)

# notes = [14, 9, 6, 8, 12]
# moy = 0
# for note in notes :
#     moy = moy + note/len(notes)
#
# print(moy)
# s = "*"
# for i in list(range(1,20,2)) :
#     print("{:^20}".format(s*i))
# import random
#
# ligne = "ligne"
# colonne = "colonne"
# valeurs = "valeurs"
# print ("{:^10}      {:^10}      {:^10}".format(ligne, colonne, valeurs))
# count = 0
# for i in range(1,11) :
#     for j in range(i+1,11) :
#         print("{:^10}       {:^10}      {:^10}".format(i,j,random.randint(0,100)))
#         count = count + 1
#
# print(count)

#suite de Fibonacci

# fibo = [0,1]
# for i in range(20):
#     fibo.append(fibo[-1]+fibo[-2])
#     print(fibo[-1]/fibo[-2])
#
# print(fibo)

# nombres = [4, 5, 6]
# for nb in nombres:
# if nb == 5:
# print("Le test est vrai")
# print("car la variable nb vaut {}".format(nb)


#CAPITRE 6 : TESTS************************************************************************************************************

#exercices sur les tests

#exercice 1

# semaine  = ['lundi','mardi','mercredi','jeudi','vendredo','samedi','dimanche']
# for jour in semaine :
#     if jour in semaine[0:4] :
#         print("{:<10} : Au travail !".format(jour))
#     elif jour == semaine[4] :
#         print("{:<10} : Youpi c'est vendredi !".format(jour))
#     else :
#         print("{:<10} : C'est le weekend je suis dans les bruits !".format(jour))

#exercice 2

# seq = ["A","C","G","T","T","A","G","C","T","A","A","C","G"]
#
# nseq = []
#
# for unit in seq :
#     if unit == "A" :
#         nseq.append("T")
#     elif unit == "T" :
#         nseq.append("A")
#     elif unit == "C" :
#         nseq.append("G")
#     elif unit == "G" :
#         nseq.append("C")
#
# print(seq)
# print(nseq)

#exercice3

# liste = [8, 4, 6, 1, 5]
#
# min = liste[0]
# for element in liste :
#     if element <= min :
#         min = element
# print(liste)
# print("le minimum de ma liste est {:>4}".format(min))

#exercice 4

# seq = ["A","R","A","W","W","A","W","A","R","W","W","R","A","G","A","R"]
# fa = 0
# fr = 0
# fg = 0
# fw = 0
#
# for element in seq :
#     if element == "A" :
#         fa = fa + 1/len(seq)
#     if element == "R" :
#         fr = fr + 1/len(seq)
#     if element == "G" :
#         fg = fg + 1/len(seq)
#     if element == "W" :
#         fw = fw + 1/len(seq)
#
# print("Les fréquences de A R G W sont respectivement {} {} {} {} ".format(fa,fr,fg,fw))


#exercice 5
# liste = [14,9,13,15,12]
# min = liste[0]
# for element in liste :
#     if element <= min :
#         min = element
# print(liste)
# print("le minimum de ma liste est {:>4}".format(min))

# max = liste[0]
# moy = 0
# for element in liste :
#     moy = moy + element/len(liste)
#     if element >= max :
#         max = element
# print(liste)
# print("le minimum de ma liste est {:>4}".format(max))
# print("mention : ", end = '')
# if moy < 10 :
#     print("cet etudiant est mediocre")
# elif moy >= 10 and moy < 12 :
#     print("passable")
# elif moy >=10 and moy <14 :
#     print("assez bien")
# elif moy >14 :
#     print("Wow sacré etudiant c'es très bien ça")


#ecercice 6

#nombres pairs

# for i in range(20) :
#     if i%2 == 0 and i<11 :
#         print(i)
#     elif i%2 != 0 and i>10 :
#         print(i)
#
#

#Exercice 7

# for i in range(100,1000) :
#     chaine = list(str(i))
#     if(i<200 and (chaine[0] == chaine[1] or chaine[0] == chaine[2] or chaine[1] == chaine[2]) and int(chaine[0])+ int(chaine[1])+ int(chaine[2]) == 5 and i%2 == 0) :
#         print(i)
#
# print("program end")
#


#Exercice8


#Exercice 9

# liste = [[48.6,53.4],[-124.9,156.7],[-66.2,-30.8],[-58.8,-43.1],
# [-73.9,-40.6],[-53.7,-37.5],[-80.6,-16.0],[-68.5,135.0],
# [-64.9,-23.5],[-66.9,-45.5],[-69.6,-41.0],[-62.7,-37.5],
# [-68.2,-38.3],[-61.2,-49.1],[-59.7,-41.1],[-63.2,-48.5],
# [-65.5,-38.5],[-64.1,-40.7],[-63.6,-40.8],[-66.4,-44.5],
# [-56.0,-52.5],[-55.4,-44.6],[-58.6,-44.0],[-77.5,-39.1],
# [-91.7,-11.9],[48.6,53.4]]
#
# p = 0
# for element in liste :
#     if element[0]<=-27 and element[0]>=-87 and element[1]<=-17 and element[1]>= -77 :
#         print(element)
#         p = p+1
#
# print("il ya {} elements dans la liste et {} elements qui correspondent".format(len(liste),p))

#Exercice 10

#methode 1

# for i in range(100) :
#     c = 0
#     for j in range(1,i+1) :
#         if i%j == 0 :
#             c = c + 1
#     if c == 2 :
#         print("{:<5} est un nombre premier".format(i))
#
# #methode 2
#
# premiers = [2]
# for i in range(3,100) :
#     L = []
#     for j in premiers :
#         L.append(i%j)
#     if 0 not in L :
#         premiers.append(i)
#
# print(premiers)

#exercice 11
#
# Recherche dichotomique

#recherche dichotomique

# moi = int(input("entrer un nombre svp !"))
#
# val = [1,100]
# while val[0] != val[1] :
#     print("votre nombre est il plus grand que {} [+/-/=]".format((val[0] + val[1])//2))
#     rep = input("entrer votre reponse")
#     if rep == "+" :
#         val[0] = (val[0] + val[1])//2
#     elif rep == "-" :
#         val[1] = (val[0] + val[1])//2
#     elif rep == "=" :
#         val[0] = (val[0] + val[1])// 2
#         val[1] = val[0]
# print("votre nombre est {}".format(val[0]))


#chapitre 7 :  LES FICHIERS ******************************************************************************************************

#exercice 2

# animaux2 = ['poisson', 'abeille', 'chat']
# filout = open('zoo2.txt', 'w+')
# for animal in animaux2:
#     filout.write(animal+"\n")
# print(filout)


#exercice 4

# import math
# rayon = 4
# theta = 0
#
# with open("spirale.dat","w+") as fichier :
#     while theta != 2*math.pi :
#         fichier.write("{:<10.5f} {:<10.5f} \n ".format(rayon*math.sin(theta), rayon*math.cos(theta)))
#         theta = theta + 0.1*math.pi
#
# #rayon changeant
#
# import math
#
# rayon = 0
# theta = 0
#
# with open("spirale.dat", "w+") as fichier:
#     while theta != 2 * math.pi or rayon != 10:
#         fichier.write("{:<10.5f} {:<10.5f} \n ".format(rayon * math.sin(theta), rayon * math.cos(theta)))
#         theta = theta + 0.1 * math.pi
#         rayon = rayon + 0.5
#


#chapitre 8 :  MODULES

#exercice 1

#afficher les premiers nombres avec leurs racines

# import math
#
# for  i in range(10,20) :
#     print("La racine de {:<2} est : {:0<10.10f}".format(i,math.sqrt(i)))
# print("les modules c'est trop bien !!!!")

#exercice 2

# calcul de cosinus
# import math
# print("le cosinus de pi/2 est {:2f}".format(math.cos(math.pi/2)))

#exercice 3

# liste des fichiers dans un repertoire

# import os
# ch = os.listdir("/home/billjunior/PycharmProjects/exospython")
# print(ch)

#exercice 4

#affichage temporisé
# import time
# for i in range(10) :
#     print(i)
#     time.sleep(1)

#exercice 5

#sequence aleatoire de chiffres

# import random
#
# print(random.randint(0,4))

# exercice 6
#
# sequences aleatoires de base
#
# determination du nombre pi

# import random
# import math
# n = 0
# for i in range(100000000) :
#     x = random.uniform(0,1)
#     y = random.uniform(0,1)
#     r = x*x+y*y
#     r =math.sqrt(r)
#     if r<= 1 :
#         n = n + 1
#
# print("la valeur de pi est de : {}".format(4*n/100000000))
# print("la vraie valeur de pi est de {}".format(math.pi))



#chapitre 9 : FONCTIONS

#exercice 1


#exercice 2

#fonction puissance

# def puissance(x,y):
#     z = 1
#     for i in range(y) :
#         z = x*z
#     return z
#
# nombre1 = float(input("enter un nombre !!!  "))
# nombre2 = int(input("enter la puissance !!!  "))
# print("la puissance de {} ^ {} est {}".format(nombre1,nombre2,puissance(nombre1,nombre2)))

#exercice 3

#fonction pyramide

# def pyramide_gen(p) :
#     s = "*"
#     for i in range(2*p) :
#         if i%2 == 0 :
#             print("{:^100}".format(s*i))
#
# p = int(input("entrer un nombre !!! "))
# pyramide_gen(p)

#exercice 4

#nombre premier

# def is_prime(n) :
#     for i in range(2,n) :
#         if n%i == 0 :
#             return False
#     return True
#
# for i in range(2,100) :
#     if is_prime(i) :
#         print("[ {:<2} ] est un nombre premeir".format(i))
#     else :
#         print("[ {:<2} ] n'est pas un nombre premeir".format(i))

#exercice 5

#fonctionnement complet

# def complement(t) :
#     c = []
#     for i in range(len(t)) :
#         c.append(t[len(t) - i - 1])
#     return c
#
# seq = ['A', 'T', 'C', 'G', 'A','T', 'C', 'G', 'A', 'T', 'C', 'G', 'C', 'T', 'G', 'C', 'T', 'A', 'G', 'C']
# print(seq)
# print(complement(seq))

#exercice 6

#distance entre deux points

# import math
# def cal_distance3D(a,b) :
#     d = 0
#     for i in range(3) :
#         d = d + (a[i] - b[i])*(a[i] - b[i])
#     return math.sqrt(d)
#
# a = [0,0,0]
# b = [1,1,1]
#
# print("la distance entre nos deux poits est : {}".format(cal_distance3D(a,b)))
# print("la racine de 3 est de : ",math.sqrt(3))

#exercice 7

#fonction distribution et stat

# import random
# import math
#
# def moyenne(t) :
#     m = 0
#     for i in range(len(t)) :
#         m = t[i]/len(t) + m
#     return m
#
# def gen_distrib(n) :
#     liste = []
#     for i in range(n) :
#         liste.append(random.randint(1,100))
#     return liste
#
# def calc_stat(liste) :
#     ls = []
#     ls.append(min(liste))
#     ls.append(max(liste))
#     ls.append(liste[len(liste)//2])
#     ls.append(moyenne(liste))
#     return  ls
#
# for i in range(20) :
#     ls = calc_stat(gen_distrib(100))
#     print("Liste {:<5} minimum : {:<5} maximum : {:<5} mediane : {:<5} moyenne {:<5} ".format(i,ls[0],ls[1],ls[2],ls[3]))


#exercice 8

# Fonction distance à l'origine

# import math
#
# def cal_distance2D(b,a = [0,0]) :
#     d = 0
#     for i in range(2) :
#         d = d + (a[i] - b[i])*(a[i] - b[i])
#     return math.sqrt(d)
#
# def calc_dist2ori(listex,listey) :
#     liste = []
#     for i in range(len(listex)) :
#         liste.append(cal_distance2D([listex[i],listey[i]]))
#     return liste
#
# x = - math.pi
# lsx = []
# lsy = []
#
# while x <= math.pi :
#     lsx.append(x)
#     lsy.append(math.sin(x))xer
#     x = x + 0.1
#
# L = calc_dist2ori(lsx,lsy)
#
# with open("sin2ori.dat","w+") as fic :
#     for i in range(len(L)) :
#         fic.write("{:<8.3f} {:>8.3f} \n".format(lsx[i],L[i]))


#exrecice 9

#calcul d'aire methode des triangles

# import math
#
# def calc_aire(lsx,lsy) :
#     a = []
#     for i in range(len(lsx)) :
#         a.append(abs(lsx[i])*abs(lsy[i]))
#     return a
#
# x = - math.pi
#
# lsx = []
# lsy = []
#
# while x <= math.pi :
#     lsx.append(x)
#     lsy.append(math.sin(x))
#     x = x + 0.1
#
# liste = calc_aire(lsx,lsy)
#
# print("l'aire de la fonction sinus dans -pi , pi est de : {}".format(sum(liste)))



#chapitre 10 : PLUS SUR LES CHAINES DE CARACTÈRE

#exercice 1

#Parcours d'une liste

# animaux = ['girafe', 'tigre', 'singe', 'souris']
#
# for animal in animaux :
#     print("l' animal {:<6s} a {}  caractères ".format(animal,len(animal)))


#exercice 2

#Fréquence des bases dans une séquence nucléique

# def calc_composition(chaine) :
#     return chaine.count("A")/len(chaine),chaine.count("C")/len(chaine),chaine.count("G")/len(chaine),chaine.count("T")/len(chaine)
#
# chaine = "ATATACGGATCGGCTGTTGCCTGCGTAGTAGCGT"
#
# print(calc_composition(chaine))
#ceci va donner des tuples


#exercice 3

#Conversion codes à 3 lettres au code à une lettre

# liste = ["Ala","Arg","Asn","Asp","Cys","Glu","Gln","Gly","His","Ile","Leu","Lys","Met","Phe","Pro","Ser","Thr","Trp","Tyr","Val"]
#
# listeprime = ["A","R","N","D","C","E","Q","G","H","I","L","K","M","F","P","S","T","W","Y","V"]
#
# chaine = "ALA GLY GLU ARG TRP TYR SER GLY ALA TRP"
#
# for i in range(len(liste)) :
#     liste[i] = liste[i].upper()
#
# print(liste)
# print(len(liste) == len(listeprime))
# print(chaine)
# for j in range(len(liste)) :
#     if chaine.find(liste[j]) != -1 :
#         chaine = chaine.replace(liste[j],listeprime[j])
#         print(chaine)
# print(chaine)


#exercice 4

#distance de hamming

# def calc_distancedehamming(liste1,liste2) :
#     c = 0
#     for i in range(len(liste1)) :
#         if liste2[i] != liste1[i] :
#              c = c + 1
#     return  c
#
# chaine1 = "AGWPSGGASAGLAIL"
# chaine2 = "IGWPSAGASAGLWIL"
# chaine3 = "ATTCATACGTTACGATT"
# chaine4 = "ATACTTACGTAACCATT"
#
# print(calc_distancedehamming(chaine4,chaine3))
# print(calc_distancedehamming(chaine1,chaine2))

#exercice 5

#palindrome

# def is_palindrome(chaine) :
#     return chaine == "".join(reversed(chaine.split()))
#
# print(is_palindrome("paap"))

#exercice 7

#pangramme

# def get_alphabet() :
#     chaine = ""
#     for i in range(97,123) :
#         chaine = chaine + chr(i)
#     return chaine
#
# print(get_alphabet())
#
# def pangramme(chaine) :
#     for i in get_alphabet() :
#         if chaine.count(i) > 0 :
#             return False
#     return True
#
# print(pangramme("dgjklazazopiuezytyqmslkdjhgfwxxxxxxxxxxncb"))

#exercice 8

#exercice 9

#exercice 10



#chapitre 11 PLUS SUR LES LISTES

#exercice 1

#tri d'une liste

# def croiss(liste) :
#     list = []
#     r = liste[:]
#     for i in range(len(liste)) :
#         list.append(min(r))
#         r.remove(list[-1])
#     return list
# maliste = [8, 3, 12.5, 45, 25.5, 52, 1]
# print("la liste {} trié correspond à {}".format(maliste,croiss(maliste)))

#exercice 2

#Séquence nucléique aléatoire

# import random
# def gen_seq_alea(n) :
#     liste = ["A","C","G","T","U"]
#     l = []
#     for i in range(n) :
#         l.append(random.choice(liste))
#     return l
#
# print(gen_seq_alea(20))


#chapitre 13 : DICTIONNAIRE ET TUPLE

#exercice 1

#composition des acides aminés

# seq = "AGWPSGGASAGLAILWGASAIMPGALW"
#
# dictionnaire  = {}
# for acide in seq:
#     dictionnaire[acide] = seq.count(acide)
# print(dictionnaire)


#exercice 2

#Mots de deux lettres

# seq = "ACCTAGCCATGTAGAATCGCCTAGGCTTTAGCTAGCTCTAGCTAGCTG"
# dictionnaire  = {}
#
# for i in range(len(seq)//2) :
#     acide = seq[i:i+2]
#     dictionnaire[acide] = seq.count(acide)
#
# print(dictionnaire)


#exercice 3

#Mots de trois à quatre lettre

# seq = "ACCTAGCCATGTAGAATCGCCTAGGCTTTAGCTAGCTCTAGCTAGCTG"
# dictionnaire  = {}
#
# for i in range(len(seq)//3) :
#     acide = seq[i:i+3]
#     dictionnaire[acide] = seq.count(acide)
#
# print(dictionnaire)

# seq = "ACCTAGCCATGTAGAATCGCCTAGGCTTTAGCTAGCTCTAGCTAGCTG"
# dictionnaire  = {}
#
# for i in range(len(seq)//4) :
#     acide = seq[i:i+4]
#     dictionnaire[acide] = seq.count(acide)
#
# print(dictionnaire)



#exercice 4

#Mots de 2 lettres de Saccharomyces cerevisiae


#############################################modules d'interets ###########################################"""""""""""

#Mathplotlib

# import math
# import matplotlib.pyplot as plt
#
# temps = [1, 2, 3, 4, 6, 7, 9]
# o = math.pi
# concentration = [5.5, 7.2, 11.8, 13.6, 19.1, 21.7, 29.4]
#
# plt.scatter(temps, concentration, marker='o', color = 'blue')
#
# plt.xlabel("Temps (h)")
# plt.ylabel("Concentration (mg/L)")
# plt.title("Concentration de produit en fonction du temps")
# plt.show()

#------------------------module à importer------------------------------------------------------#
import numpy as np

#---------------------------Lecture du fichier PDB-----------------------------------------------#

n = 0

with open("1bta.pdb","r") as fichier1, open("1bta_CA.txt","w") as fichier2 :
    for ligne in fichier1 :
        champ = ligne.split()
        if champ[0] == "ATOM" and champ[2] == "CA" :
            fichier2.write("{} {} {}\n".format(champ[7],champ[8],champ[9]))
            n = n + 1

print("Le nombre de coordonnées est de {} ".format(n))

#--------------------------Lecture du ficher coordonnees et creation de liste--------------------#

maliste = []

with open("1bta_CA.txt","r") as fichier2 :
    for ligne in fichier2 :
        champ = ligne.split()
        maliste.append(champ)

print(maliste)

#-----------------------------construction d'un array---------------------------------------------#

mliste = np.array(maliste)
mliste = mliste.reshape(2)
print(mliste.size())


#---------------grosse incompréhesion-----------------------#



#