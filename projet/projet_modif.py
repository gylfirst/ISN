#éléments avec # : soit du debug, soit des commentaires.

# tas = 50 #on met 50 cartes dans le talon.
slots_carte = 10 #on a dix slots pour distribuer les cartes
cartes = [1,2,3,4,5,6,7,8,9,10,11,12,13]*8 #liste contenant les cartes de 2 paquets de 52 cartes, à une couleur.
gen_cartes_list = []
final = []
list = [[],[],[],[],[],[],[],[],[],[]]
tas = []
tags = []
cartes_finales = "jesuislafinale"
tagtas = "jesuisletas"
tagfond = "jesuislefond"
nb_mouv = 0
CLIC = False
Win_condi = False

for h in range (1,105):
    tags.append(h)

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
    first_affichage()
    Canevas.update()
    fonctionnement(list)

def fonctionnement (liste):
    global list, ask_tas, tas, nb_mouv
    while Win_condi is not True:
        Canevas.update()
        # print("\n")
        # affichage()
        # print("\n")
        # #deplacement()
        # nb_mouv = nb_mouv + 1
        # check_serie()
        # fin()
        # if tas != []:
        #     a_tas = str(input("Voulez vous distribuer le tas ? (oui ou non) "))
        #     if a_tas == "oui":
        #         ask_tas = True
        #     else :
        #         ask_tas = False


##Interface graphique :
from tkinter import *
from PIL import Image, ImageTk
from tkinter.messagebox import *

#Fonction pour quitter le jeu :
def quitter ():
    global FenetreJeu
    if askyesno("Quitter le jeu", "Êtes-vous sûr de vouloir faire ça ?"):
        FenetreJeu.destroy()
    else:
        showinfo("Quitter le jeu", "Merci de votre fidélité !")

#zone de selection de la difficulté :
diff = ""
def difficult ():
    global diff, var, qdiff
    qdiff = Tk()
    var = StringVar(qdiff)
    def validdiff ():
        diff = str(var.get())
        #print("Vous avez choisi la difficulté", diff,"!")
        if diff == "facile":
            print("Bienvenue dans la version la plus simple de ce jeu !\nVous pouvez lancer le jeu !")
        elif diff == "normale":
            print("Bienvenue dans la version de difficulté normale de ce jeu !\nVous pouvez lancer le jeu !")
        elif diff == "difficile":
            print("Bienvenue dans la version la plus difficile de ce jeu !\nVous pouvez lancer le jeu !")
    qdiff.title("Quelle difficulté choisir ?")
    def quit ():
        qdiff.destroy()
    bouton1 = Radiobutton(qdiff, text="Facile", variable=var, value="facile", command = validdiff)
    bouton2 = Radiobutton(qdiff, text="Normale", variable=var, value="normale", command = validdiff)
    bouton3 = Radiobutton(qdiff, text="Difficile", variable=var, value="difficile", command = validdiff)
    bouton1.pack()
    bouton2.pack()
    bouton3.pack()
    boutonvalid = Button(qdiff, text = "Valider", command = quit)
    boutonvalid.pack()

##On forme une grille pour afficher les cartes :
"""
1 : fond
2 à 6 : tas
7 à 60 : cartes 1er aff
"""

def first_affichage ():
    # Canevas.delete("all")
    # Canevas.create_image(0,0, anchor = NW, image = fond)
    # Canevas.pack()
    if len(final) != 0:
        nb_tas_succ = int(len(final)/13)
        for i in range (nb_tas_succ):
            Canevas.create_image((i*23+40),550, anchor = NW, image = dos)
    if len(tas) != 0:
        nb_tas_dis = int(len(tas)/10)
        for i in range (nb_tas_dis):
            Canevas.create_image((i*(-15)+1130),550, anchor = NW, image = dos)

    for i in range (len(list[0])) :
        for j in range (len(list)) :
            t = int(list[j][i])
            # print(t)
            x = 99
            y = 153
            if t == 1:
                u = as_pic
            elif t == 2:
                u = de_pic
            elif t == 3:
                u = tr_pic
            elif t == 4:
                u = qu_pic
            elif t == 5:
                u = ci_pic
            elif t == 6:
                u = si_pic
            elif t == 7:
                u = se_pic
            elif t == 8:
                u = hu_pic
            elif t == 9:
                u = ne_pic
            elif t == 10:
                u = di_pic
            elif t == 11:
                u = va_pic
            elif t == 12:
                u = da_pic
            elif t == 13:
                u = ro_pic
            Canevas.create_image((j*(x+23)+40),(i*(y-123)+40), anchor = NW, image = u)
    Canevas.pack()

