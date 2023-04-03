from tkinter import *

def affich() :
    global texte
    nb = entree.get()
    try : texte.destroy()
    except : a = 0
    texte = Label(fenetre,text=nb+" = "+scientifique(nb,chiffre_s(nb)))
    texte.pack(side=TOP,padx=5,pady=5)

def chiffre_s(nb) :
    i = 0
    for j in nb+"1" :
        if j != "0" and j != "." and j != "-" or j == "0" and i > 0 : i += 1
    return i-1

def scientifique(nb,s) :
    i = 0
    while abs(float(nb)) >= 10 : i,nb = i+1,str(float(nb)/10)
    while abs(float(nb)) < 1 : i,nb = i-1,str(float(nb)*10)
    while nb[0] == "0" : i,nb = i-1,str(float(nb)*10)
    while chiffre_s(nb) > s : nb = nb[:-1]
    while chiffre_s(nb) < s : nb = nb+"0"
    if nb[-1] == "." : nb = nb[:-1]
    return str(nb)+" x 10^"+str(i)

fenetre = Tk()
cadre = LabelFrame(fenetre,text="Donnez un nombre :",padx=5,pady=5)
cadre.pack(fill="both",expand="no")
nb = StringVar()
nb.set("")
entree = Entry(cadre,textvariable=nb,width=30)
entree.pack(side=LEFT,padx=0,pady=5)
b_appliquer = Button(cadre,text=">",command=affich).pack(side=LEFT,padx=5,pady=5)

fenetre.mainloop()