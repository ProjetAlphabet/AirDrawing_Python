# -*- coding: utf-8 -*-
"""
Created on Wed Apr 18 17:02:43 2[018

@author: blook
"""
# Support (variables globales)
from numpy import asarray

# Définition du nom des modèles
# /!\ SAISIR LES NOMS ET LES MODELES CORRESPONDANT AU MEME INDICE /!\ #
models_alph_name = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z',]
models_nums_name = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
models_shap_name = ["carré\n", "cercle\n", "losange\n", "triangle\n"]

models_alph_name_array = asarray(models_alph_name)
models_nums_name_array = asarray(models_nums_name)
models_shap_name_array = asarray(models_shap_name)

# Definition du chemin des modèles
models_alph = (["./res/models/alphabet/a/maj_model.png", "./res/models/alphabet/a/maj_toshow.png"],
               ["./res/models/alphabet/b/maj_model.png", "./res/models/alphabet/b/maj_toshow.png"],
               ["./res/models/alphabet/c/maj_model.png", "./res/models/alphabet/c/maj_toshow.png"],
               ["./res/models/alphabet/d/maj_model.png", "./res/models/alphabet/d/maj_toshow.png"],
               ["./res/models/alphabet/e/maj_model.png", "./res/models/alphabet/e/maj_toshow.png"],
               ["./res/models/alphabet/f/maj_model.png", "./res/models/alphabet/f/maj_toshow.png"],
               ["./res/models/alphabet/g/maj_model.png", "./res/models/alphabet/g/maj_toshow.png"],
               ["./res/models/alphabet/h/maj_model.png", "./res/models/alphabet/h/maj_toshow.png"],
               ["./res/models/alphabet/i/maj_model.png", "./res/models/alphabet/i/maj_toshow.png"],
               ["./res/models/alphabet/j/maj_model.png", "./res/models/alphabet/j/maj_toshow.png"],
               ["./res/models/alphabet/k/maj_model.png", "./res/models/alphabet/k/maj_toshow.png"],
               ["./res/models/alphabet/l/maj_model.png", "./res/models/alphabet/l/maj_toshow.png"],
               ["./res/models/alphabet/m/maj_model.png", "./res/models/alphabet/m/maj_toshow.png"],
               ["./res/models/alphabet/n/maj_model.png", "./res/models/alphabet/n/maj_toshow.png"],
               ["./res/models/alphabet/o/maj_model.png", "./res/models/alphabet/o/maj_toshow.png"],
               ["./res/models/alphabet/p/maj_model.png", "./res/models/alphabet/p/maj_toshow.png"],
               ["./res/models/alphabet/q/maj_model.png", "./res/models/alphabet/q/maj_toshow.png"],
               ["./res/models/alphabet/r/maj_model.png", "./res/models/alphabet/r/maj_toshow.png"],
               ["./res/models/alphabet/s/maj_model.png", "./res/models/alphabet/s/maj_toshow.png"],
               ["./res/models/alphabet/t/maj_model.png", "./res/models/alphabet/t/maj_toshow.png"],
               ["./res/models/alphabet/u/maj_model.png", "./res/models/alphabet/u/maj_toshow.png"],
               ["./res/models/alphabet/v/maj_model.png", "./res/models/alphabet/v/maj_toshow.png"],
               ["./res/models/alphabet/w/maj_model.png", "./res/models/alphabet/w/maj_toshow.png"],
               ["./res/models/alphabet/x/maj_model.png", "./res/models/alphabet/x/maj_toshow.png"],
               ["./res/models/alphabet/y/maj_model.png", "./res/models/alphabet/y/maj_toshow.png"],
               ["./res/models/alphabet/z/maj_model.png", "./res/models/alphabet/z/maj_toshow.png"])

models_nums = (["./res/models/numbers/0/model.png", "./res/models/numbers/0/toshow.png"],
               ["./res/models/numbers/1/model.png", "./res/models/numbers/1/toshow.png"],
               ["./res/models/numbers/2/model.png", "./res/models/numbers/2/toshow.png"],
               ["./res/models/numbers/3/model.png", "./res/models/numbers/3/toshow.png"],
               ["./res/models/numbers/4/model.png", "./res/models/numbers/4/toshow.png"],
               ["./res/models/numbers/5/model.png", "./res/models/numbers/5/toshow.png"],
               ["./res/models/numbers/6/model.png", "./res/models/numbers/6/toshow.png"],
               ["./res/models/numbers/7/model.png", "./res/models/numbers/7/toshow.png"],
               ["./res/models/numbers/8/model.png", "./res/models/numbers/8/toshow.png"],
               ["./res/models/numbers/9/model.png", "./res/models/numbers/9/toshow.png"])

models_shap = ["./res/models/shapes/carre_model.png", "./res/models/shapes/cercle_model.png", "./res/models/shapes/losange_model.png", "./res/models/shapes/triangle_model.png"]

models_alph_array = asarray(models_alph)
models_nums_array = asarray(models_nums)
models_shap_array = asarray(models_shap)

# Variables globales
cam = "./__temp__/cam.png"
saved = "./__temp__/saved.png"
draw = "./__temp__/draw.png"
process = "./__temp__/processed.png"
white = "./__temp__/white.png"

gamemode = -1
model = 0
thickness = 10
main_color = (0, 0, 255)
window_color = "#000000"