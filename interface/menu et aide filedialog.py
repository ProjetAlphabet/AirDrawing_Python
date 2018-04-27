from tkinter import *
import tkinter.messagebox
import tkinter.filedialog
from tkinter import colorchooser

#A FAIRE REUSSIR A EXECUTER LA SECONDE FENETRE CONTENANT LE TRACE ET LE RESULTAT

def repondre():
 affichage['text'] = reponse.get()  # lecture du contenu du widget "reponse"

def Nom():
    Nom1.delete(ALL)
    nom = Label(Nom1, text = "Nom d'utilisateur :")
    reponse = Entry(Nom1)
    valeur = Button(Nom1, text =' Valider', command=repondre)
    affichage = Label(Nom1, width=25)
    votre_nom=Label(Nom1, text='') #votre nom est
    nom.pack()
    reponse.pack()
#    valeur.pack()
#    votre_nom.pack()
#    affichage.pack()
    print(reponse)


def Astuce():
    tkinter.messagebox.showinfo("Astuce","Maintenir une position stable")

def Apropos():
    tkinter.messagebox.showinfo("A propos","Python & Tkinter\n(C) Guillaume Obin\n Cécile Becquie\n Emilie Vintrou\n Marie-Léa Hupin")

def couleura():
    Frame0['bg'] = "blue"
    Frame1['bg'] = "blue"
    Frame2['bg'] = "blue"
    Frame3['bg'] = "blue"    
    Mafenetre['bg'] = "blue"
    Frame4['bg'] = "blue"
    Frame42['bg'] = "blue"
    Frame43['bg'] = "blue"

def couleurb():
    Frame0['bg'] = "bisque"    
    Frame1['bg'] = "bisque"
    Frame2['bg'] = "bisque"
    Frame3['bg'] = "bisque" 
    Mafenetre['bg'] = "bisque"
    Frame4['bg'] = "bisque"
    Frame42['bg'] = "bisque"
    Frame43['bg'] = "bisque"

def couleurfond():
    color = colorchooser.askcolor()
    color = str(color)
    couleur1 = color.split("\'")
    couleur2 = couleur1[1]
    Mafenetre['bg'] = couleur2
    Frame0['bg'] = couleur2
    Frame1['bg'] = couleur2
    Frame2['bg'] = couleur2
    Frame3['bg'] = couleur2
    Frame4['bg'] = couleur2
    Frame42['bg'] = couleur2
    Frame43['bg'] = couleur2
    diff1["text"] = "la couleur de la spatule!"
    diff1['bg'] = couleur2
    quest['bg'] = couleur2
    Titre1['bg'] = couleur2
    deco1['bg'] = couleur2
    Nom1['bg'] = couleur2

def épaisseur():
    a = int(valeur.get())
    diff["text"] = a, "pixels"
    
    
"""
def Ouvrir():
    filename = tkinter.filedialog.askopenfilename(title="Ouvrir une image",filetypes=[('png files','.png'),('gif files','.gif'),('all files','.*')])
    final = PhotoImage(file=filename)
    finalement = final.subsample(3,3)
    Fin.create_image(0,0,anchor=NW,image=finalement)
    Fin.config(height=finalement.height(),width=finalement.width())"""


#___Fentre principale, Main window
Mafenetre = Tk()
Mafenetre.title("Air drawing - mini projet")
Mafenetre.geometry("900x900")
Mafenetre.resizable(width=False,height=False)


#___Création du Menu (widget)
menubar = Menu(Mafenetre)

menufichier = Menu(menubar,tearoff=0)
menufichier.add_command(label="Nom d'utilisateur",command=Nom)
menufichier.add_command(label="Quitter",command=Mafenetre.destroy)
menubar.add_cascade(label="Fenêtre", menu=menufichier)

menuaide = Menu(menubar,tearoff=0)
menuaide.add_command(label="A propos",command=Apropos)
menubar.add_cascade(label="Aide", menu=menuaide)
menuaide.add_command(label="Astuce",command=Astuce)

#Affichage du menu
Mafenetre.config(menu=menubar)

#___Insertion du titre

# Image titre
photo = PhotoImage(file="titre.png")
photo_taille=photo.subsample(2,2)

# création d'un widget Frame appellé titre dans Mafenetre
Titre = Frame(Mafenetre,borderwidth=0,relief=GROOVE, bg="black")
Titre.pack(padx=0,pady=0)

Titre1=Label(Titre, image=photo_taille, bg="black")
Titre1.pack()

"""# Création d'une zone graphique (widget canvas)
Largeur = 800
Hauteur = 300
Canevas = Canvas(Mafenetre,width = Largeur, height =Hauteur, bg="black", borderwidth=0)
Canevas.create_image(0,0,anchor=NW, image=photo_taille)
print("jusqu'ici ok")
Canevas.pack(anchor=CENTER)"""

#___Insertion déco

# Image deco
photodeco = PhotoImage(file="2.png")
photodeco_taille=photodeco.subsample(2,2)

