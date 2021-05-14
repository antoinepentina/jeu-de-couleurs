#Projet jeu des couleurs
#L1 MIASHS TD02
#Pentinat Antoine, Négrier Amélie, Tairou Iswat, Auclerc Emre, Huguen Marine, Rafiq Loubna

#création de la fenetre graphique
from tkinter import *
import tkinter as tk
import random as rd
import time
from turtle import *


racine = Tk()
racine.title("Jeu de couleurs")
racine.geometry("900x300")
racine.config(background="azure2")
canvas=Canvas(racine, width=300, height= 900, bg="azure2")
canvas2=Canvas(racine, width=300, height= 900, bg="azure2")

def réinitialiser():
    """Fonction qui remet le score à 0 et qui remet le compte à rebours à 30 secondes"""
    pass

#ajout des fonctions
def incremente():
    """Fonction qui génère un compte à rebours de 30 secondes"""
    global compteur
   if compteur > 0 :
        compteur -=1
        compteur_lbl['text'] = str(compteur)
        canvas.after(1000, incremente)
        return compteur 



compteur = 30
compteur_lbl = tk.Label(canvas, text=str(compteur), font=("", 16))
compteur_lbl.pack()
score = 0

def changement(str, couleur):
    """fonction qui permet de changer aléatoirement la couleur et le mot (du label_title)"""
    global label_title
    global score
    label_title["text"]= str
    label_title["fg"]= couleur
    score+=1

#Apparition du mot du milieu
couleurs = ['deep sky blue','firebrick1','spring green2','Gold','DeepPink2','chocolate1','white']
mots = ['Bleu','Rouge','Vert','Jaune','Rose','Orange','Blanc','Violet','Noir','Marron','Gris','Beige']
label_title = Label(canvas, text=rd.choice(mots), font=("Cassia",40), fg=rd.choice(couleurs), bg='azure2')
label_title.pack()

    

label_text = Label(canvas, text="Tapez la couleur des mots et pas le texte des mots !", bg="azure2", font=("Cassia", 20))
label_score = Label(canvas, text="Score : " + str(score), bg ="azure2", font=("Cassia", 18))



#ajout des boutons

first_button = Button(canvas, text="Démarrer", command=incremente)
second_button = Button(canvas, text="réinitialiser", command = réinitialiser)
third_button = Button(canvas, text='Bleu', bg=couleurs[0], command= lambda : changement(rd.choice(mots), rd.choice(couleurs)))
fourth_button = Button(canvas, text='Rouge', bg=couleurs[1], command = lambda: changement(rd.choice(mots), rd.choice(couleurs)))
fifth_button = Button(canvas, text='Vert', bg=couleurs[2], command= lambda : changement(rd.choice(mots), rd.choice(couleurs)))
sixth_button = Button(canvas, text='Jaune', bg=couleurs[3], command= lambda : changement(rd.choice(mots), rd.choice(couleurs)))
seventh_button = Button(canvas, text='Rose', bg=couleurs[4], command= lambda : changement(rd.choice(mots), rd.choice(couleurs)))
eighth_button = Button(canvas, text='Orange', bg=couleurs[5], command= lambda : changement(rd.choice(mots), rd.choice(couleurs)))
ninth_button = Button(canvas, text='Blanc', bg=couleurs[6], command= lambda : changement(rd.choice(mots), rd.choice(couleurs)))



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


racine.mainloop()
