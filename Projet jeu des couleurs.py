# Projet jeu des couleurs
# L1 MIASHS TD02
# Pentinat Antoine, Négrier Amélie, Tairou Iswat, Auclerc Emre, Huguen Marine, Rafiq Loubna

# création de la fenetre graphique
import tkinter as tk
import random as rd


compteur = 30
score = 0
demarrer = False
# couleurs = ['deep sky blue','firebrick1','spring green2','Gold','DeepPink2','chocolate1','white']
couleurs = ["blue", "red", "green", "yellow", "pink", "orange", "white"]
mots = ['Bleu', 'Rouge', 'Vert', 'Jaune', 'Rose', 'Orange', 'Blanc', 'Violet', 'Noir', 'Marron', 'Gris', 'Beige']


def réinitialiser():
    """Fonction qui remet le score à 0 et qui remet le compte à rebours à 30 secondes"""
    global demarrer, score, compteur
    compteur = 30
    compteur_lbl['text'] = str(compteur)
    score = 0
    label_score["text"] = "Score : " + str(score)
    demarrer = False
    canvas.after_cancel(repeat)


# ajout des fonctions
def incremente():
    """Fonction qui génère un compte à rebours de 30 secondes"""
    global compteur, demarrer, repeat
    demarrer = True
    if compteur > 0:
        compteur -= 1
        compteur_lbl['text'] = str(compteur)
        repeat = canvas.after(1000, incremente)
    else:
        demarrer = False


def changement(color):
    """fonction qui permet de changer aléatoirement la couleur et le mot (du label_title)"""
    global label_title, score
    if demarrer is True:
        if label_title["fg"] == color:
            score += 1
            label_score["text"] = "Score : " + str(score)
        label_title["text"] = rd.choice(mots)
        label_title["fg"] = rd.choice(couleurs)
        print(label_title["fg"], color)


racine = tk.Tk()
racine.title("Jeu de couleurs")
racine.geometry("1130x300")
racine.config(background="azure2")
canvas = tk.Canvas(racine, width=300, height=900, bg="azure2")
canvas2 = tk.Canvas(racine, width=300, height=900, bg="azure2")


# Apparition du mot du milieu
compteur_lbl = tk.Label(canvas, text=str(compteur), font=("", 16))
compteur_lbl.pack()

label_title = tk.Label(canvas, text=rd.choice(mots), font=("Cassia", 40), fg=rd.choice(couleurs), bg='azure2')
label_title.pack()

label_text = tk.Label(canvas, text="Tapez la couleur des mots et pas le texte des mots !", bg="azure2", font=("Cassia", 20))
label_score = tk.Label(canvas, text="Score : " + str(score), bg="azure2", font=("Cassia", 18))


# ajout des boutons
first_button = tk.Button(canvas, text="Démarrer", command=incremente)
second_button = tk.Button(canvas, text="réinitialiser", command=réinitialiser)
third_button = tk.Button(canvas, text='Bleu', bg=couleurs[0], command=lambda: changement("blue"))
fourth_button = tk.Button(canvas, text='Rouge', bg=couleurs[1], command=lambda: changement("red"))
fifth_button = tk.Button(canvas, text='Vert', bg=couleurs[2], command=lambda: changement("green"))
sixth_button = tk.Button(canvas, text='Jaune', bg=couleurs[3], command=lambda: changement("yellow"))
seventh_button = tk.Button(canvas, text='Rose', bg=couleurs[4], command=lambda: changement("pink"))
eighth_button = tk.Button(canvas, text='Orange', bg=couleurs[5], command=lambda: changement("orange"))
ninth_button = tk.Button(canvas, text='Blanc', bg=couleurs[6], command=lambda: changement("white"))


# Affichage
label_text.pack()
label_score.pack()
first_button.pack(side=tk.LEFT, pady=50)
second_button.pack(side=tk.RIGHT, pady=50)
third_button.pack(side=tk.LEFT, padx=15, ipadx=20, ipady=10)
fourth_button.pack(side=tk.LEFT, padx=15, ipadx=20, ipady=10)
fifth_button.pack(side=tk.LEFT, padx=15, ipadx=20, ipady=10)
sixth_button.pack(side=tk.LEFT, padx=15, ipadx=20, ipady=10)
seventh_button.pack(side=tk.LEFT, padx=15, ipadx=20, ipady=10)
eighth_button.pack(side=tk.LEFT, padx=15, ipadx=20, ipady=10)
ninth_button.pack(side=tk.LEFT, padx=15, ipadx=20, ipady=10)
canvas.pack()


racine.mainloop()
