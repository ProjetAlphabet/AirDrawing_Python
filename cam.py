# -*- coding: utf-8 -*-
"""
Created on Fri Apr 27 14:20:20 2018

@author: blook
"""

# Importation des bibliothèques
from PIL import Image, ImageTk
from pathlib import Path

import cv2
import tkinter
import tkinter.scrolledtext
import tkinter.filedialog
import imutils
import os

# Importation des fichiers Python3 présents dans le dossier
import bounding
import pixel_color
import resizer
import __var__ as glb
import img_ssim as sim

# Définition des bornes inférieures et supérieures de la couleur détectée
greenLower = (29, 86, 6)
greenUpper = (64, 255, 255)
pts = [] # Tableau vide contenant toutes les positions du point central de l'objet détecté

frame = None # Définition d'une frame vide pour l'utiliser à travers toutes les fonctions
imgtk = None # Définition d'une image résultat vide pour l'utiliser à travers toutes les fonctions

window = None # Définition de la fenêtre principale comme vide pour éviter les erreurs lors du changement de couleur
camera = None # Définition de la caméra comme vide pour pouvoir l'utiliser dans toutes les fonctions et l'arrêter lors de la fermeture de main.py

# Fonction d'initialisation
def init():
    text = Path("./output.txt")
    # Suppression du fichier texte s'il existe
    if text.is_file():
        os.remove('./output.txt')
        
    global pts, camera, window # Récupération du tableau de points global
    pts = [] # Réinitialisation du tableau de point à chaque initialisation
    
    camera = cv2.VideoCapture(0) # Définition de la caméra
    
    # Chargement de l'image par défaut
    default1 = cv2.imread('./res/default.png')
    
    # Conversion de l'espace de couleur de BGR à RGB pour l'affichage dans Tkinter
    b,g,r = cv2.split(default1)
    default1 = cv2.merge((r,g,b))
        
    # Conversion de l'image PIL en image Tkinter
    default2 = Image.fromarray(default1)
    default = ImageTk.PhotoImage(image=default2)
    
    # Fonction d'initialisation de la frame
    def img_frame():
        global camera
        
        # Récupère la frame actuelle
        grabbed, frame = camera.read()
        return frame
    
    # Fonction de traitement de la frame caméra
    def show_frame():
        global pts, frame # Récupération de la frame globale et du tableau de points
        
        frame = img_frame() # Récupération de la frame actuelle
        
        frame = imutils.resize(frame, height=512) # Redimensionnement de la frame
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV) # Conversion en HSV
        
        # Création d'un masque pour la couleur verte
        # Erosion et dilatation du masque pour supprimer les imperfections
        mask = cv2.inRange(hsv, greenLower, greenUpper)
        mask = cv2.erode(mask, None, iterations=2)
        mask = cv2.dilate(mask, None, iterations=2)
        
        # Cherche les contours dans le masque et initialisation du centre de l'objet vert
        cnts = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[-2]
        center = None
    
        # S'il y a un contour de trouvé
        if len(cnts) > 0:
            
            # Cherche le contour le plus grand dans le masque et l'utilise pour le processus
            c = max(cnts, key=cv2.contourArea)
            ((x, y), radius) = cv2.minEnclosingCircle(c)
            M = cv2.moments(c)
            center = (int(M["m10"] / M["m00"]), int(M["m01"] / M["m00"]))
        
            # Si le cercle a une taille minimum (réglable en fonction de ce que l'on souhaite)
            if radius > 10:
                # Déssine le contour et le centre de l'objet sur la frame
                cv2.circle(frame, (int(x), int(y)), int(radius),(0, 255, 255), 2)
                cv2.circle(frame, center, 5, glb.main_color, -1)
            
        # Ajout du centre de l'objet dans le tableau de points
        pts.append(center)
    
        # Boucle permettant de déssiner les lignes associées aux points
        for i in range(1, len(pts)):
            # S'il n'y a pas de points dans la liste
            if pts[i - 1] is None or pts[i] is None:
                continue
        
            # Sinon, déssine des lignes associées aux points sur la frame
            cv2.line(frame, pts[i - 1], pts[i], glb.main_color, glb.thickness)
        
        frame = cv2.flip(frame, 1) # Symétrie de la vidéo
        
        # Processus de conversion Tkinter
        cv2image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGBA) # Conversion de l'espace de couleur de BGR en RGB
        
        img = Image.fromarray(cv2image) # Chargement de la frame avec PIL
        imgtk = ImageTk.PhotoImage(image=img) # Chargement de la frame PIL avec Tkinter
        
        lmain.imgtk = imgtk # Chargement de l'image Tkinter dans une Frame Tkinter
        lmain.configure(image=imgtk) # Configuration de la Frame Tkinter
        lmain.after(10, show_frame) # Rafraîchissement de la Frame Tkinter
    
    # Fonction de néttoyage du tracé
    def key_clear(e):
        global pts # Récupération du tableau de points
        pts = [] # Vide le tableau de points pour effacer le tracé
        
        
        #DEBOGAGE
        if glb.gamemode == 0:
            print('gamemode 0')
        elif glb.gamemode == 1:
            print('gamemode 1')
        elif glb.gamemode == 2:
            print('gamemode 2')
        else:
            print('ERR: code -1')
        print('clear')
        
    
    # Fonction de traitement de l'image pour la détection du tracé    
    def key_print(e):
        global pts, frame, imgtk
        
        # Enregistrement de l'image
        cv2.imwrite(glb.cam, frame)
            
        # Effacement du tracé
        pts = []
        
        # Traitement de l'image
        bounding.processing() # Récupération du tracé seul
        pixel_color.convert_pix() # Conversion des pixels autres que ceux du tracé en noir
        resizer.resize_image() # Redimensionnement de l'image en 512x512
        pixel_color.convert_white() # Conversion des pixels du tracé en blanc
    
        if glb.gamemode == 0:
            indic, sim_compare = sim.compare(glb.models_shap_array, glb.white, 4) # Récupération de l'indice du modèle et du SSIM
            glb.model = indic # Ecriture de l'indice du modèle dans le fichier contenant toutes les variables globales
            
            img = cv2.imread(glb.models_shap_array[glb.model]) # Charge l'image associée
            
            write_file(glb.models_shap_name_array[glb.model]) # Exécution de la fonction d'écriture du nom du résultat
            
            print(sim_compare) # Affiche la valeur du SSIM correspondant
            
        elif glb.gamemode == 1:
            indic, sim_compare = sim.compare(glb.models_nums_array, glb.white, 10) # Récupération de l'indice du modèle et du SSIM
            glb.model = indic # Ecriture de l'indice du modèle dans le fichier contenant toutes les variables globales
            
            img = cv2.imread(glb.models_nums_array[glb.model, 1]) # Charge l'image associée
            
            write_file(glb.models_nums_name_array[glb.model]) # Exécution de la fonction d'écriture du nom du résultat
            
            print(sim_compare) # Affiche la valeur du SSIM correspondant
            
        elif glb.gamemode == 2:
            indic, sim_compare = sim.compare(glb.models_alph_array, glb.white, 26) # Récupération de l'indice du modèle et du SSIM
            glb.model = indic # Ecriture de l'indice du modèle dans le fichier contenant toutes les variables globales
            
            img = cv2.imread(glb.models_alph_array[glb.model, 1]) # Charge l'image associée
            
            write_file(glb.models_alph_name_array[glb.model]) # Exécution de la fonction d'écriture du nom du résultat
            
            print(sim_compare) # Affiche la valeur du SSIM correspondant
        
        print('Done')
        
        # Conversion de l'espace de couleur de BGR à RGB pour l'affichage dans Tkinter
        b,g,r = cv2.split(img)
        img = cv2.merge((r,g,b))
        
        # Conversion de l'image PIL en image Tkinter
        im = Image.fromarray(img)
        imgtk = ImageTk.PhotoImage(image=im)
        
        tk_img() # Mise à jour de la frame résultat (de droite) pour l'affichage du résultat
        
        open_file()
       
    # Fonctions des raccourcis clavier
    def key_close(e):
        on_closing()
        
    def key_about(e):
        about()

    def key_help(e):
        help_window()
        
    def key_new(e):
        new_file()
        
    def key_save(e):
        save_file()

    # Fonction de fermeture de la fenêtre
    def on_closing():
        global camera, window
        
        text = Path("./output.txt")
        if text.is_file():
            os.remove('./output.txt')
        camera.release() # Arrête l'utilisation de la caméra pour permettre une réutilisation ultérieure
        window.destroy() # Détruit la fenêtre
        window = None
    
    # Fonction d'actualisation du résultat
    def tk_img():
        Frame1.configure(image=imgtk) # Chargement de l'image finale
        Frame1.image = imgtk # Affichage de l'image finale
 
    # Fonction d'écriture du fichier texte
    def write_file(txt):
        # Ouverture du fichier texte
        with open('output.txt','a') as file:
            content = txt
            # Ecriture du nom du dessin dans le fichier texte
            file.write(content)
            file.close() # Fermeture du fichier
    
    # Fonction d'actualisation du fichier texte
    def open_file():
        # Ouverture du fichier texte
        with open('output.txt','r') as file:
            content = file.read() # Lexture du fichier
            
            # Mise en écriture de la Frame
            textPad.config(state=tkinter.NORMAL)
            textPad.delete('1.0', tkinter.END) # Suppression du contenu précédent
            textPad.insert('1.0', content, 'name') # Ajout du nouveau contenu
            textPad.tag_config('name', background='black', foreground='white') # Stylisation du texte
            # Bloquage en mode lecture seule de la Frame
            textPad.config(state=tkinter.DISABLED)
            
            file.close() # Fermeture du fichier texte
    
    # Fonction nouveau fichier
    def new_file():
        text = Path("./output.txt")
        # Vérification de la présence du fichier pour éviter les erreurs
        if text.is_file():
            os.remove('./output.txt') # Suppression du fichier texte
            
            # Mise en écriture de la Frame
            textPad.config(state=tkinter.NORMAL)
            textPad.delete('1.0', tkinter.END) # Suppression du contenu
            # Bloquage en lecture seule de la Frame
            textPad.config(state=tkinter.DISABLED)
        
        # Charge l'image résultat par défaut
        Frame1.configure(image=default)
        Frame1.image = default
    
    # Fonction sauver le fichier
    def save_file():
        # Affichage de la boîte de dialogue de sauvegarde
        file = tkinter.filedialog.asksaveasfile(mode='w', defaultextension=".txt", filetypes=[("Fichier texte", "*.txt"), ("Tous les fichiers", "*.*")])
        # Vérification de l'existence du chemin d'accès pour éviter les erreurs
        if file != None:
            # Ecriture du fichier dans sa totalité et ajout d'un retour à la ligne
            data = textPad.get('1.0', tkinter.END+'-1c')
            file.write(data) # Ecriture du fichier
            file.close() # Fermeture du fichier
    
    # Fonction fenêtre aide
    def help_window():
        tkinter.messagebox.showinfo("Astuce","Maintenir une position stable")

    # Fonction fenêtre à propos
    def about():
        tkinter.messagebox.showinfo("A propos","Python & Tkinter\n\n Auteurs :\n Guillaume Obin\n Cécile Becquie\n Emilie Vintrou\n Marie-Léa Hupin \n\n Réalisé avec OpenCV2")
    
    # Configuration de l'interface
    window = tkinter.Toplevel() # Création de la fenêtre principale
    
    # Définition du nom de la fenêtre, en fonction du mode
    if glb.gamemode == 0:
        window.wm_title("Camera - Mode formes")
    if glb.gamemode == 1:
        window.wm_title("Camera - Mode chiffres")
    if glb.gamemode == 2:
        window.wm_title("Camera - Mode alphabet")
    
    # Mode par défaut, lorsque le script n'est pas lancé à travers main.py
    if glb.gamemode == -1:
        window.wm_title("Camera - Mode -1 (VEUILLEZ LANCER LA CAMERA A TRAVERS LA FENETRE PRINCIPALE!)")
    
    # Création d'une barre de menus
    menubar = tkinter.Menu(window)
    
    # Menu fichier
    menufichier = tkinter.Menu(menubar,tearoff=0)
    menufichier.add_command(label="Nouveau", underline=1, command=new_file, accelerator="Ctrl+N")
    menufichier.add_command(label="Savegarder...", underline=1, command=save_file, accelerator="Ctrl+S")
    
    menufichier.add_separator() # Ajout d'un séparateur pour plus de lisibilité
    
    menufichier.add_command(label="Fermer", underline=1, command=on_closing, accelerator="Ctrl+Q")
    menubar.add_cascade(label="Fichier", menu=menufichier) # Ajout du menu à la barre de menus
    
    # Menu aide
    menuaide = tkinter.Menu(menubar,tearoff=0)
    menuaide.add_command(label="À propos", underline=1, command=about, accelerator="F12")
    
    menuaide.add_separator() # Ajout d'un séparateur pour plus de lisibilité
    
    menuaide.add_command(label="Aide", underline=1, command=help_window, accelerator="F1")
    menubar.add_cascade(label="Aide", menu=menuaide) # Ajout du menu à la barre de menus
    
    window.config(background=glb.window_color, menu=menubar) # Configuration du background de la fenêtre (par défaut : noir)
    window.resizable(width=False,height=False) # Configuration de la fenêtre comme non redimensionnable

    # Configuration de la Frame Tkinter contenant la Frame caméra
    imageFrame = tkinter.Frame(window, width=682, height=512, background="black", borderwidth=2, relief=tkinter.GROOVE)
    imageFrame.grid(row=0, column=0)

    # Insertion de la Frame Tkinter de la caméra dans la Frame créée précédemment
    lmain = tkinter.Label(imageFrame, background="black")
    lmain.grid(row=0, column=0, padx=5, pady=5)  
    
    # Configuration des raccourcis clavier
    window.bind("<Delete>", key_clear) # Efface le tracé
    window.bind("<Return>", key_print) # Capture et traite le tracé
    window.bind("<Control-q>", key_close) # Ferme la fenêtre
    window.bind("<Control-n>", key_new) # Efface le résultat et le fichier texte
    window.bind("<Control-s>", key_save) # Ouvre une boîte de dialogue de sauvegarde du fichier texte
    window.bind("<F1>", key_help) # Ouvre l'aide
    window.bind("<F12>", key_about) # Ouvre la fenêtre "À propos"

    window.protocol("WM_DELETE_WINDOW", on_closing) # Action de fermeture de la fenêtre principale
    
    # Création de la Frame Tkinter contenant l'image finale (résultat du tracé)
    Frame0 = tkinter.Frame(window, width=512, height=512, borderwidth=2, relief=tkinter.GROOVE, background="black")
    Frame0.grid(row = 0, column=1, padx=5, pady=5)
    
    # Label contenant l'image du résultat
    Frame1 = tkinter.Label(Frame0, image=default, background="black") # Création d'un label vide
    Frame1.image = default # Insère l'image par défaut
    Frame1.pack(padx=5, pady=5)
    
    # Frame contenant le fichier texte
    textPad = tkinter.scrolledtext.ScrolledText(window, width=100, height=20, background="black")
    textPad.config(state=tkinter.DISABLED) # Désactive l'écriture sur la fenêtre
    textPad.grid(row=1, column=0, columnspan=2, padx=5, pady=5) # Permet d'étendre la FrameTk sur deux colonnes au lieu d'une

    show_frame() # Exécution de la fonction qui affiche la caméra sur la Frame de gauche