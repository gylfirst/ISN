#éléments avec # : soit du debug, soit des commentaires.

# tas = 50 #on met 50 cartes dans le talon.
slots_carte = 10 #on a dix slots pour distribuer les cartes
cartes = [1,2,3,4,5,6,7,8,9,10,11,12,13]*8 #liste contenant les cartes de 2 paquets de 52 cartes, à une couleur.
gen_cartes_list = []
final = []
list = [[],[],[],[],[],[],[],[],[],[]]
tas = []
nb_mouv = 0
Win_condi = False

import random as rd

def generate_cartes (): #fonction qui génére aléatoirement les paquets de cartes
    global gen_cartes_list
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
    global list, gen_cartes_list
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

def distribution ():
    global tas, list
    nombres_cartes()
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

def affiche_colone (liste):
    global list
    ligne = " {:>2}  {:>2}  {:>2}  {:>2}  {:>2}  {:>2}  {:>2}  {:>2}  {:>2}  {:>2} "
    x = 0
    for c in range(len(liste)):
        if x < len(liste[c]):
            x = len(liste[c])
    for k in range (x):
        affichage = []
        for j in range (10):
            if len(liste[j]) > k :
                affichage.append(str(liste[j][k]))
            else :
                affichage.append("")
        print(ligne.format(affichage[0],affichage[1],affichage[2],
                     affichage[3],affichage[4],affichage[5],
                     affichage[6],affichage[7],affichage[8],affichage[9]))

def deplacement ():
    global list
    print("On va numéroter les colonnes de 1 à 10 !")
    slot_dep = int(input("Quelle est la colonne de départ ? "))-1
    slot_fin = int(input("Quelle est la colonne d'arrivée ? "))-1
    nb_cartes = int(input("Combien de cartes souhaitez-vous deplacer ? "))
    #on veut vérifier que la carte désirée est supérieure de 1 comparée à celle d'arrivée
    x = list[slot_dep][len(list[slot_dep])-nb_cartes]
    #print(x)
    virt = False
    if list[slot_fin] == [] :
        virtx = x+1
        #print(virtx)
        list[slot_fin].append(virtx)
        virt = True
    y = list[slot_fin][len(list[slot_fin])-1]
    #print(y)
    depla = True
    if x != y-1 :
        depla = False
    else :
        for a in range (nb_cartes):
            if  list[slot_dep][len(list[slot_dep])-nb_cartes+a] != x-a :
                depla = False

    if depla :
        for i in range (nb_cartes,0,-1):
            list[slot_fin].append(list[slot_dep][len(list[slot_dep])-i])
            del(list[slot_dep][len(list[slot_dep])-i])
        if virt :
            del(list[slot_fin][0])
    else :
        print("Le déplacement de la carte est impossible !")

def distrib_tas ():
    #print(tas)
    for i in range (10):
        x = 0
        list[i].append(tas[x])
        del(tas[x])
        x += 1
    #print(tas)

def check_serie ():
    global list, final
    for i in range (len(list)):
        test = True
        for k in range (1,14) :
            if len(list[i])- k >= 0 :
                if list[i][len(list[i])-k] != k :
                    test = False
            else :
                test = False
        if test :
            #print("OK pour i = ", i)
            x = 13
            if x in list[i] :
                for j in range (13,0,-1):
                    final.append(j)
                    del(list[i][-1])
                    #print(final)
                    #print(list)
        else :
           #print("Raté pour i = ", i)
           pass

def fin ():
    global Win_condi, list, nb_mouv
    #print("win_condi: ", Win_condi)
    x = 0
    for i in range (len(list)):
        if len(list[i]) == 0 :
            #print("La colonne ", i, " est vide !")
            x += 1
        else :
            #print("La colonne ", i, " n'est pas vide !")
            x = x
    if x == 10 and tas == [] :
        print("Vous avez gagné en",nb_mouv,"mouvements !\nFélicitation !\n")
        Win_condi = True
    else :
        print("\nVous n'avez pas encore gagné ! Allez, courage !\n")
        Win_condi = False
    #print("win_condi: ", Win_condi)

def debug ():
    global tas, list
    print("         Fonction debug en execution !\n")
    affiche_colone(list)
    print("\n")
    for j in range (10):
        list[j] = []
        for i in range(13,0,-1):
            list[j].append(i)
    list[9].remove(1)
    list[0].append(1)
    tas = []
    print(tas)
    #affiche_colone(list)
    #check_serie()

##Initialisation du jeu :
print("\n-------------------------------------------------\n|   Jeu créé pour le projet ISN de Terminale    |\n|         Créé par Matthieu Tourrette           |\n-------------------------------------------------\n")
print("        Initialsation du jeu en cours...\n             Veuillez patienter...")
print("           Merci de jouer à mon jeu !\n")
#print("Choisissez une difficulté pour commencer à jouer.\n")
print("-------------------------------------------------\n|    Modèles de cartes par 'VectorStock.com'    |\n-------------------------------------------------")

def startpartie ():
    global ask_tas, tas, list
    distribution()
    ask_tas = False
    #debug()
    fonctionnement(list)

def fonctionnement (liste):
    global list, ask_tas, tas, nb_mouv
    while Win_condi is not True:
        print("\n")
        affiche_colone(liste)
        print("\n")
        deplacement()
        nb_mouv = nb_mouv + 1
        check_serie()
        fin()
        if tas != []:
            a_tas = str(input("Voulez vous distribuer le tas ? (oui ou non) "))
            if a_tas == "oui":
                ask_tas = True
            else :
                ask_tas = False

startpartie()