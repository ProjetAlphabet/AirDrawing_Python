# -*- coding: utf-8 -*-
"""
Created on Fri Apr 27 14:20:20 2018

@author: Marie-Léa
"""

# Importation des bibliothèques
from tkinter import Tk, Menu, PhotoImage, Frame, Label, Canvas, Button, DoubleVar, Scale, colorchooser, GROOVE, LEFT, RIGHT, NW, HORIZONTAL
from tkinter.messagebox import showinfo

import __var__ as glb
import cam

# Définition des fonctions
def help_window():
    showinfo("Aide","Maintenir une position stable")

def about():
    showinfo("A propos","Version 1.0\n\n Auteurs :\n Guillaume Obin\n Cécile Becquie\n Emilie Vintrou\n Marie-Léa Hupin \n\n Réalisé avec OpenCV2")

def couleurfond():
    color = colorchooser.askcolor()
    color = str(color)
    couleur1 = color.split("\'")
    couleur2 = couleur1[1]
    glb.window_color = couleur2
    
    # Recupération de la couleur choisie
    h = couleur2.lstrip('#')
    (r, g, b) = tuple(int(h[i:i+2], 16) for i in (0, 2, 4))
    glb.main_color = (b, g, r) # Insertion de la couleur choisie dans les vars globales
    
    diff1['bg'] = couleur2
    
    Mafenetre['bg'] = couleur2
    Titre1['bg'] = couleur2
    deco1['bg'] = couleur2
    Nom1['bg'] = couleur2
    deco['bg'] = couleur2
    
    if cam.window != None:
        cam.window['background'] = couleur2

def épaisseur():
    a = int(valeur.get())
    diff["text"] = a, "pixels"
    glb.thickness = a
    
def formes():
    glb.gamemode = 0
    cam.init()
    
def chiffres():
    glb.gamemode = 1
    cam.init()
    
def lettres():
    glb.gamemode = 2
    cam.init() 

def on_closing():
    if cam.camera != None:
        cam.camera.release()
    Mafenetre.destroy()
    
def key_close(e):
    on_closing()

def key_about(e):
    about()

def key_help(e):
    help_window()

# Fentre principale, Main window
Mafenetre = Tk()
Mafenetre.title("Air Drawing")
Mafenetre.geometry("800x680")
Mafenetre.resizable(width=False,height=False)


# Création du Menu (widget)
menubar = Menu(Mafenetre)

menufichier = Menu(menubar,tearoff=0)
menufichier.add_command(label="Quitter", underline=1, command=on_closing, accelerator="Ctrl+Q")
menubar.add_cascade(label="Fichier", menu=menufichier)
    
menuaide = Menu(menubar,tearoff=0)
menuaide.add_command(label="À propos", underline=1, command=about, accelerator="F12")
menuaide.add_separator()
menuaide.add_command(label="Aide", underline=1, command=help_window, accelerator="F1")
menubar.add_cascade(label="Aide", menu=menuaide)
    
# Affichage du menu
Mafenetre.config(menu=menubar)
    
# Insertion du titre

# Image titre
photo = PhotoImage(file="./res/UI/titre.png")
photo_taille=photo.subsample(2,2)
    
# Création d'un widget Frame appellé titre dans Mafenetre
Titre = Frame(Mafenetre,borderwidth=0,relief=GROOVE, bg="black")
Titre.pack(padx=0,pady=0)
    
Titre1=Label(Titre, image=photo_taille, bg="black")
Titre1.pack()

# Insertion déco

# Image deco
photodeco = PhotoImage(file="./res/UI/2.png")
photodeco_taille=photodeco.subsample(2,2)

deco = Frame(Mafenetre,borderwidth=0,relief=GROOVE, bg="black")
deco.pack(padx=0,pady=0)
    
deco1=Label(deco, image=photodeco_taille, bg="black")
deco1.pack(side=LEFT)
    
# Nom d'utilisateur
    
# Création d'une zone graphique (widget canvas)
Nom1 = Canvas(deco,width = 71, height =75, bg="black", bd=0)
U = PhotoImage(file="./res/UI/utilisateur.png")
U_2 = U.subsample(2,2)
Nom1.create_image(0,0,anchor=NW, image=U_2)
Nom1.pack(side=RIGHT,padx=10,pady=10)
    
