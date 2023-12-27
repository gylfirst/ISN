from tkinter import *
from PIL import ImageTk, Image
from functools import partial

list = [[1,2,3,4,5,6,7,8,9,10,11,12,13],[1,2,3,4,5,6,7,8,9,10,11,12,13],[1,2,3,4,5,6,7,8,9,10,11,12,13],[1,2,3,4,5,6,7,8,9,10,11,12,13],[1,2,3,4,5,6,7,8,9,10,11,12,13],[1,2,3,4,5,6,7,8,9,10,11,12,13],[1,2,3,4,5,6,7,8,9,10,11,12,13],[1,2,3,4,5,6,7,8,9,10,11,12,13],[1,2,3,4,5,6,7,8,9,10,11,12,13],[1,2,3,4,5,6,7,8,9,10,11,12,13]]

root = Tk()
#CARTE DIMENSIONS : 99x153 (ESPACEMENT ENTRE COLONNE DE 23, ET ESPACEMENT ENTRE DEBUT CARTE HAUTEUR DE 30 :
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

#f1 = Frame(root)
#Label(f1, image = fond).grid()
Canevas = Canvas(root, width = 1280, height = 720)

for i in range (len(list)):
    for j in range (len(list[i])):
        x = 99
        y = 153
        t = int(list[i][j])
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
        #Label(f1, image = u).grid(row=j, column=i)
        Canevas.create_image((i*(x+23)+40),(j*(y-123)+40), anchor = NW, image = u)
#f1.pack()
Canevas.pack()

root.mainloop()