deco = Frame(Mafenetre,borderwidth=0,relief=GROOVE, bg="black")
deco.pack(padx=0,pady=0)

deco1=Label(deco, image=photodeco_taille, bg="black")
deco1.pack(side=LEFT)

#___Nom d'utilisateur

# Création d'une zone graphique (widget canvas)
Nom1 = Canvas(deco,width = 71, height =75, bg="black", bd=0)
U = PhotoImage(file="utilisateur.png")
U_2 = U.subsample(2,2)
Nom1.create_image(0,0,anchor=NW, image=U_2)
print("jusqu'ici Nom1")
Nom1.pack(side=RIGHT,padx=10,pady=10)

#___partie blocks enchassées

Mafenetre['bg']='black' # couleur de fond

# création du widget Frame0 dans la fenêtre principale contient 1-2-3
Frame0 = Frame(Mafenetre,borderwidth=2,relief=GROOVE, bg="black")
Frame0.pack(padx=1,pady=1)

# création d'un widget Frame dans Frame0
Frame1 = Frame(Frame0,borderwidth=0,relief=GROOVE, bg="black")
Frame1.pack(side=LEFT,padx=10,pady=10)

# création d'un second widget Frame dans Frame0
Frame2 = Frame(Frame0,borderwidth=0,relief=GROOVE, bg="black")
Frame2.pack(side=LEFT,padx=10,pady=10)

# création d'un troisième widget Frame dans Frame0
Frame3 = Frame(Frame0,borderwidth=0,relief=GROOVE, bg="black")
Frame3.pack(side=LEFT,padx=10,pady=10)

# création d'un quatrième widget Frame dans la fenêtre principale
Frame4 = Frame(Mafenetre,borderwidth=2,relief=GROOVE, bg="black")
Frame4.pack(padx=10,pady=10)

# création d'un widget Frame... dans un widget Frame
# le widget Frame4 est le parent du widget Frame42
# le parent du widget Frame4 est le widget Mafenetre (fenêtre principale)
Frame42 = Frame(Frame4,bg="black",borderwidth=1,relief=GROOVE)
Frame42.pack(side=RIGHT,padx=10,pady=10)

Frame43 = Frame(Frame4,bg="black",borderwidth=1,relief=GROOVE)
Frame43.pack(side=RIGHT,padx=5,pady=10)

# création d'un widget Label et d'un widget Button dans un widget Frame
Label(Frame1,text="Choix de la représentation:\n une lettre", bg="black", fg="white").pack(padx=1,pady=1)
A =PhotoImage(file="a.png")
AA = A.subsample(2,2)
Button(Frame1,image=AA,bg='black',command=couleura, cursor="star").pack(padx=1,pady=1)

Label(Frame2,text="Choix de la représentation:\n un chiffre", bg="black", fg="white").pack(padx=1,pady=1)
B =PhotoImage(file="1.png")
BB = B.subsample(2,2)
Button(Frame2,image=BB,bg='black',command=couleurb, cursor="star").pack(padx=1,pady=1)

Label(Frame3,text="Choix de la représentation:\n une forme", bg="black", fg="white").pack(padx=1,pady=1)
C =PhotoImage(file="triangle.png")
CC = C.subsample(2,2)
Button(Frame3,image=CC,bg='black',command=Frame0.destroy, cursor="star").pack(padx=1,pady=1)

#___Epaisseur du trait
Label(Frame4,text="Choix de l'épaisseur du trait", bg="black", fg="white").pack(padx=1,pady=10)
diff = Label(Frame4,text="10 pixels", bg="green", fg="white")
diff.pack(pady=5)
valeur = DoubleVar()
scale1 = Scale(Frame4,from_ = 10, to = 20, variable = valeur ,orient = HORIZONTAL, resolution = 1, cursor="pencil",bd=0, bg="black", fg="white")
scale1.pack(pady=10, padx=23)
Button(Frame4, text="C'est partit!", command = épaisseur).pack(padx=10,pady=5)

#___couleur du tracé 

quest=Label(Frame43,text="De quelle couleur\nsera votre tracé?",bg="black", fg="white")
quest.pack(padx=20,pady=5)
Button(Frame43,text="Définir ma couleur", command=couleurfond, cursor="pencil").pack(padx=10,pady=5)
Label(Frame43,text="La couleur choisie est",bg="black", fg="white").pack(padx=20,pady=5)
diff1 = Label(Frame43, bg="red", fg="white")
diff1.pack(pady=5)

#___Résultat

Label(Frame42,text="/!\Attention/!\ \n Le tracé débute dès que la couleur sélectionné \n est détectée, retournez la spatule \nlorsque vous êtes prêts.",bg="black", fg="white").pack(padx=5,pady=10)
"""Fin = Canvas(Frame42,width = 50, height =50, bg="black", bd=0)
Fin.pack(padx=3,pady=3)"""
Button(Frame42,text="réaliser un nouveau tracé", command=Mafenetre.destroy, cursor="pencil").pack(padx=10,pady=10)


Mafenetre.mainloop()