# Partie blocks enchassées
    
Mafenetre['bg']='black' # couleur de fond
    
# Création du widget Frame0 dans la fenêtre principale contient 1-2-3
Frame0 = Frame(Mafenetre,borderwidth=2,relief=GROOVE, bg="black")
Frame0.pack()

text0 = Label(Frame0, text="SELECTION DU MODE", bg="black", fg="white", font=("Calibri Bold", 12))
text0.pack(pady=1)
    
# Création d'un widget Frame dans Frame0
Frame1 = Frame(Frame0,borderwidth=0,relief=GROOVE, bg="black")
Frame1.pack(side=LEFT,padx=10,pady=10)
    
# Création d'un second widget Frame dans Frame0
Frame2 = Frame(Frame0,borderwidth=0,relief=GROOVE, bg="black")
Frame2.pack(side=LEFT,padx=10,pady=10)
    
# Création d'un troisième widget Frame dans Frame0
Frame3 = Frame(Frame0,borderwidth=0,relief=GROOVE, bg="black")
Frame3.pack(side=LEFT,padx=10,pady=10)
    
# Création d'un quatrième widget Frame dans la fenêtre principale
Frame4 = Frame(Mafenetre,borderwidth=2,relief=GROOVE, bg="black")
Frame4.pack(padx=10,pady=10)
    
# Création d'un widget Frame... dans un widget Frame
# Le widget Frame4 est le parent du widget Frame42
# Le parent du widget Frame4 est le widget Mafenetre (fenêtre principale)
Frame42 = Frame(Frame4,bg="black",borderwidth=1,relief=GROOVE)
Frame42.pack(side=RIGHT,padx=10,pady=10)
    
Frame43 = Frame(Frame4,bg="black",borderwidth=1,relief=GROOVE)
Frame43.pack(side=RIGHT,padx=5,pady=10)
    
# Création d'un widget Label et d'un widget Button dans un widget Frame
A =PhotoImage(file="./res/UI/a.png")
AA = A.subsample(2,2)
Button(Frame1,image=AA,bg='black',command=lettres, cursor="star").pack(padx=5,pady=1)

B =PhotoImage(file="./res/UI/1.png")
BB = B.subsample(2,2)
Button(Frame2,image=BB,bg='black',command=chiffres, cursor="star").pack(padx=5,pady=1)

C =PhotoImage(file="./res/UI/triangle.png")
CC = C.subsample(2,2)
Button(Frame3,image=CC,bg='black',command=formes, cursor="star").pack(padx=5,pady=1)
    
thick = glb.thickness, "pixels"

# Epaisseur du trait
Label(Frame4,text="Epaisseur du trait", bg="black", fg="white").pack(padx=1,pady=10)
diff = Label(Frame4,text=thick, bg="green", fg="white")
diff.pack(pady=5)
valeur = DoubleVar()
scale1 = Scale(Frame4,from_ = 10, to = 20, variable = valeur ,orient = HORIZONTAL, resolution = 1, cursor="pencil",bd=0, bg="black", fg="white")
scale1.pack(pady=10, padx=23)
Button(Frame4, text="Valider", command = épaisseur).pack(padx=10,pady=5)
    
# Couleur du tracé 
    
quest=Label(Frame43,text="Couleur du trait",bg="black", fg="white")
quest.pack(padx=20,pady=10)
Button(Frame43,text="Définir", command=couleurfond, cursor="pencil").pack(padx=10,pady=5)
diff1 = Label(Frame43, bg="red", fg="white", width=15)
diff1.pack(pady=15)
    
# Résultat
    
Label(Frame42,text="ATTENTION! \n\n Le tracé débute dès que la couleur sélectionné \n est détectée, retournez la spatule \nlorsque vous êtes prêts.",bg="black", fg="white").pack(padx=5,pady=10)

Mafenetre.bind("<Control-q>", key_close)
Mafenetre.bind("<F1>", key_help)
Mafenetre.bind("<F12>", key_about)

Mafenetre.protocol("WM_DELETE_WINDOW", on_closing) # Action de fermeture de la fenêtre principale
    
Mafenetre.mainloop()