def affichage_tas () :
    global tas
    a = len(tas)/10
    x = str(int(2+a))
    # print(x)
    Canevas.delete(x)

def Clic_carte (event):
    global CLIC, X, Y, xmax, ymax, tag_carte
    X = event.x
    Y = event.y
    tag_carte = Canevas.find_withtag(CURRENT)[0]
    print(tag_carte)

    # coordonnées de l'objet
    xmin,ymin = Canevas.coords(tag_carte)
    xmax = xmin + 99
    ymax = ymin + 153
    #print("Position objet -> ",xmin,ymin,xmax,ymax)
    if xmin<=X<=xmax and ymin<=Y<=ymax:
        if tag_carte != 1 and tag_carte != 2 and tag_carte != 3 and tag_carte != 4 and tag_carte != 5 and tag_carte != 6 :
            CLIC = True
        else:
            CLIC = False
        if tag_carte == 2 or tag_carte == 3 or tag_carte == 4 or tag_carte == 5 or tag_carte == 6 :
            distrib_tas()
            affiche_colone(list)
            affichage_tas()
            Canevas.update()
    else:
        CLIC = False
    print("DETECTION CLIC SUR OBJET -> ",CLIC)


def Drag (event):
    """ Gestion de l'événement bouton gauche enfoncé """
    X = event.x
    Y = event.y
    #print("Position du pointeur -> ",X,Y)

    if CLIC == True:
       # limite de l'objet dans la zone graphique
        if X<0: X=0
        if X>Largeur: X=Largeur
        if Y<0: Y=0
        if Y>Hauteur: Y=Hauteur
        # mise à jour de la position de l'objet (drag)
        Canevas.coords(tag_carte ,X-60 ,Y-80)
        Canevas.tag_raise(tag_carte)


#On crée notre fenetre :
FenetreJeu = Tk()
FenetreJeu.title("Solitaire Spider - Projet ISN Terminale")

#On crée le fond de la fenêtre avec le canevas :
fond = ImageTk.PhotoImage(file = "projet/images/fond.jpg")
Largeur = 1280
Hauteur = 720
Canevas = Canvas(FenetreJeu, width = Largeur, height = Hauteur)
Canevas.create_image(0,0, anchor = NW, image = fond)
Canevas.pack()

#On crée un menu pour choisir la difficulté, quitter le jeu, et démarrer le jeu :
menubar = Menu(FenetreJeu)
menuoption = Menu(menubar,tearoff=0)
menuoption.add_command(label="Choisir la difficulté", command=difficult)
menuoption.add_command(label="Commencer à jouer", command=startpartie)
menuoption.add_separator()
menuoption.add_command(label="Quitter le jeu", command=quitter)
menubar.add_cascade(label="Options",menu=menuoption)
FenetreJeu.config(menu=menubar)

#On ajoute les fichiers pour les cartes :
as_pic = ImageTk.PhotoImage(file = "projet/images/asp.jpg")
de_pic = ImageTk.PhotoImage(file = "projet/images/2p.jpg")
tr_pic = ImageTk.PhotoImage(file = "projet/images/3p.jpg")
qu_pic = ImageTk.PhotoImage(file = "projet/images/4p.jpg")
ci_pic = ImageTk.PhotoImage(file = "projet/images/5p.jpg")
si_pic = ImageTk.PhotoImage(file = "projet/images/6p.jpg")
se_pic = ImageTk.PhotoImage(file = "projet/images/7p.jpg")
hu_pic = ImageTk.PhotoImage(file = "projet/images/8p.jpg")
ne_pic = ImageTk.PhotoImage(file = "projet/images/9p.jpg")
di_pic = ImageTk.PhotoImage(file = "projet/images/10p.jpg")
va_pic = ImageTk.PhotoImage(file = "projet/images/vap.jpg")
da_pic = ImageTk.PhotoImage(file = "projet/images/dap.jpg")
ro_pic = ImageTk.PhotoImage(file = "projet/images/rop.jpg")
dos = ImageTk.PhotoImage(file = "projet/images/dos.jpg")

Canevas.bind('<Button-1>', Clic_carte)
Canevas.bind('<B1-Motion>', Drag) # événement bouton gauche enfoncé (hold down)

#Ne pas enlever (et mettre à la fin)
FenetreJeu.mainloop()