from tkinter import *


#OUVERTURE DU FICHIER PARTICIPANT.JSON AVEC LES DONNES DES PARTIES
import json, os
fichier = "participant.json" 
#ouvrir le fichier
if os.path.exists(fichier):
    
    #lecture du fichier json
    with open(fichier, "r", encoding="utf-8") as fic_json:
        #envoyer les données dans une liste
        listeEtudiant = json.load(fic_json)
        listeUser = []
        #parcourir la liste
        for i in range(len(listeEtudiant)):
            #On récupère les données du fichier json
            #pour les mettre dans une liste de dictionnaires
            etudiant_dict = listeEtudiant[i]
            question = etudiant_dict["reponse"]
            dict_question = question
            listeUser.append(dict_question)
#Si le fichier n'Est pas trouvé, on affiche un message d'erreur
else:
    print("Erreur, le fichier n'existe pas")





#CRÉATION DE LA FENETRE GRAPHIQUE
#création fenêtre
fenetre = Tk()

#titre de la fenêtre
fenetre.title("Participant Graphique")

#taille
fenetre.geometry("450x300")

#Les labels qui s'afficheront au sommet de la fenetre
lbl_nomProjet = Label(fenetre, text="Résultat Quiz 4b5 - Zergoug Mehdi")
lbl_nomProjet.grid(column=1, row=0)
lbl_pointage = Label(fenetre, text="Pointage: ")
lbl_pointage.grid(column=1, row=1)
lbl_nbrBonneRep = Label(fenetre, text="Nombre de bonnes réponses: ")
lbl_nbrBonneRep.grid(column=1, row=2)

#fonction pour la liste
def lst_ville_onSelect(evt):
    #on atribut un index et une valeur
    index = int(lst_participant.curselection()[0])
    valeur = lst_participant.get(lst_participant.curselection())

frm_haut= Frame(fenetre)
frm_haut.grid(column=0, row=3)
lst_participant = Listbox(frm_haut)

#On fait une boucle pour mettre les
#participants dans la liste graphique
init = 0
for i in listeUser:
    lst_participant.insert((init), i["nomUtilisateur"])
    init+=1
lst_participant.pack()

# gestion de l'evenement
lst_participant.bind("<<ListboxSelect>>", lst_ville_onSelect)

#déclaration du text_box
message =''''''
text_box = Text(
    fenetre,
    height=13,
    width=40
)
text_box.grid(column=1, row=3)
text_box.insert('end', message)





#fonction pour afficher les données
#quand on appuie sur le bouton
def btn_afficher_clicked():
    donnees = lst_participant.curselection()
    donnees = int(''.join(map(str, donnees)))
    message = listeUser[int(donnees)]
    message = message["listeReponse"]
    text_box.delete('1.0', END)
    text_box.insert('end', message)
    
#fonction pour changer le texte
#des labels
def change():
    donnees = lst_participant.curselection()
    donnees = int(''.join(map(str, donnees)))
    message = listeUser[int(donnees)]
    messagePoint = message["pointage"]
    messageBonneReponse = message["bonneReponse"]
    lbl_pointage.config(text="Pointage: " + str(messagePoint))
    lbl_nbrBonneRep.config(text="Nombre de bonnes réponses: " + str(messageBonneReponse))

#fonction en contenant deux
#on la donnera au boutton qui
#sert à afficher les données
def btn_afficher_clicked_and_change():
    btn_afficher_clicked()
    change()

#On définit le boutton qui
#sert à afficher les données
button = Button(fenetre, text = "Afficher Les Données", width=40, command=btn_afficher_clicked_and_change)
button.grid(column=1, row=4)





#affichage de la fenêtre
fenetre.mainloop()