def impairs (x,y) :
    l_impairs = []
    for i in range (x,y,1) :
        if (i % 2) != 0 :
            l_impairs.append(i)
    return l_impairs

p1 = int(input("Entrer un premier nombre : "))
p2 = int(input("Entrer un deuxieme nombre : "))
liste = impairs(p1,p2)
print(liste)
