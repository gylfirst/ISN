import matplotlib.pyplot as plt
import matplotlib.image as img

image = img.imread("icon.bmp")
plt.imshow(image)
plt.show()

def comptage_pixel (image) :
    nl = len(image)
    nc = len(image[0])
    nb_pixel = 0
    for l in  range (nl) :
        for c in range (nc) :
            nb_pixel = nb_pixel + 1
    return nb_pixel
    #print("Le nombre de pixels dans cette image est de :", nb_pixel, "pixels.")

def resolution (image) :
    nl = len(image)
    nc = len(image[0])
    return nc, nl
    #print("La résolution de l'image est de : ", nc, "x", nl)

def taille (image) :
    taille_img = comptage_pixel(image) * 3
    return taille_img
    #print("La taille de cette image est de :", taille_img, "octects.")