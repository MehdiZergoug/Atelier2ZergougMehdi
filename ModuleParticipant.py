class participant:
    
    #constructeur
    def __init__(self, nomParticipant, listeReponses, nb_bonnesrep, pointage):
        self.nomParticipant = nomParticipant
        self.listeReponses = listeReponses
        self.nb_bonnesrep = nb_bonnesrep
        self.pointage = pointage
    
    #retourne le nom du participant
    def __repr__(self):
        return self.nomParticipant
        
    #affiche les données du participant
    def affichageParticipant(self):
        print("Nom Participant : " + self.nomParticipant + 
              ", liste de réponses: " + self.listeReponses + 
              ", nombre de bonnes réponse: "+ self.nb_bonnesrep +
              ", pointage: " + self.pointage)