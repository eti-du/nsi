def anciennnete(self):
    return self.dateEmbauche - datetime.datetime.now().year
def augmentationDuSalaire(self):
    anc = self.anciennete()
    if  anc <5:
        self.salaire *= 1.02
    elif anc<10:
        self.salaire *= 1.05
    else:
        salaire *= 1.1
def afficherEmploye(self):
    print(self.matricule,self.nom,self.prenom,self.age(),self.annciennete(),self.salaire)