from tkinter import *
from PIL import ImageTk, Image
from functools import partial

list = [[1,5,1,6,7,8],[5,7,1,2,7,4],[1,8,9,2,7,7]]

# Dessiner une mosaïque de 3 * 3 labels.
# Tous les labels sont blancs sauf celui au centre qui est rouge.
# Le label rouge à une taille de 1 sur 1 mais les labels sur ses
# côtés ont une taille de 3 ce qui fait que le label rouge ne prend
# pas toute la place de sa cellule.
root = Tk()

as_pic = ImageTk.PhotoImage(file = "asp.jpg")
dos = ImageTk.PhotoImage(file = "dos.jpg")
fond = ImageTk.PhotoImage(file = "fond.jpg")

f1 = Frame(root)
#Label(f1, image = fond).grid()

Label(f1, image = as_pic).grid(row=0, column=0)
Label(f1, image = dos).grid(row=1, column=0)
f1.pack()


root.mainloop()
