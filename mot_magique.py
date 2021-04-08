import tkinter
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import random

min = 0
max = 50
y = 0
nbre_magique = random.randint(min, max)

couleurs=("aliceblue","aqua","bisque","blueviolet","chartreuse","coral","darkkhaki","darkorange","deepskyblue","gainsboro","indigo","khaki","lightpink","lightsteelblue","magenta","maroon","olive","salmon","peru")

mainapp = tkinter.Tk()
mainapp.title("mot magique")
mainapp.geometry("1500x950")
mainapp.minsize(480, 360)
mainapp.config(background='sandybrown')

def start_jeu():

    def calcul():
        global y

        try:
            valeur_nbre = int(entree.get())
        except:
            x = random.randint(0, 18)
            reponse3 = Label(fen_jeu, text="Il faut noter un nombre (et pas de lettres) ", width=40, height=3, bg=couleurs[x], font=("Courrier", 20));
            reponse3.place(x=230, y=400)
            return

        x = random.randint(0, 18)
        y += 1

        if valeur_nbre < nbre_magique:
            reponse1 = Label(fen_jeu, text="Ton nombre est trop petit ", width=40, height=3, bg=couleurs[x], font=("Courrier", 20));
            reponse1.place(x=230, y=400)

        elif valeur_nbre > nbre_magique:
            reponse2 = Label(fen_jeu, text="Ton nombre est trop grand ", width=40, height=3, bg=couleurs[x], font=("Courrier", 20));
            reponse2.place(x=230, y=400)

        else:
            reponse = Label(fen_jeu, text=f"BRAVO, tu as trouvé le nombre magique {nbre_magique} en {y} essais", width=45, height=8, bg=couleurs[x], font=("Courrier", 30));
            reponse.place(x=95, y=180)
            y = 0
            # bouton recommencer
            recommencer = tkinter.Button(fen_jeu, text="RECOMMENCER", width=20, height=3, font=("Courrier", 12), bg='#FFCC99', command=start_jeu)
            recommencer.place(x=500, y=450)

    fen_jeu = tkinter.Toplevel()
    fen_jeu.title("chercher nombre")
    fen_jeu.geometry("1200x600")
    fen_jeu.config(background='cadetblue')

    bouton_start_jeu.destroy()
    nbre_magique = random.randint(min, max)

    label_texte = Label(fen_jeu, text="Trouve le nombre magique (entre 0 et 50) : ", width=50, height=5, bg='cadetblue', font=("Courrier", 20));
    label_texte.place(x=200, y=50)

    # entrée nombre
    entree = Entry(fen_jeu, font=("Courrier", 20), width=3);
    entree.place(x=550, y=180)

    # bouton entrer nombre
    b = Button(fen_jeu, text="ENTRER", width=10, height=2, font=("Courrier", 20), bg='#FFCC99', command=calcul)
    b.place(x=490, y=260)

#bouton start
bouton_start_jeu = tkinter.Button(mainapp, text="Démarrer le jeu", width=20, height=5, font=("Courrier", 40), bg='#339900',command=start_jeu);bouton_start_jeu.place(x=450, y=100)

# bouton quitter
def fermer_fenetre():
    mainapp.destroy()
quitter = tkinter.Button(mainapp, text="QUITTER", width=12, height=3, font=("Courrier", 12), bg='#FFCC99',command=fermer_fenetre)
quitter.place(x=1350, y=850)



mainapp.mainloop()