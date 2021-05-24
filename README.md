# jeu-de-couleurs
code du jeu de couleurs groupe 6 L1 MIASHS TD02 LSIN200

Ce jeu consiste à faire la différence entre la couleur du mot et le mot en lui même.
Pour cela, nous avons créé 7 cases avec des noms de couleurs différents: bleu, rouge, vert, jaune, rose, orange, blanc. Un nom de couleur aléatoire est affiché avec une couleur de caractère elle-même aléatoire (pas forcément la même).

Afin de commencer et de finir la partie, nous avons créé deux autres boutons (démarrer et réinitialiser). Le bouton démarrer lance un compteur de temps de 30 secondes et le bouton réininitaliser le remet à 30 et réinitalise le compteur de scores une fois la partie terminée (possible aussi lorsque la partie n'est pas encore terminée).
Afin de marquer un point, nous devons cliquer sur la couleur du mot et non sur le nom de la couleur affichée.
Par exemple, si le mot "bleu" est affiché avec une couleur verte, nous allons devoir cliquer sur la case verte et non sur la case bleue.
Si nous avons réussi, le compteur de score passe de 0 à 1 et ainsi de suite.
Cliquer sur une case de couleur fait apparaître un autre mot et une autre couleur peu importe si la réponse est bonne ou fausse.
Si jamais nous n'avons pas cliqué sur la bonne case, le compteur de score reste le même et un autre mot apparaît.
Une fois le temps écoulé, la seule action possible est de réinitaliser le jeu.


Nous avons essayé de passer au niveau 2. Simplement, par manque de temps, nous n'avons pas pu le finaliser. Nous vous mettons ci dessous le code à ajouter ligne 68 

label_title = tk.Label(canvas, text=rd.choice(mots), font=("Cassia", 40), fg=rd.choice(couleurs), bg='azure2')
label_title.pack()

label_title1 = tk.Label(canvas, text=rd.choice(mots), font=("Cassia", 40), fg=rd.choice(couleurs), bg='azure2')
label_title1.pack()

label_title2 = tk.Label(canvas, text=rd.choice(mots), font=("Cassia", 40), fg=rd.choice(couleurs), bg='azure2')
label_title2.pack()

label_text = tk.Label(canvas, text="Tapez la couleur des mots et pas le texte des mots !", bg="azure2", font=("Cassia", 20))
label_score = tk.Label(canvas, text="Score : " + str(score), bg="azure2", font=("Cassia", 18))

Ce code permet d'afficher plusieurs mots supplémentaires en plus de celui prévu initialement. 
Il faut également élargir la page en remplaçant 300 par 600 ligne 56.


