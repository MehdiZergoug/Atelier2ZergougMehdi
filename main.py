#On importe le module participant
import ModuleParticipant as me



#Affichage de la page de démarage
print(" _____________________________________________________")
print("|                                                     |")
print("|            Atelier02 4b5 ZergougMehdi               |")
print("|_____________________________________________________|")
print("|Choisissez la bonne réponse(a, b, c)                 |")
print("|q pour quitter                                       |")
print("|_____________________________________________________|")
print()

#Les données du joueur qui serviront pour faire l'objet
nomJoueur = input("Choisissez un nom: ")
listeReponses = []
nb_bonnesrep = 0
pointage = 0





#LECTURE DU FICHIER JSON QUESTIONS.JSON
#Ouverture du fichier Json Pour lancer le jeu,
#poser les questions et enregistrer les données de l'utilisateur
import json, os
fichier = "questions.json" 
#ouvrir le fichier
if os.path.exists(fichier):
    
    #lecture du fichier json
    with open(fichier, "r", encoding="utf-8") as fic_json:
        #envoyer les données dans une liste
        listeParticipant = json.load(fic_json)
        
        #parcourir la liste
        for i in range(len(listeParticipant)):
            
            # élément de la liste > dictionnaire
            participant_dict = listeParticipant[i]
            #afficher un élément du dictionnaire : clé et la valeur
            #On attribut les donnees
            question = participant_dict["q"]
            reponseA = participant_dict["a"]
            reponseB = participant_dict["b"]
            reponseC = participant_dict["c"]
            reponseBonne = participant_dict["rep"]
            nombrePoint = participant_dict["pts"]
            
            #On affiche les questions et les réponses possible
            print(str(i + 1) + ") " + str(question))
            print("<a> " + str(reponseA))
            print("<b> " + str(reponseB))
            print("<c> " + str(reponseC))
            reponseUsager = input("Entrez l'option (a/b/c) ou q pour quitter: ")
            
            #On analyse la réponse de l'usager
            #et on pose une action selon si
            #c'est une bonne ou une mauvaise réponse
            if reponseUsager == reponseBonne:
                print("Bonne réponse")
                listeReponses.append(participant_dict[reponseUsager])
                nb_bonnesrep += 1
                pointage += nombrePoint
            elif reponseUsager != reponseBonne and reponseUsager != "q" and reponseUsager == "a" or reponseUsager == "b" or reponseUsager == "c":
                print("Mauvaise réponse")
                listeReponses.append(participant_dict[reponseUsager])
            elif reponseUsager == "q":
                break
            #Des sauts de lignes
            print()
            print()
#Si le fichier n'est pas trouvé, on
#affiche un message d'erreur
else:
    print("Erreur, le fichier n'existe pas")

#On créer un objet participant
pt1 = me.participant(str(nomJoueur), listeReponses, nb_bonnesrep, pointage)





#ECRITURE DANS LE FICHIER PARTICIPANT.JSON
#On créer une variable dictionnaire
#avec les données de l'objet participant créé
person_dict = {"nomUtilisateur": str(pt1.nomParticipant),
"listeReponse": pt1.listeReponses,
"bonneReponse": pt1.nb_bonnesrep,
"pointage": pt1.pointage
}
don_dict = {"reponse": person_dict}

#nom du fichier
fichierUser = "participant.json"

#si le fichier existe:
if os.path.exists(fichierUser):
    #ouverture du fichier
    with open(fichierUser, encoding='utf-8') as fic_json :
        #charger les données json existantes
        donnees = json.load(fic_json)
        #ajout du nouveau participant dans la variable json
        donnees.append(don_dict)
        
# si le fichier n'existe pas        
else:
    donnees = list()
    donnees.append(don_dict) # ajout du participant dans la liste
    print(donnees)
    
# ecriture les données dans le fichier json
with open(fichierUser, "w", encoding="utf-8") as fic_json:
    json.dump(donnees, fic_json, indent=4)