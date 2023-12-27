import random

nb_secret = random.randint(0,100)
compt = 0
rep = int(input("Entrer un nombre entre 0 et 100 : "))
while rep != nb_secret :
    if rep < nb_secret :
        print("Le nombre secret est plus grand !")
        rep = int(input("Réessaie ! \n"))
        compt+=1
    if rep > nb_secret :
        print("Le nombre secret est plus petit !")
        rep = int(input("Réessaie ! \n"))
        compt+=1
    if rep == nb_secret :
        print("Vous avez trouvé le nombre secret en", compt, "essais !\nIl était :", nb_secret)

