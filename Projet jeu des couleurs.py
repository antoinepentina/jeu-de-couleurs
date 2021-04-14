#Projet jeu des couleurs
#L1 MIASHS TD02
#Pentinat Antoine, Négrier Amélie, Tairou Iswat, Auclerc Emre, Huguen Marine, Rafiq Loubna

#création de la fenetre graphique
from tkinter import *
import tkinter as tk
import random as rd
import time

racine = Tk()
racine.title("Jeu de couleurs")
racine.geometry("900x300")
racine.config(background="azure2")
canvas=Canvas(racine, width=300, height= 900, bg="azure2")
#ajout d'un premier texte 
#label_text = Label(racine, text="Tapez la couleur des mots et pas le texte des mots !", bg="azure2", font=("Cassia", 20))

#ajout des fonctions
def incremente():
    "Incrémente le compteur à chaque seconde"
    global compteur
    compteur -=1
    compteur_lbl['text'] = str(compteur)
    if compteur > 0:
        canvas.after(1000, incremente)



compteur = 30
compteur_lbl = tk.Label(canvas, text=str(compteur), font=("", 16))
compteur_lbl.pack()



#Apparition du mot du milieu
couleurs = ['deep sky blue','firebrick1','spring green2','Gold','DeepPink2','chocolate1','white']
mots = ['Bleu','Rouge','Vert','Jaune','Rose','Orange','Blanc','Violet','Noir','Marron','Gris','Beige']

label_title = Label(canvas, text=rd.choice(mots), font=("Cassia",40), fg=rd.choice(couleurs), bg='azure2')
label_title.pack()


label_text = Label(canvas, text="Tapez la couleur des mots et pas le texte des mots !", bg="azure2", font=("Cassia", 20))
label_score = Label(canvas, text="Score :", bg ="azure2", font=("Cassia", 18))

class ButtonColor(Button):
    pass 

#ajout des boutons
first_button = Button(canvas, text="Démarrer")
second_button = Button(canvas, text="réinitialiser")
third_button = Button(canvas, text='Bleu', bg='deep sky blue')
fourth_button = Button(canvas, text='Rouge', bg='firebrick1')
fifth_button = Button(canvas, text='Vert', bg='spring green2')
sixth_button = Button(canvas, text='Jaune', bg='Gold')
seventh_button = Button(canvas, text='Rose', bg='DeepPink2')
eighth_button = Button(canvas, text='Orange', bg='chocolate1')
ninth_button = Button(canvas, text='Blanc', bg='white')

#Affichage
label_text.pack()
label_score.pack()
first_button.pack(side =LEFT , pady =50)
second_button.pack(side =RIGHT, pady =50)
third_button.pack(side=LEFT, padx=15, ipadx=20, ipady=10)
fourth_button.pack(side=LEFT, padx=15, ipadx=20, ipady=10)
fifth_button.pack(side=LEFT, padx=15, ipadx=20, ipady=10)
sixth_button.pack(side=LEFT, padx=15, ipadx=20, ipady=10)
seventh_button.pack(side=LEFT, padx=15, ipadx=20, ipady=10)
eighth_button.pack(side=LEFT, padx=15, ipadx=20, ipady=10)
ninth_button.pack(side=LEFT, padx=15, ipadx=20, ipady=10)
canvas.pack()

canvas.after(1000,incremente)
racine.mainloop()
