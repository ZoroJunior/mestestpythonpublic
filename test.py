
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