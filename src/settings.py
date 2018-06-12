# -*- coding: utf-8 -*-
"""
Created on Tue Jun 12 22:26:22 2018

@author: blook
"""

import configparser
from tkinter import Toplevel, Frame, Label, GROOVE

def init():
    main_window = Toplevel()
    main_window.title("Preferences...")
    main_window.geometry("200x200")
    main_window.resizable(width=False,height=False)
    
    config = configparser.ConfigParser() # Création du récepteur de fichier de configuration
    config.read('./config.ini') # Ouverture du fichier de configuration au format .ini
    cfg_lang = str(config.get('Language', 'lang')) # Récupération et conversion en int de la valeur indiquant la langue choisie
    cfg_onstartup = str(config.get('Language', 'lang_onstartup'))
    
    test_msg = "lang=" + cfg_lang + "\n" + "lang_onstartup=" + cfg_onstartup
    
    txt_frame = Frame(main_window,borderwidth=2,relief=GROOVE, bg="black")
    txt_frame.pack()
    Label(txt_frame,text=test_msg,bg="black", fg="white").pack(padx=5,pady=10)