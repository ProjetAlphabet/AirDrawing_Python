# Air Drawing
Projet de traitement vidéo

Mini Projet d'informatique sous Python 3 \
Lycée Déodat de Séverac

## Informations importantes
Certains éléments du projet ne sont pas parfaitement fonctionnels, notamment les modes chiffres et lettres qui sont à améliorer et optimiser grandement : ils souffrent d'un paramétrage des modèles qui n'est pas des plus parfaits et qui doit être revu et optimisé. \
Pour démarrer le logiciel, lancer le script 'main.py' avec Python 3.

**Attention:** *il est impératif d'utiliser un objet de couleur vert/vert fluo/jaune pour pouvoir tracer les formes. Il est conseillé d'utiliser un objet à deux faces dont l'une des deux faces est d'une autre couleur que vert/jaune pour pouvoir "lever" le pinceau. Vous pouvez toujours si vous le souhaitez (et si vous y arrivez) changer l'intervalle de couleur détecté.*

## Requis
Pour faire fonctionner le logiciel, il est nécessaire de remplir les pré-requis suivant :
* Python 3 (3.6 préférée)
* OpenCV2
* Tkinter
* Toutes les bibliothèques Python relatives aux calculs mathématiques et au traitement de l'image

## Installer OpenCV2
Pour installer OpenCV2, il vous faudra, en fonction de la distribution de Python choisie, effectuer les étapes suivantes :

### Anaconda3 (recommandé)
Ouvrir Anaconda Prompt et saisir les lignes suivantes pour installer OpenCV2 et Tkinter, s'il ne l'est pas déjà :

```
conda install -c anaconda tk
pip install opencv-contrib-python
```

### WinPython
Ouvrir WinPython Command Prompt et saisir la ligne de code suivante :

```
pip install opencv-contrib-python
```

Pour Tkinter, il devrait être installé par défaut

## Auteurs
* **Guillaume Obin** - *Eléments relatifs à la capture* - [FinnZy](https://github.com/FinnZy)
* **Marie-Léa Hupin** - *Interface utilisateur* - [Marie-Lea](https://github.com/Marie-Lea)
* **Cécile Becquié** - *Traitement de l'image* - [cbecq](https://github.com/cbecq)
* **Emilie Vintrou-Vidal** - *Traitement de l'image* - [FoxyProject](https://github.com/FoxyProject)

## Licence
Ce projet est sous licence GNU - voir [LICENSE.md](LICENSE.md) pour plus de détails
