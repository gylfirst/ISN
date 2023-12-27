pSeuil = 2.3
vSeuil = 7.41

pressure = float(input("Entrer le niveau de pression : "))
volume = float(input("Entrer le volume : "))

if pressure > pSeuil and volume > vSeuil :
    print("Arrêt immédiat !")
elif pressure > pSeuil and volume < vSeuil :
    print("Veuillez augmenter le volume de l'enceinte !")
elif pressure < pSeuil and volume > vSeuil :
    print("Veuillez diminuer le volume de l'enceinte !")
elif pressure < pSeuil and volume < vSeuil :
    print("Tout va bien !")