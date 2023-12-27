#éléments avec # : soit du debug, soit des commentaires.

tas = 50 #on met 50 cartes dans le talon.
slots_carte = 10 #on a dix slots pour distribuer les cartes
cartes = [1,2,3,4,5,6,7,8,9,10,11,12,13]*4*2 #liste contenant les cartes de 2 paquets de 52 cartes, à une couleur.
gen_cartes_list = []
list = [[],[],[],[],[],[],[],[],[],[]]
tas = []

import random as rd

def generate_cartes (): #fonction qui génére aléatoirement les paquets de cartes
    x = 0
    n = 0
    while n < len(cartes) :
        x = rd.randint(1,len(cartes))
        #print(x)
        if x not in gen_cartes_list :
            gen_cartes_list.append(x)
            #print(gen_cartes_list)
            n = n+1

def nombres_cartes (): #fonction qui permet de mettre le nombre des cartes entre 1 et 13.
    generate_cartes() #on appelle la fonction pour générer notre paquet de 104 cartes.
    for i in range (len(gen_cartes_list)): #on va mettre tout les nombres de la liste entre 1 et 13.
        if gen_cartes_list[i] > 13 and gen_cartes_list[i] < 27 :
            gen_cartes_list[i] = gen_cartes_list[i] - 13
        if gen_cartes_list[i] > 26 and gen_cartes_list[i] < 40 :
            gen_cartes_list[i] = gen_cartes_list[i] - 26
        if gen_cartes_list[i] > 39 and gen_cartes_list[i] < 53 :
            gen_cartes_list[i] = gen_cartes_list[i] - 39
        if gen_cartes_list[i] > 52 and gen_cartes_list[i] < 66 :
            gen_cartes_list[i] = gen_cartes_list[i] - 52
        if gen_cartes_list[i] > 65 and gen_cartes_list[i] < 79 :
            gen_cartes_list[i] = gen_cartes_list[i] - 65
        if gen_cartes_list[i] > 78 and gen_cartes_list[i] < 92 :
            gen_cartes_list[i] = gen_cartes_list[i] - 78
        if gen_cartes_list[i] > 91 and gen_cartes_list[i] < 105 :
            gen_cartes_list[i] = gen_cartes_list[i] - 91
        #print(gen_cartes_list[i])

    i=0
    for j in range (10):
        for k in range (5):
            list[j].append(gen_cartes_list[i])
            i += 1

    for j in range (4):
        list[j].append(gen_cartes_list[i])
        i += 1

    for l in range (i, len(gen_cartes_list)):
        tas.append(gen_cartes_list[l])
    #print(tas)
    #print(list)
    #print(gen_cartes_list)




