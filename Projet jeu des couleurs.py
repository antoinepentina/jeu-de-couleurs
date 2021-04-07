#Projet jeu des couleurs
#L1 MIASHS TD02
#Pentinat Antoine, Négrier Amélie, Tairou Iswat, Auclerc Emre, Huguen Marine, Rafiq Loubna

#création de la fenetre graphique
from tkinter import *
import tkinter as tk
racine = Tk()
racine.title("Jeu de couleurs")
racine.geometry("900x600")
racine.config(background="azure2")

#ajout d'un premier texte 
label_text = Label(racine, text="Tapez la couleur des mots et pas le texte des mots !", bg="azure2", font=("Cassia", 20))

#ajout des fonctions
def incremente():
    "Incrémente le compteur à chaque seconde"
    global compteur
    compteur += 1
    compteur_lbl['text'] = str(compteur)
    racine.after(1000, incremente)

compteur = 0
compteur_lbl = tk.Label(racine, text=str(compteur), font=("", 16))
compteur_lbl.pack()


#ajout des boutons
first_button = Button(racine, text="Démarrer")
second_button = Button(racine, text="réinitialiser")
#Affichage
first_button.pack(side=RIGHT)
second_button.pack(side=LEFT)
label_text.pack()
racine.after(1000,incremente)
racine.mainloop()
lalalalalalalalala
lilili
lololo
